class Node(object):
    def __str__(self):
        return self.printTree()

class Const(Node):
    def __init__(self, value):
        self.value = value

class Expr(Node):
    pass

class BinExpr(Expr):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class UnExpr(Expr):
    def __init__(self, expr):
        self.expr = expr

class FunCall(Expr):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class BrackExpr(Expr):
    def __init__(self, expr):
        self.expr = expr

class Init(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Inits(Node):
    def __init__(self, *list):
        self.list = list

class Declaration(Node):
    def __init__(self, inits):
        self.inits = inits

class Declarations(Node):
    def __init__(self, *list):
        self.list = list

class Epsilon(Node):
    def __init__(self):
        pass

class Arg(Node):
    def __init__(self, name):
        self.name = name

class ArgsList(Node):
    def __init__(self, *list):
        self.list = list

class Condition(Node):
    def __init__(self, expr):
        self.expr = expr

class ExprList(Node):
    def __init__(self, *list):
        self.list = list

class Instruction(Node):
    pass

class PrintInstr(Instruction):
    def __init__(self, expr):
        self.expr = expr

class Assignment(Instruction):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class ReturnInstr(Instruction):
    def __init__(self, expr):
        self.expr = expr

class ContinueInstr(Instruction):
    def __init__(self,):
        pass

class BreakInstr(Instruction):
    def __init__(self):
        pass

class LabeledInstr(Instruction):
    def __init__(self, name, instr):
        self.name = name
        self.instr = instr

class ChoiceInstruction(Instruction):
    pass

class IfInstr(ChoiceInstruction):
    def __init__(self, cond, instr):
        self.cond = cond
        self.instr = instr

class IfElseInstr(ChoiceInstruction):
    def __init__(self, cond, instr, elseinstr):
        self.cond = cond
        self.instr = instr
        self.elseinstr = elseinstr

class Instructions(Instruction):
    def __init__(self, *list):
        self.list = list

class WhileInstr(Instruction):
    def __init__(self, cond, instr):
        self.cond = cond
        self.instr = instr

class RepeatInstr(Instruction):
    def __init__(self, instr, cond):
        self.cond = cond
        self.instr = instr

class CompoundInstr(Instruction):
    def __init__(self, decl, instr):
        self.decl = decl
        self.instr = instr

class FunDef(Node):
    def __init__(self, type, name, args, instr):
        self.type = type
        self.name = name
        self.args = args
        self.instr = instr

class FunDefs(Node):
    def __init__(self, fundef, fundefs):
        self.list = [fundef, fundefs]

class Program(Node):
    def __init__(self, decl, fun, instr):
        self.decl = decl
        self.fun = fun
        self.instr = instr

class Integer(Const):
    pass
    #...


class Float(Const):
    pass
    #...


class String(Const):
    pass
    #...


class Variable(Node):
    pass
    #...

# ...