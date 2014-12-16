
import sys
import ply.yacc as yacc
from Part1.Cparser import Cparser as Cparser
from TypeChecker import TypeChecker

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\fact.in"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\fib.in"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\funcdef.in"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\gcd.in"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\if.in"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\ifelse.in"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\loops.in"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\primes.in"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\scopes.in"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    Cparser = Cparser()
    parser = yacc.yacc(module=Cparser)
    text = file.read()
    ast = parser.parse(text, lexer=Cparser.scanner)
    typeChecker = TypeChecker()
    typeChecker.visit(ast)   # or alternatively ast.accept(typeChecker)

