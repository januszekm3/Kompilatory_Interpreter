__author__ = 'Janusz'

class Node:

    def accept(self, visitor):
        return visitor.visit(self)