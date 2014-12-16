#!/usr/bin/python
class Symbol(object):
    pass

class FunctionSymbol(Symbol):

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.argtypes = []

class VariableSymbol(Symbol):

    def __init__(self, name, type):
        self.name = name
        self.type = type

class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.scope = {}

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        self.scope[name] = symbol

    def get(self, name): # get variable symbol or fundef from <name> entry
        if name in self.scope:
            return self.scope[name]
        else:
            return None

    def getParentScope(self):
        if self.parent is None:
            return None
        else:
            return self.parent