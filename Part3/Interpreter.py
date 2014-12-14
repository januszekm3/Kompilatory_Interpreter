__author__ = 'Janusz'
# File was downloaded from http://home.agh.edu.pl/~mkuta/tk/zadanie2c/zadanie2C.html

import AST
import SymbolTable
from Memory import *
from Exceptions import *
from visit import *

class Interpreter(object):
    def __init__(self):
        self.globalMemory = MemoryStack(Memory("global"))
        self.functionMemories = []

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Node)
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
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        return eval("a" + node.op + "b", {"a": r1, "b": r2})

    @when(AST.UnExpr)
    def visit(self, expr):
        pass

    @when(AST.FunCall)
    def visit(self, node):
        pass

    @when(AST.BrackExpr)
    def visit(self, expr):
        pass


    @when(AST.Init)
    def visit(self, node):
        value_accept = node.value.accept(self)
        self.globalMemory.peek().put(node.name, value_accept)
        return value_accept


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

    @when(AST.Arg)
    def visit(self, node):
        return node.name

    @when(AST.ArgsList)
    def visit(self, node):
        for i in node.list:
            i.accept(self)

    @when(AST.Condition)
    def visit(self, expr):
        pass

    @when(AST.ExprList)
    def visit(self, node):
        for i in node.list:
            i.accept(self)

    @when(AST.Instruction)
    def visit(self, node):
        pass

    @when(AST.PrintInstr)
    def visit(self, node):
        print node.expr.accept(self)

    @when(AST.Assignment)
    def visit(self, node):
        expr_accept = node.expr.accept(self)
        self.globalMemory.set(node.name, expr_accept)
        return expr_accept

    @when(AST.ReturnInstr)
    def visit(self, node):
        value = node.expression.accept(self)
        raise ReturnValueException(value)

    @when(AST.ContinueInstr)
    def visit(self, node):
        raise ContinueException()

    @when(AST.BreakInstr)
    def visit(self, node):
        raise BreakException()

    @when(AST.LabeledInstr)
    def visit(self, node):
        pass

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
        elif node.elseinstr:
            return node.elseinstr.accept(self)
        else:
            pass

    @when(AST.Instructions)
    def visit(self, node):
        for i in node.list:
            i.accept(self)

    @when(AST.WhileInstr)
    def visit(self, node):
        r = None
        while node.cond.accept(self):
            r = node.body.accept(self)
        return r

    @when(AST.RepeatInstr)
    def visit(self, node):
        while True:
            try:
                node.instr.accept(self)
                if node.cond.accept(self):
                    break
            except BreakException:
                break
            except ContinueException:
                pass

    @when(AST.CompoundInstr)
    def visit(self, node):
        node.decl.accept(self)
        node.instr.accept(self)

    @when(AST.FunDef)
    def visit(self, node):
        self.globalMemory.peek().put(node.name, node)

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