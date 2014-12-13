__author__ = 'Janusz'
# File was downloaded from http://home.agh.edu.pl/~mkuta/tk/zadanie2c/zadanie2C.html

class Node:

    def accept(self, visitor):
        return visitor.visit(self)