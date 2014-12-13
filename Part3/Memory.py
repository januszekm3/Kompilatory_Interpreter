__author__ = 'Janusz'
# File was downloaded from http://home.agh.edu.pl/~mkuta/tk/zadanie2c/zadanie2C.html

class Memory:

    def __init__(self, name):                       # memory name
        self.name = name
        self.memory = {}

    def has_key(self, name):                        # variable name
        return self.memory.has_key(name)

    def get(self, name):                            # get from memory current value of variable <name>
        return self.memory[name]

    def put(self, name, value):                     # puts into memory current value of variable <name>
        self.memory[name] = value

class MemoryStack:

    def __init__(self, memory=None):                # initialize memory stack with memory <memory>
        self.memoryStack = []
        if (memory != None):
            self.memoryStack.append(memory)

    def get(self, name):                            # get from memory stack current value of variable <name>
        if (len (self.memoryStack) > 0):
            for i in range (len(self.memoryStack)-1, -1, -1):
                if (self.memoryStack[i].has_key(name)):
                    return self.memoryStack[i].get(name)
        else:
            return None

    def insert(self, name, value):                  # inserts into memory stack variable <name> with value <value>
        if (len(self.memoryStack) > 0):
            self.memoryStack[len(self.memoryStack)-1].put(name, value)
        else:
            raise OutOfStackMemoryException

    def set(self, name, value):                     # sets variable <name> to value <value>
        if (len(self.memoryStack) > 0):
            for i in range(len(self.memoryStack)-1, -1, -1):
                if (self.memoryStack[i].has_key(name)):
                    self.memoryStack[i].put(name, value)
                    return True
        return False

    def push(self, memory):                         # push memory <memory> onto the stack
        self.memoryStack.append(memory)

    def pop(self):                                  # pops the top memory from the stack
        self.memoryStack.pop()

class OutOfStackMemoryException(Exception):
    pass