class Node(object):
    def accept(self, visitor):
        return visitor.visit(self)

    def __init__(self):
        self.children = ()

    # def __str__(self):
    #     return self.printTree()

class Const(Node):
    pass

class Integer(Const):
    def __init__(self, line, value):
        self.value = value
        self.line = line

        self.children = ()

class Float(Const):
    def __init__(self, line, value):
        self.value = value
        self.line = line

        self.children = ()

class String(Const):
    def __init__(self, line, value):
        self.value = value
        self.line = line

        self.children = ()

class Expr(Node):
    pass

class BinExpr(Expr):
    def __init__(self, line, op, left, right):
        self.op = op
        self.left = left
        self.right = right
        self.line = line

        self.children = ( left, right )

class UnExpr(Expr):
    def __init__(self, line, expr):
        self.expr = expr
        self.line = line

        self.children = ( expr )

class FunCall(Expr):
    def __init__(self, line, name, args):
        self.name = name
        self.args = args
        self.line = line

        self.children = ( args )

class BrackExpr(Expr):
    def __init__(self, line, expr):
        self.expr = expr
        self.line = line

        self.children = ( expr )

class Init(Node):
    def __init__(self, line, name, value):
        self.name = name
        self.value = value
        self.line = line

        self.children = ( value )

class Inits(Node):
    def __init__(self, line, *list):
        self.list = list
        self.line = line

        self.children = ( list )

class Declaration(Node):
    def __init__(self, line, inits, type):
        self.inits = inits
        self.type = type
        self.line = line

        self.children = ( inits )

class Declarations(Node):
    def __init__(self, line, *list):
        self.list = list
        self.line = line

        self.children = ( list )

class Epsilon(Node):
    def __init__(self, line):
        self.children = ()
        self.line = line

class Arg(Node):
    def __init__(self, line, name, type):
        self.name = name
        self.type = type
        self.line = line

        self.children = ()

class ArgsList(Node):
    def __init__(self, line, *list):
        self.list = list
        self.line = line

        self.children = ( list )

class Condition(Node):
    def __init__(self, line, expr):
        self.expr = expr
        self.line = line

        self.children = ( expr )

class ExprList(Node):
    def __init__(self, line, *list):
        self.list = list
        self.line = line

        self.children = ( list )

class Instruction(Node):
    pass

class PrintInstr(Instruction):
    def __init__(self, line, expr):
        self.expr = expr
        self.line = line

        self.children = ( expr )

class Assignment(Instruction):
    def __init__(self, line, name, expr):
        self.name = name
        self.expr = expr
        self.line = line

        self.children = ( expr )

class ReturnInstr(Instruction):
    def __init__(self, line, expr):
        self.expr = expr
        self.line = line

        self.children = ( expr )

class ContinueInstr(Instruction):
    def __init__(self, line):
        self.line = line
        self.children = ()

class BreakInstr(Instruction):
    def __init__(self, line):
        self.line = line
        self.children = ()

class LabeledInstr(Instruction):
    def __init__(self, line, name, instr):
        self.name = name
        self.instr = instr
        self.line = line

        self.children = ( instr )

class ChoiceInstruction(Instruction):
    pass

class IfInstr(ChoiceInstruction):
    def __init__(self, line, cond, instr):
        self.cond = cond
        self.instr = instr
        self.line = line

        self.children = ( cond, instr )

class IfElseInstr(ChoiceInstruction):
    def __init__(self, line, cond, instr, elseinstr):
        self.cond = cond
        self.instr = instr
        self.elseinstr = elseinstr
        self.line = line

        self.children = ( cond, instr, elseinstr )

class Instructions(Instruction):
    def __init__(self, line, *list):
        self.list = list
        self.line = line

        self.children = ( list )

class WhileInstr(Instruction):
    def __init__(self, line, cond, instr):
        self.cond = cond
        self.instr = instr
        self.line = line

        self.children = ( cond, instr )

class RepeatInstr(Instruction):
    def __init__(self, line, instr, cond):
        self.cond = cond
        self.instr = instr
        self.line = line

        self.children = ( cond, instr )

class CompoundInstr(Instruction):
    def __init__(self, line, decl, instr):
        self.decl = decl
        self.instr = instr
        self.line = line

        self.children = ( decl, instr )

class FunDef(Node):
    def __init__(self, line, type, name, args, instr):
        self.type = type
        self.name = name
        self.args = args
        self.instr = instr
        self.line = line

        self.children = ( args, instr )

class FunDefs(Node):
    def __init__(self, line, fundef, fundefs):
        self.list = [fundef, fundefs]
        self.line = line

        self.children = ( list )

class Program(Node):
    def __init__(self, line, decl, fun, instr):
        self.decl = decl
        self.fun = fun
        self.instr = instr
        self.line = line

        self.children = ( decl, fun, instr )

class Variable(Node):
    pass