#!/usr/bin/python
from ttype import ttype
import Part1.AST as AST
import SymbolTable

class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    #def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)

class TypeChecker(NodeVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable.SymbolTable(None, "program")
        self.current_symbol_table = self.symbol_table
        self.carried_info = {}
        self.carried_info["funsymbol"] = None
        self.in_loop = False
        self.counter = 0

    def visit_Integer(self, node):
        return 'int'

    def visit_Float(self, node):
        return 'float'

    def visit_String(self, node):
        return 'string'

    def visit_BinExpr(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        type1 = self.visit(node.left)     # type1 = node.left.accept(self)
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op;


        type = ttype[op][type1][type2]
        if type == 'error':
            print "Wrong expression type at " + node.line.__str__()

        return type

    def visit_UnExpr(self, node):

        if isinstance(node.expr, AST.Node):
            type = self.visit(node.expr)
            if type == 'error':
                print "Wrong expression type at " + node.line.__str__()
            return type
        #identifier
        else:
            variable = self.current_symbol_table.get(node.expr)
            cst = self.current_symbol_table
            while variable is None:
                cst = cst.getParentScope()
                if cst is None:
                    print "Usage of undeclared variable at " + node.line.__str__()
                    return "error"
                else:
                    variable = cst.get(node.expr)

            return variable.type

    def visit_FunCall(self, node):

        funsymbol = self.current_symbol_table.get(node.name)
        cst = self.current_symbol_table
        while funsymbol is None:
            cst = cst.getParentScope()
            if cst is None:
                print "Usage of undeclared function at " + node.line.__str__()
                return "error"
            else:
                funsymbol = cst.get(node.name)

        argtypes = self.visit(node.args)
        if argtypes != funsymbol.argtypes:
            print "Wrong arguments  at " + node.line.__str__()

        return funsymbol.type

    def visit_BrackExpr(self, node):
        type = self.visit(node.expr)
        if type == 'error':
            print "Wrong expression type at " + node.line.__str__()
        return type

    def visit_Init(self, node):
        type = self.visit(node.value)

        if type == 'error':
            print "Wrong expression type at " + node.line.__str__()
            return 'error'
        elif type == 'int' or type == 'float':
            if self.carried_info["declared_type"] == 'string':
                print "Wrong type assignment at " + node.line.__str__()
                return 'error'
        else:
          if self.carried_info["declared_type"] != 'string':
                print "Wrong type assignment at " + node.line.__str__()
                return 'error'

        self.current_symbol_table.put(node.name, SymbolTable.VariableSymbol(node.name, self.carried_info["declared_type"]))

        return self.carried_info["declared_type"]

    def visit_Inits(self, node):
        for i in node.list:
            self.visit(i)

    def visit_Declaration(self, node):
        self.carried_info["declared_type"] = node.type

        self.visit(node.inits)

    def visit_Declarations(self, node):
        for i in node.list:
            self.visit(i)

    def visit_Epsilon(self, node):
        pass

    def visit_Arg(self, node):
        self.current_symbol_table.put(node.name, SymbolTable.VariableSymbol(node.name, node.type))
        self.carried_info["funsymbol"].argtypes.append(node.type)
        return node.type

    def visit_ArgsList(self, node):
        argtypes = []
        for i in node.list:
            argtypes.append(self.visit(i))

        for i in xrange(0, len(argtypes)):
            if not argtypes[i] is str:
                if len(argtypes[i]) == 1:
                    argtypes[i] = argtypes[i][0]

        return argtypes

    def visit_Condition(self, node):
        type = self.visit(node.expr)

        if type != 'int':
            print "Wrong condition type at " + node.line.__str__()
            return 'error'

        return type

    def visit_ExprList(self, node):
        argtypes = []
        for i in node.list:
            argtypes.append(self.visit(i))

        for i in xrange(0, len(argtypes)):
            if not argtypes[i] is str:
                if len(argtypes[i]) == 1:
                    argtypes[i] = argtypes[i][0]

        return argtypes

    def visit_PrintInstr(self, node):
        type = self.visit(node.expr)

        if type == 'error':
            print "Wrong value passed to print at " + node.line.__str__()

        return type

    def visit_Assignment(self, node):
        right = self.visit(node.expr)

        left = self.current_symbol_table.get(node.name)
        cst = self.current_symbol_table
        while left is None:
            cst = cst.getParentScope()
            if cst is None:
                print "Usage of undeclared variable at " + node.line.__str__()
                return "error"
            else:
                left = cst.get(node.name)

        left = left.type
        if right == 'error':
            print "Wrong type at the right side of assignment at " + node.line.__str__()
            return right

        if right != left:
            if (right == 'int' and left == 'float') or (right == 'float' and left == 'int'):
                return left
            else:
               print "Wrong type at the right side of assignment at " + node.line.__str__()
               return 'error'

        return left

    def visit_ReturnInstr(self, node):
        right = self.visit(node.expr)

        left = self.carried_info["funsymbol"].type

        if right == 'error':
            print "Wrong returned type at " + node.line.__str__()
            return right

        if right != left:
            if (right == 'int' and left == 'float') or (right == 'float' and left == 'int'):
                return left
            else:
               print "Wrong returned type at " + node.line.__str__()
               return 'error'

        return left

    def visit_ContinueInstr(self, node):
        if self.in_loop == False:
            print "Continue used outside of a loop at " + node.line.__str__()
            return 'error'

        return 'int'

    def visit_BreakInstr(self, node):
        if self.in_loop == False:
            print "Break used outside of a loop at " + node.line.__str__()
            return 'error'

        return 'int'

    def visit_LabeledInstr(self, node):
        self.visit(node.instr)

    def visit_IfInstr(self, node):
        self.visit(node.cond)

        newscope = SymbolTable.SymbolTable(self.current_symbol_table, "if" + self.counter.__str__())
        self.counter += 1
        self.current_symbol_table = newscope
        self.visit(node.instr)
        self.current_symbol_table = self.current_symbol_table.getParentScope()

    def visit_IfElseInstr(self, node):
        self.visit(node.cond)

        newscope = SymbolTable.SymbolTable(self.current_symbol_table, "if" + self.counter.__str__())
        self.counter += 1
        self.current_symbol_table = newscope
        self.visit(node.instr)
        self.current_symbol_table = self.current_symbol_table.getParentScope()

        newscope = SymbolTable.SymbolTable(self.current_symbol_table, "if" + self.counter.__str__())
        self.counter += 1
        self.current_symbol_table = newscope
        self.visit(node.elseinstr)
        self.current_symbol_table = self.current_symbol_table.getParentScope()

    def visit_Instructions(self, node):
        for i in node.list:
            self.visit(i)

    def visit_WhileInstr(self, node):
        self.visit(node.cond)

        self.in_loop = True

        newscope = SymbolTable.SymbolTable(self.current_symbol_table, "while" + self.counter.__str__())
        self.counter += 1
        self.current_symbol_table = newscope
        self.visit(node.instr)
        self.current_symbol_table = self.current_symbol_table.getParentScope()

        self.in_loop = False

    def visit_RepeatInstr(self, node):
        self.visit(node.cond)

        self.in_loop = True

        newscope = SymbolTable.SymbolTable(self.current_symbol_table, "repeat" + self.counter.__str__())
        self.counter += 1
        self.current_symbol_table = newscope
        self.visit(node.instr)
        self.current_symbol_table = self.current_symbol_table.getParentScope()

        self.in_loop = False

    def visit_CompoundInstr(self, node):
        newscope = SymbolTable.SymbolTable(self.current_symbol_table, "compound" + self.counter.__str__())
        self.counter += 1
        self.current_symbol_table = newscope
        self.visit(node.decl)
        self.visit(node.instr)
        self.current_symbol_table = self.current_symbol_table.getParentScope()

    def visit_FunDef(self, node):
        funsymbol = SymbolTable.FunctionSymbol(node.name, node.type)
        self.current_symbol_table.put(node.name, funsymbol)
        newscope = SymbolTable.SymbolTable(self.current_symbol_table, "fundef" + self.counter.__str__())
        self.counter += 1
        self.current_symbol_table = newscope
        prevsym = self.carried_info["funsymbol"]
        self.carried_info["funsymbol"] = funsymbol

        self.visit(node.args)
        self.visit(node.instr)

        self.carried_info["funsymbol"] = prevsym
        self.current_symbol_table = self.current_symbol_table.getParentScope()

    def visit_FunDefs(self, node):
        for i in node.list:
            self.visit(i)

    def visit_Program(self, node):
        self.visit(node.decl)
        self.visit(node.fun)
        self.visit(node.instr)

    def visit_RelExpr(self, node):
        type1 = self.visit(node.left)     # type1 = node.left.accept(self)
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        # ...
        #

    def visit_Integer(self, node):
        return 'int'

    #def visit_Float(self, node):
    # ...
    #

    # ...
    #