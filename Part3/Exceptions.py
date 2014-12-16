__author__ = 'Janusz'
# File was downloaded from http://home.agh.edu.pl/~mkuta/tk/zadanie2c/zadanie2C.html without any changes

class ReturnValueException(Exception):
    def __init__(self, value):
        self.value = value
        
class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass
