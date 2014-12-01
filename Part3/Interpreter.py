__author__ = 'Janusz'

import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *


class Interpreter(object):


    @on('node')
    def visit(self, node):
        pass

    @when(AST.BinOp)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        # try sth smarter than:
        # if(node.op=='+') return r1+r2
        # elsif(node.op=='-') ...

    @when(AST.RelOp)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        # ...

    @when(AST.Assignment)
    def visit(self, node):
    #
    #

    @when(AST.Const)
    def visit(self, node):
        return node.value

    # simplistic while loop interpretation
    @when(AST.WhileInstr)
    def visit(self, node):
        r = None
        while node.cond.accept(self):
            r = node.body.accept(self)
        return r