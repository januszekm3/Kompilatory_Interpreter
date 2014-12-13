import AST


def addToClass(cls):

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Program)
    def printTree(self):
        str = self.decl.__str__() + "\n" + self.fun.__str__() + "\n" + self.instr.__str__()
        str = str.split("\n")
        linesToDelete = []
        for line in str:
            if len(line) == 0:
                linesToDelete.append(line)
            else:
                if line[-1] == " ":
                    linesToDelete.append(line)
        for line in linesToDelete:
            str.remove(line)
        return "\n".join(str)


    @addToClass(AST.Declarations)
    def printTree(self):
        str = "DECL\n"
        for i in self.list:
            istr = i.__str__()
            if istr != "":
                istr = istr.split('\n')
                for line in istr:
                    str += "| " + line + '\n'
        return str


    @addToClass(AST.Declaration)
    def printTree(self):
        return self.inits.__str__()

    @addToClass(AST.Inits)
    def printTree(self):
        str = ""
        for i in self.list:
            str += i.__str__() +'\n'
        return str

    @addToClass(AST.Init)
    def printTree(self):
        str = "=\n"
        str += "| " + self.name.__str__() + "\n"
        str += "| " + self.value.__str__() + "\n"
        return str

    @addToClass(AST.FunDefs)
    def printTree(self):
        str = ""
        for i in self.list:
            istr = i.__str__()
            if istr != "":
                str += istr + '\n'
        return str

    @addToClass(AST.FunDef)
    def printTree(self):
        str = "FUNDEF\n"
        str += "| " + self.name.__str__() + '\n'
        str += "| RET " + self.type.__str__() + '\n'
        for line in self.args.__str__().split('\n'):
            str += "| " + line + '\n'
        for line in self.instr.__str__().split('\n'):
            str += "| " + line + '\n'
        return str

    @addToClass(AST.ArgsList)
    def printTree(self):
        str = ""
        for i in self.list:
            str += i.__str__() + '\n'
        return str

    @addToClass(AST.Arg)
    def printTree(self):
        return "ARG " + self.name.__str__()


    @addToClass(AST.CompoundInstr)
    def printTree(self):
        return self.decl.__str__() + "\n" + self.instr.__str__() + "\n"


    @addToClass(AST.Instructions)
    def printTree(self):
        str = ""
        for i in self.list:
            str += i.__str__() + '\n'
        return str


    @addToClass(AST.IfInstr)
    def printTree(self):
        str = "IF\n"
        for line in self.cond.__str__().split('\n'):
            str += "| " + line + '\n'
        for line in self.instr.__str__().split('\n'):
            str += "| " + line + '\n'
        return str

    @addToClass(AST.IfElseInstr)
    def printTree(self):
        str = "IF\n"
        for line in self.cond.__str__().split('\n'):
            str += "| " + line + '\n'
        for line in self.instr.__str__().split('\n'):
            str += "| " + line + '\n'
        str += "ELSE\n"
        for line in self.elseinstr.__str__().split('\n'):
            str += "| " + line + '\n'
        return str

    @addToClass(AST.Condition)
    def printTree(self):
        return self.expr.__str__()

    @addToClass(AST.BinExpr)
    def printTree(self):
        str = self.op.__str__() + "\n"
        for line in self.left.__str__().split('\n'):
            str += "| " + line + "\n"
        for line in self.right.__str__().split('\n'):
            str += "| " + line + "\n"
        return str

    @addToClass(AST.Assignment)
    def printTree(self):
        str = "=\n"
        str += "| " + self.name.__str__() + "\n"
        for line in self.expr.__str__().split('\n'):
            str += "| " + line + '\n'
        return str

    @addToClass(AST.FunCall)
    def printTree(self):
        str = "FUNCALL\n"
        str += "| " + self.name.__str__() + "\n"
        for line in self.args.__str__().split('\n'):
            str += "| " + line + '\n'
        return str

    @addToClass(AST.ExprList)
    def printTree(self):
        str = ""
        for i in self.list:
            str += i.__str__() + '\n'
        return str

    @addToClass(AST.PrintInstr)
    def printTree(self):
        str = "PRINT\n"
        str += "| " + self.expr.__str__() + "\n"
        return str


    @addToClass(AST.ReturnInstr)
    def printTree(self):
        str = "RETURN\n"
        str += "| " + self.expr.__str__() + "\n"
        return str

    @addToClass(AST.BrackExpr)
    def printTree(self):
        return self.expr.__str__()

    @addToClass(AST.UnExpr)
    def printTree(self):
        return self.expr.__str__()

    @addToClass(AST.Const)
    def printTree(self):
        return self.value.__str__()


    @addToClass(AST.Epsilon)
    def printTree(self):
        return ""

    @addToClass(AST.ContinueInstr)
    def printTree(self):
        return "CONTINUE"

    @addToClass(AST.BreakInstr)
    def printTree(self):
        return "BREAK"

    @addToClass(AST.LabeledInstr)
    def printTree(self):
        str = self.name.__str__() + "\n"
        str += "| " + str.instr.__str__() + "\n"
        return str

    @addToClass(AST.WhileInstr)
    def printTree(self):
        str = "WHILE\n"
        for line in self.cond.__str__().split('\n'):
            str += "| " + line + "\n"
        for line in self.instr.__str__().split('\n'):
            str += "| " + line + "\n"
        return str

    @addToClass(AST.RepeatInstr)
    def printTree(self):
        str = "REPEAT\n"
        for line in self.instr.__str__().split('\n'):
            str += "| " + line + "\n"
        str += "UNTIL\n"
        for line in self.cond.__str__().split('\n'):
            str += "| " + line + "\n"
        return str
