__author__ = 'Janusz'

#!/usr/bin/python
from collections import defaultdict
from SymbolTable import SymbolTable, FunctionSymbol, VariableSymbol

ttype = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))
for op in ['+', '-', '*', '/', '%', '<', '>', '<<', '>>', '|', '&', '^', '<=', '>=', '==', '!=']:
    ttype[op]['int']['int'] = 'int'

for op in ['+', '-', '*', '/']:
    ttype[op]['int']['float'] = 'float'
    ttype[op]['float']['int'] = 'float'
    ttype[op]['float']['float'] = 'float'

for op in ['<', '>', '<=', '>=', '==', '!=']:
    ttype[op]['int']['float'] = 'int'
    ttype[op]['float']['int'] = 'int'
    ttype[op]['float']['float'] = 'int'

ttype['+']['string']['string'] = 'string'
ttype['*']['string']['int'] = 'string'

for op in ['<', '>', '<=', '>=', '==', '!=']:
    ttype[op]['string']['string'] = 'int'

class NodeVisitor(object):
    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node): # Any of visitor function exists
        return 1

class TypeChecker(NodeVisitor):
    def __init__(self):
        self.table = SymbolTable(None, "root")
        self.actType = ""
        self.isValid = True

    def visit_Const(self, node):
        value = node.value
        if value[0] == '"' and value[len(value) - 1] == '"':
            type = 'string'
        else:
            try:
                int(value)
                type = 'int'
            except ValueError:
                try:
                    float(value)
                    type = 'float'
                except ValueError:
                    print "line {1}: Value's {0} type is not recognized".format(value, node.line)
                    self.found_any_errors = True
        return type

    def visit_Expr(self, node):
        pass

    def visit_BinExpr(self, node):
        r1 = self.visit(node.left)
        r2 = self.visit(node.right)
        op = node.op
        if ttype[op][r1][r2] is None:
            self.isValid = False
            print "Bad expression {} in line {}".format(node.op, node.line)
        return ttype[op][r1][r2]

    def visit_UnExpr(Expr):
        pass

    def visit_FunCall(self, node):
        for i in node.instr:
            i.accept(self)

    def visit_BrackExpr(Expr):
        pass

    def visit_Init(self, node):
        initType = self.visit(node.expr)
        if initType == self.actType or (initType == "int" and self.actType == "float") or (
                    initType == "float" and self.actType == "int"):
            if self.table.get(node.name) is not None:
                self.isValid = False
                print "Invalid definition of {} in line: {}.".format(node.name, node.line)
            else:
                self.table.put(node.name, VariableSymbol(node.name, self.actType))
        else:
            self.isValid = False
            print "Bad assignment of {} to {} in line {}".format(initType, self.actType, node.line)

    def visit_Inits(self, node):
        for i in node.list:
            self.visit_Init(i)

    def visit_Declaration(self, node):
        for init in node.inits.elements:
            self.visit(init)

    def visit_Declarations(self, node):
        for i in node.list:
            self.visit_Declaration(i)

    def visit_Epsilon(self, node):
        pass

    def visit_Arg(self, node):
        if self.table.get(node.name) is not None:
            self.isValid = False
            print "Argument {} already defined. Line: {}".format(node.name, node.line)
        else:
            self.table.put(node.name, VariableSymbol(node.name, node.type))

    def visit_ArgsList(self, node):
        for i in node.list:
            self.visit_Arg(i)

    def visit_Condition(self, node):
        pass

    def visit_ExprList(self, node):
        for i in node.list:
            self.visit_Expr(i)

    def visit_Instruction(self, node):
        pass

    def visit_PrintInstr(self, node):
        self.visit(node.expr)

    def visit_Assignment(self, node):
        definition = self.table.getGlobal(node.name)
        type = self.visit(node.expr)
        if definition is None:
            self.isValid = False
            print "Used undefined symbol {} in line {}".format(node.name, node.line)
        elif type != definition.type and (definition.type != "float" and definition != "int"):
            self.isValid = False
            print "Bad assignment of {} to {} in line {}.".format(type, definition.type, node.line)

    def visit_ReturnInstr(self, node):
        self.visit(node.returns)

    def visit_ContinueInstr(self, node):
        pass

    def visit_BreakInstr(self, node):
        pass

    def visit_LabeledInstr(self, node):
        self.visit(node.instr)

    def visit_ChoiceInstruction(self, node):
        pass

    def visit_IfInstr(self, node):
        self.visit(node.cond)
        self.visit(node.instr)

    def visit_IfElseInstr(self, node):
        self.visit(node.cond)
        self.visit(node.instr)
        self.visit(node.elseinstr)

    def visit_Instructions(self, node):
        for i in node.list:
            self.visit_Instruction(i)

    def visit_WhileInstruction(self, node):
        self.visit(node.condition)
        self.visit(node.instr)

    def visit_RepeatInstr(self, node):
        self.visit(node.cond)
        self.visit(node.instr)

    def visit_CompoundInstr(self, node):
        innerScope = SymbolTable(self.table, "innerScope")
        self.table = innerScope
        if node.decl is not None:
            self.visit(node.decl)
        self.visit(node.instr)
        self.table = self.table.getParentScope()

    def visit_FunDef(self, node):
        argList = []
        for arg in node.args.elements:
            a = self.visit(arg)
            argList.append(a)
        self.visit(node.instr)

    def visit_FunDefs(self, node):
        for i in node.list:
            self.visit_FunDef(i)

    def visit_Program(self, node):
        self.visit(node.decl)
        self.visit(node.fun)
        self.visit(node.instr)

    def visit_Integer(Const):
        return 'int'

    def visit_Float(Const):
        return 'float'

    def visit_String(Const):
        return 'string'

    def visit_Variable(self, node):
        definition = self.table.getGlobal(node.name)
        if definition is None:
            self.isValid = False
            print "Undefined symbol {} in line {}".format(node.op, node.line)
        else:
            return definition.type