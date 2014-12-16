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
        self.memory_stack = defaultdict(lambda: Memory(self.memory_stack[0]))
        self.memory_stack[0] = Memory()

    def get_scope(self, scope):
        hash = self.memory_stack.keys()[-1]

        while hash in self.memory_stack.keys():
            hash = hash + 1

        self.memory_stack[hash] = Memory(self.memory_stack[scope])
        return hash

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
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        return optype[node.op](r1, r2)

    @when(AST.UnExpr)
    def visit(self, node, scope=0):
        return node.accept(self)