import ply.lex as lex
import ply.yacc as yacc
from Software.Syntactic.SyntacticAnalizer import *


def lex_test():
    sourceFile = "../Lexical_Analysis/source.txt"
    if sourceFile is not None:
        with open(sourceFile, 'r') as file:
            print("Entrando al lexer...")
            try:
                source = file.read()
            except EOFError as e:
                print(e)

            lexer = lex.lex()
            lexer.input(source)
            clone = lexer.clone()
            clone.input(source)

            for token in clone:

                myTable.insertToken(token.type, token.value)

            parser = yacc.yacc()
            parser.parse(source)
            print("Saliendo del parser...")
            print("TERMINE DE COMPILAR")
            print(" \n *********** ERRORES DE COMPILACION *********** \n")
            error = ErrorLog()
            error.print()
            print(" \n ******************* FIN ********************** \n")

    else:
        print("ESTA VACIO")
    for Tok in lexer:
        print(Tok)

lex_test()
