import ply.lex as lex
import ply.yacc as yacc
from Software.Syntactic.SyntacticAnalizer import *

#sourceFile = "source.txt"
def lex_test(sourceFile):
    print("ME LLEGO EL PATH")
    lexer = lex.lex()
    parser = yacc.yacc()
    print("CREE INSTANCIAS DE LEX Y YACC")
    print("VERIFICARE QUE NO ESTA VACIO el ----> " + sourceFile)
    if sourceFile is not None:
                with open(sourceFile) as file:
                    source = file.read()

                    lexer.input(source)
                    parser.parse(source)
    else:
        print("ESTA VACIO")
    for Tok in lexer:
        print(Tok)


#lex_test(sourceFile)


