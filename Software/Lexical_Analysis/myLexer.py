import ply.lex as lex

from LexicalAnalizer import *

sourceFile = "Software/Lexical_Analysis/source.txt"
def lex_test(sourceFile):
    lexer = lex.lex()
    if sourceFile is not None:
                with open(sourceFile) as file:
                    source = file.read()
                    lexer.input(source)
    for Tok in lexer:
        print(Tok)

lex_test(sourceFile)
    