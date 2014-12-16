__author__ = 'Janusz'
# File was downloaded from http://home.agh.edu.pl/~mkuta/tk/zadanie2c/zadanie2C.html

import Part1.AST as AST
from Memory import *
from Exceptions import *
from visit import *

optype = {}
optype["+"] = lambda x, y: x + y
optype["-"] = lambda x, y: x - y
optype["*"] = lambda x, y: x * y
optype["/"] = lambda x, y: x / y
optype["%"] = lambda x, y: x % y
optype["<"] = lambda x, y: 1 if x < y else 0
optype[">"] = lambda x, y: 1 if x > y else 0
optype["shl"] = lambda x, y: x << y
optype["shr"] = lambda x, y: x >> y
optype["|"] = lambda x, y: x | y
optype["&"] = lambda x, y: x & y
optype["^"] = lambda x, y: x ^ y
optype["<="] = lambda x, y: 1 if x <= y else 0
optype[">="] = lambda x, y: 1 if x >= y else 0
optype["=="] = lambda x, y: 1 if x == y else 0
optype["!="] = lambda x, y: 1 if x != y else 0
optype["&&"] = lambda x, y: 1 if (x and y) else 0
optype["||"] = lambda x, y: 1 if (x or y) else 0

class Interpreter(object):
    def __init__(self):
        self.globalMemory = MemoryStack(Memory("global"))
        self.functionMemory = MemoryStack()

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Const)
    def visit(self, node):
        return node.value

    @when(AST.Expr)
    def visit(self, node):
        pass

    # @when(AST.BinOp) - Cannot find reference 'BinOp' in 'AST.py'
    # changed to AST.BinExpr
    @when(AST.BinExpr)
    def visit(self, expr):
        r1 = expr.left.accept(self)
        r2 = expr.right.accept(self)
        return optype[expr.op](r1, r2)

    @when(AST.UnExpr)
    def visit(self, node):
        return node.accept(self)

#    @when(AST.FunCall)
#    def visit(self, node):
#        args = node.args.accept(self)
#        fun = node.name.accept(self)
#        return fun(*args)

    @when(AST.BrackExpr)
    def visit(self, expr):
        return expr

    @when(AST.Init)
    def visit(self, node):
        self.globalMemory.push(node.value.accept(self))

    @when(AST.Inits)
    def visit(self, node):
        for i in node.list:
            i.accept(self)

    @when(AST.Declaration)
    def visit(self, node):
        node.inits.accept(self)

    @when(AST.Declarations)
    def visit(self, node):
        for i in node.list:
            i.accept(self)

    @when(AST.Epsilon)
    def visit(selfself, node):
        pass

    @when(AST.Arg)
    def visit(self, node):
        return node.name

    @when(AST.ArgsList)
    def visit(self, node):
        for i in node.list:
            i.accept(self)

    @when(AST.Condition)
    def visit(self, expr):
        return expr

    @when(AST.ExprList)
    def visit(self, node):
        for i in node.list:
            i.accept(self)

    @when(AST.Instruction)
    def visit(self, node):
        pass

    @when(AST.PrintInstr)
    def visit(self, node):
        value = node.expr.accept(self)
        print value
        return value

    @when(AST.Assignment)
    def visit(self, node):
        nea = node.expr.accept(self)
#        self.globalMemory.set(node.name, nea)
        return nea

    @when(AST.ReturnInstr)
    def visit(self, node):
        raise ReturnValueException(node.expr.accept(self))

    @when(AST.ContinueInstr)
    def visit(self, node):
        raise ContinueException()

    @when(AST.BreakInstr)
    def visit(self, node):
        raise BreakException()

    @when(AST.LabeledInstr)
    def visit(self, node):
        node.instr.accept(self)

    @when(AST.ChoiceInstruction)
    def visit(self, instruction):
        pass

    @when(AST.IfInstr)
    def visit(self, node):
        if node.cond.accept(self):
            return node.instr.accept(self)
        else:
            pass

    @when(AST.IfElseInstr)
    def visit(self, node):
        if node.cond.accept(self):
            return node.instr.accept(self)
        else:
            return node.elseinstr.accept(self)

    @when(AST.Instructions)
    def visit(self, node):
        for i in node.list:
            i.accept(self)

    @when(AST.WhileInstr)
    def visit(self, node):
        r = None
        try:
            while node.cond.accept(self):
                try:
                    r = node.instr.accept(self)
                except ContinueException:
                    pass
        except BreakException:
            pass
        return r

    @when(AST.RepeatInstr)
    def visit(self, node):
        run = True
        r = None

        try:
            while run:
                try:
                    r = node.instr.accept(self)
                except ContinueException:
                    pass

                run = not node.cond.accept(self)
        except BreakException:
            pass
        return r

    @when(AST.CompoundInstr)
    def visit(self, node):
        node.decl.accept(self)
        node.instr.accept(self)

    @when(AST.FunDef)
    def visit(self, node):
        def fun(*args):
            if len(args) != len(node.args):
                raise Exception("{0} takes {1} argument(s); {2} given".format(node.id, node.arity(), len(args)))
            for i in range(len(node.args)):
                argument = node.args.elements[i]
                self.functionMemory.insert(argument.name, args[i])
            try:
                node.instr.accept(self)
            except ReturnValueException as e:
                return e.value

    @when(AST.FunDefs)
    def visit(self, node):
        for i in node.list:
            i.accept(self)

    @when(AST.Program)
    def visit(self, node):
        node.decl.accept(self)
        node.fun.accept(self)
        node.instr.accept(self)

    @when(AST.Integer)
    def visit(self, node):
        return int(node.value)

    @when(AST.Float)
    def visit(self, node):
        return float(node.value)

    @when(AST.String)
    def visit(self, node):
        return node.value

    @when(AST.Variable)
    def visit(self, node):
        return self.globalMemory.get(node.name)