import ply.lex as lex
import ply.yacc as yacc
from Software.Syntactic.SyntacticAnalizer import *

def lex_test():
    sourceFile = "../Lexical_Analysis/source.txt"
    if sourceFile is not None:
                with open(sourceFile, 'r') as file:
                    print("Entrando al lexer...")
                    source = file.read()
                    lexer = lex.lex()
                    lexer.input(source)
                    print("Lexer listo")
                    print("Entrando al parser...")
                    parser = yacc.yacc()
                    print("Saliendo del parser...")
                    parser.parse(source)
                    print("TERMINE DE COMPILAR")

    else:
        print("ESTA VACIO")
    for Tok in lexer:
        print(Tok)





