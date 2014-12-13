__author__ = 'Janusz'
# File was downloaded from http://home.agh.edu.pl/~mkuta/tk/zadanie2c/zadanie2C.html without any changes

import sys
import ply.yacc as yacc
from Part1.Cparser import Cparser as Cparser
from TypeChecker import TypeChecker
from Interpreter import Interpreter

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "acceptance_test.py"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    Cparser = Cparser()
    parser = yacc.yacc(module=Cparser)
    text = file.read()
    parser.parse(text, lexer=Cparser.scanner)

    ast = parser.parse(text, lexer=Cparser.scanner)
    ast.accept(TypeChecker())

    # jesli wizytor TypeChecker z implementacji w poprzednim lab korzystal z funkcji accept
    # to nazwa tej ostatniej dla Interpretera powinna zostac zmieniona, np. na accept2 ( ast.accept2(Interpreter()) )
    # tak aby rozne funkcje accept z roznych implementacji wizytorow nie kolidowaly ze soba
    ast.accept(Interpreter())

    # in future
    # ast.accept(OptimizationPass1())
    # ast.accept(OptimizationPass2())
    # ast.accept(CodeGenerator())

    if ast == None:
        sys.exit(-1)

    try:
        ast.printTree(0)
        semantic_errors_found = TypeChecker().dispatch(ast)
        if not semantic_errors_found:
            ast.accept(Interpreter())
    except Exception:
        print "Error while printing tree or performing type-check caused by previous syntax errors."