__author__ = 'Janusz'
# File was downloaded from http://home.agh.edu.pl/~mkuta/tk/zadanie2c/zadanie2C.html

import sys
import ply.yacc as yacc
from Part1.Cparser import Cparser
from Interpreter import Interpreter
import os

if __name__ == '__main__':
    os.sys.setrecursionlimit(5000)

    try:
        #filename = sys.argv[1] if len(sys.argv) > 1 else "acceptance_test.py"          #bangla
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\fact.in"          #nie bangla
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\fib.in"           #nie bangla
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\funcdef.in"       #nie bangla
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\gcd.in"           #nie bangla
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\if.in"            #bangla
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\ifelse.in"        #bangla
        filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\loops.in"         #nie bangla
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\primes.in"        #nie bangla
        #filename = sys.argv[1] if len(sys.argv) > 1 else "..\\tests\\scopes.in"        #nie bangla
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    Cparser = Cparser()
    parser = yacc.yacc(module=Cparser)
    text = file.read()

    ast = parser.parse(text, lexer=Cparser.scanner)
    if ast:
        ast.accept(Interpreter())
        print "\nInterpretation finished\n"
    else:
        print "\nSyntax check failed\n"