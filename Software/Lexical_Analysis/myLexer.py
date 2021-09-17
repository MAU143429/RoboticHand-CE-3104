import ply.lex as lex
import ply.yacc as yacc
from Software.Syntactic.SyntacticAnalizer import *

def lex_test():
    sourceFile = "source.txt"
    if sourceFile is not None:
                with open(sourceFile) as file:
                    source = file.read()
                    lexer.input(source)
                    parser.parse(source)
                    print("TERMINE DE COMPILAR")

    else:
        print("ESTA VACIO")
    for Tok in lexer:
        print(Tok)





