__author__ = 'Janusz'
# File was downloaded from http://home.agh.edu.pl/~mkuta/tk/zadanie2c/zadanie2C.html

import Part1.AST as AST
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
        if len(self.functionMemories) == 0:
            self.globalMemory.insert(node.id, node.expression.accept(self))
        else:
            self.functionMemories[len(self.functionMemories) - 1].put(node.id, node.expression.accept(self))

    @when(AST.Inits)
    def visit(self, node):
        for child in node.children:
            child.accept(self)

    @when(AST.Declaration)
    def visit(self, node):
        node.inits.accept(self)

    @when(AST.Declarations)
    def visit(self, node):
        for child in node.children:
            child.accept(self)

    #@when(AST.Epsilon)

    @when(AST.Arg)
    def visit(self, node):
        return node.name

    @when(AST.ArgsList)
    def visit(self, node):
        for child in node.children:
            child.accept(self)

    @when(AST.Condition)
    def visit(self, expr):
        pass

    @when(AST.ExprList)
    def visit(self, node):
        for child in node.children:
            child.accept(self)

    @when(AST.Instruction)
    def visit(self, node):
        pass

    @when(AST.PrintInstr)
    def visit(self, node):
        print node.expr.accept(self)

    @when(AST.Assignment)
    def visit(self, node):
        if len(self.functionMemories) == 0 or self.functionMemories[len(self.functionMemories) - 1].put_existing(node.id, node.expression.accept(self)) is False:
            self.globalMemory.set(node.id, node.expression.accept(self))

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

    #@when(AST.IfInstr)

    #@when(AST.IfElseInstr)

    @when(AST.Instructions)
    def visit(self, node):
        for instruction in node.instructions:
            instruction.accept(self)

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
                node.instructions.accept(self)
                if node.condition.accept(self):
                    break
            except BreakException:
                break
            except ContinueException:
                pass

    @when(AST.CompoundInstr)
    def visit(self, node):
        function = False
        if len(self.functionMemories) == 0:
            self.globalMemory.push(Memory("compound"))
        else:
            function = True
            self.functionMemories[len(self.functionMemories) - 1].push(Memory("compound"))
        node.declarations.accept(self)
        node.instructions.accept(self)

        if function is False:
            self.globalMemory.pop()
        else:
            self.functionMemories[len(self.functionMemories) - 1].pop()

    @when(AST.FunDef)
    def visit(self, node):
        node.compound_instr.accept(self)

    @when(AST.FunDefs)
    def visit(self, node):
        for fundef in node.fundefs:
            self.globalMemory.insert(fundef.id, fundef)

    @when(AST.Program)
    def visit(self, node):
        node.declarations.accept(self)
        node.fundefs.accept(self)
        node.instructions.accept(self)

    @when(AST.Integer)
    def visit(self, const):
        pass

    @when(AST.Float)
    def visit(self, const):
        pass

    @when(AST.String)
    def visit(self, const):
        pass

    @when(AST.Variable)
    def visit(self, node):
        pass