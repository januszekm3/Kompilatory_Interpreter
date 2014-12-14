__author__ = 'Janusz'

#!/usr/bin/python
from collections import defaultdict
from AST import *
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
        #print "node {} has visitor {}".format(str(node), str(visitor))
        return visitor(node)

    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        elif hasattr(node, "children"):
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, Node):
                            self.visit(item)
                elif isinstance(child, Node):
                    self.visit(child)

                    # simpler version of generic_visit, not so general
                    #def generic_visit(self, node):
                    #    for child in node.children:
                    #        self.visit(child)


class TypeChecker(NodeVisitor):
    def __init__(self):
        self.table = SymbolTable(None, "root")
        self.actType = ""
        self.isValid = True

    #def visit_Node(object):
    #def visit_Const(Node):
    #def visit_Expr(Node):

    def visit_BinExpr(self, node):
        r1 = self.visit(node.left)
        r2 = self.visit(node.right)
        op = node.op
        if ttype[op][r1][r2] is None:
            self.isValid = False
            print "Bad expression {} in line {}".format(node.op, node.line)
        return ttype[op][r1][r2]

    #def visit_UnExpr(Expr):
    #def visit_FunCall(self, node):
    #def visit_BrackExpr(Expr):

    def visit_Init(self, node):
        initType = self.visit(node.expr)
        if initType == self.actType or (initType == "int" and self.actType == "float") or (
                    initType == "float" and self.actType == "int"):
            if self.table.get(node.name) is not None:
                self.isValid = False
                print "Invalid definition of {} in line: {}. Entity redefined". \
                    format(node.name, node.line)
            else:
                self.table.put(node.name, VariableSymbol(node.name, self.actType))
        else:
            self.isValid = False
            print "Bad assignment of {} to {} in line {}".format(initType, self.actType, node.line)

    #def visit_Inits(Node):

    def visit_Declaration(self, node):
        self.actType = node.type
        self.visit(node.inits)
        self.actType = ""

    #def visit_Declarations(Node):
    #def visit_Epsilon(Node):

    def visit_Arg(self, node):
        if self.table.get(node.name) is not None:
            self.isValid = False
            print "Argument {} already defined. Line: {}".format(node.name, node.line)
        else:
            self.table.put(node.name, VariableSymbol(node.name, node.type))

    def visit_ArgsList(self, node):
        for i in node.list:
            self.visit(i)
        self.actFunc.extractParams()

    #def visit_Condition(Node):
    #def visit_ExprList(Node):
    #def visit_Instruction(Node):

    def visit_PrintInstr(self, node):
        self.visit(node.expr)

    def visit_Assignment(self, node):
        definition = self.table.getGlobal(node.id)
        type = self.visit(node.expr)
        if definition is None:
            self.isValid = False
            print "Used undefined symbol {} in line {}".format(node.name, node.line)
        elif type != definition.type and (definition.type != "float" and definition != "int"):
            self.isValid = False
            print "Bad assignment of {} to {} in line {}.".format(type, definition.type, node.line)

    def visit_ReturnInstr(self, node):
        if self.actFunc is None:
            self.isValid = False
            print "Return placed outside of a function in line {}".format(node.line)
        else:
            type = self.visit(node.expression)
            if type != self.actFunc.type and (self.actFunc.type != "float" or type != "int"):
                self.isValid = False
                print "Invalid return type of {} in line {}. Expected {}".format(type, node.line, self.actFunc.type)

    #def visit_ContinueInstr(Instruction):
    #def visit_BreakInstr(Instruction):

    def visit_LabeledInstr(self, node):
        self.visit(node.instr)

    def visit_ChoiceInstruction(self, node):
        self.visit(node.condition)
        self.visit(node.action)
        if node.alternateAction is not None:
            self.visit(node.alternateAction)

    #def visit_IfInstr(ChoiceInstruction):
    #def visit_IfElseInstr(ChoiceInstruction):
    #def visit_Instructions(Instruction):

    def visit_WhileInstruction(self, node):
        self.visit(node.condition)
        self.visit(node.instr)

    def visit_RepeatInstr(self, node):
        self.visit(node.cond)
        self.visit(node.instr)

    def visit_CompoundInstr(self, node):
        innerScope = SymbolTable(self.table, "innerScope")
        self.table = innerScope
        if node.declarations is not None:
            self.visit(node.declarations)
        self.visit(node.instructions)
        self.table = self.table.getParentScope()

    def visit_FunDef(self, node):
        if self.table.get(node.name):
            self.isValid = False
            print "Function {} already defined. Line: {}".format(node.name, node.line)
        else:
            function = FunctionSymbol(node.name, node.retType, SymbolTable(self.table, node.name))
            self.table.put(node.name, function)
            self.actFunc = function
            self.table = self.actFunc.table
            if node.args is not None:
                self.visit(node.args)
            self.visit(node.body)
            self.table = self.table.getParentScope()
            self.actFunc = None

    #def visit_FunDefs(Node):

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

################

    def visit_GroupedExpression(self, node):
        return self.visit(node.interior)

    def visit_InvocationExpression(self, node):
        funDef = self.table.getGlobal(node.name)
        if funDef is None or not isinstance(funDef, FunctionSymbol):
            self.isValid = False
            print "Function {} not defined. Line: {}".format(node.name, node.line)
        else:
            if ((node.args is None and funDef.params != [] ) or len(node.args.children) != len(funDef.params)):
                self.isValid = False
                print "Invalid number of arguments in line {}. Expected {}". \
                    format(node.line, len(funDef.params))
            else:
                types = [self.visit(x) for x in node.args.children]
                expectedTypes = funDef.params
                for actual, expected in zip(types, expectedTypes):
                    if actual != expected and not (actual == "int" and expected == "float"):
                        self.isValid = False
                        print "Mismatching argument types in line {}. Expected {}, got {}". \
                            format(node.line, expected, actual)
            return funDef.type