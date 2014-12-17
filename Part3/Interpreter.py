__author__ = 'Janusz'
# File was downloaded from http://home.agh.edu.pl/~mkuta/tk/zadanie2c/zadanie2C.html

import Part1.AST as AST
from Memory import *
from Exceptions import *
from visit import *
from collections import defaultdict

optype = {}
optype["+"] = lambda x, y: x + y
optype["-"] = lambda x, y: x - y
optype["*"] = lambda x, y: x * y
optype["/"] = lambda x, y: x / y
optype["%"] = lambda x, y: x % y
optype["|"] = lambda x, y: x | y
optype["&"] = lambda x, y: x & y
optype["^"] = lambda x, y: x ^ y
optype["SHL"] = lambda x, y: x << y
optype["SHR"] = lambda x, y: x >> y
optype["<"] = lambda x, y: 1 if x < y else 0
optype[">"] = lambda x, y: 1 if x > y else 0
optype["<="] = lambda x, y: 1 if x <= y else 0
optype[">="] = lambda x, y: 1 if x >= y else 0
optype["=="] = lambda x, y: 1 if x == y else 0
optype["!="] = lambda x, y: 1 if x != y else 0
optype["&&"] = lambda x, y: 1 if (x and y) else 0
optype["||"] = lambda x, y: 1 if (x or y) else 0

class Interpreter(object):
    def __init__(self):
        self.memory_stack = defaultdict(lambda: Memory(self.memory_stack[0]))
        self.memory_stack[0] = Memory()
        self.curr_stack = 1

    def get_scope(self, scope):
        self.curr_stack += 1
        self.memory_stack[self.curr_stack] = Memory(self.memory_stack[scope])
        return self.curr_stack

    @on('node')
    def visit(self, node, scope=0):
        pass

    @when(AST.Program)
    def visit(self, node, scope=0):
        node.decl.accept(self, scope)
        node.fun.accept(self, scope)
        node.instr.accept(self, scope)

    @when(AST.BinExpr)
    def visit(self, node, scope=0):
        r1 = node.left.accept(self, scope)
        r2 = node.right.accept(self, scope)
        #print 'jestem jestem jestem jestem jestem jestem jestem jestem jestem jestem jestem jestem jestem jestem jestem '
        print optype[node.op](r1, r2)
        return optype[node.op](r1, r2)

    @when(AST.UnExpr)
    def visit(self, node, scope=0):
        return node.expr.accept(self, scope)

    @when(AST.FunCall)
    def visit(self, node, scope=0):
        args = node.args.accept(self, scope)
        name = node.name.accept(self, scope)
        return name(*args)

    @when(AST.BrackExpr)
    def visit(self, node, scope=0):
        #print 'jestem jestem jestem jestem jestem jestem jestem jestem jestem jestem jestem jestem jestem jestem jestem '
        return node.expr.accept(self, scope)

    @when(AST.Init)
    def visit(self, node, scope=0):
        if node.name in self.memory_stack[scope].keys():
            raise Exception("Variable {0} already defined".format(node.name))
        value = node.value.accept(self, scope)
        self.memory_stack[scope][node.name] = value
        return value

    @when(AST.Inits)
    def visit(self, node, scope=0):
        for i in node.list:
            i.accept(self)

    @when(AST.Declaration)
    def visit(self, node, scope=0):
        node.inits.accept(self, scope)

    @when(AST.Declarations)
    def visit(self, node, scope=0):
        for i in node.list:
            i.accept(self)

    @when(AST.Epsilon)
    def visit(self, node, scope=0):
        pass

    @when(AST.Arg)
    def visit(self, node, scope=0):
        pass

    @when(AST.ArgsList)
    def visit(self, node, scope=0):
        pass

    @when(AST.Condition)
    def visit(self, node, scope=0):
        pass

    @when(AST.ExprList)
    def visit(self, node, scope=0):
        for i in node.list:
            i.accept(self)

    @when(AST.Instruction)
    def visit(self, node, scope=0):
        pass

    @when(AST.PrintInstr)
    def visit(self, node, scope=0):
        value = node.expr.accept(self, scope)
        print value
        return value

    @when(AST.Assignment)
    def visit(self, node, scope=0):
        if node.name in self.memory_stack[scope].scope_keys():
            value = node.expr.accept(self, scope)
            self.memory_stack[scope].scope_setitem(node.name, value)
            return value
        else:
            raise Exception("Undeclared variable {0}".format(node.name))

    @when(AST.ReturnInstr)
    def visit(self, node, scope=0):
        raise ReturnValueException(node.returns.accept(self, scope))

    @when(AST.ContinueInstr)
    def visit(self, node, scope=0):
        raise ContinueException()

    @when(AST.BreakInstr)
    def visit(self, node, scope=0):
        raise BreakException()

    @when(AST.LabeledInstr)
    def visit(self, node, scope=0):
        return node.instruction.accept(self, scope)

    @when(AST.ChoiceInstruction)
    def visit(self, node, scope=0):
        pass

    @when(AST.IfInstr)
    def visit(self, node, scope=0):
        if node.cond.accept(self, scope):
            node.instr.accept(self, scope)

    @when(AST.IfElseInstr)
    def visit(self, node, scope=0):
        if node.cond.accept(self, scope):
            node.instr.accept(self, scope)
        else:
            node.elseinstr.accept(self, scope)

    @when(AST.Instructions)
    def visit(self, node, scope=0):
        for i in node.list:
            i.accept(self)

    @when(AST.WhileInstr)
    def visit(self, node, scope=0):
        r = None
        try:
            while node.cond.accept(self, scope):
                try:
                    r = node.instr.accept(self, scope)
                except ContinueException:
                    pass
        except BreakException:
            pass

        return r

    @when(AST.RepeatInstr)
    def visit(self, node, scope=0):
        run = True
        r = None

        try:
            while run:
                try:
                    r = node.instr.accept(self, scope)
                except ContinueException:
                    pass

                run = not node.cond.accept(self, scope)
        except BreakException:
            pass

        return r

    @when(AST.CompoundInstr)
    def visit(self, node, scope=0):
        new_scope = self.get_scope(scope)
        node.decl.accept(self, new_scope)
        node.instr.accept(self, new_scope)

    @when(AST.FunDef)
    def visit(self, node, scope=0):
        def fun(*args):
            new_scope = self.get_scope(scope)
            if len(args) != len(node.args):
                raise Exception("{0} takes {1} argument(s); {2} given".format(node.name, len(node.args), len(args)))

            for i in range(len(node.args)):
                argument = node.args.elements[i]
                self.memory_stack[new_scope][argument.name] = args[i]

            try:
                node.instr.accept(self, scope=new_scope)
            except ReturnValueException as e:
                return e.value

        self.memory_stack[scope][node.name] = fun

    @when(AST.FunDefs)
    def visit(self, node, scope=0):
        for i in node.list:
            i.accept(self)

    @when(AST.Integer)
    def visit(self, node, scope=0):
        return int(node.value)

    @when(AST.Float)
    def visit(self, node, scope=0):
        return float(node.value)

    @when(AST.String)
    def visit(self, node, scope=0):
        return node.value[1:-1]

    @when(AST.Variable)
    def visit(self, node, scope=0):
        pass