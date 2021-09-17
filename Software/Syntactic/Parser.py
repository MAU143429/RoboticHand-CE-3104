import ply.yacc as yacc
from Software.Lexical_Analysis.Tokenize import *



syntax_error = False;
semantic_error = False;


def build(lex):


    def p_value(p):
        '''
        value : expresion
              | empty
        '''

    syntactic = yacc.yacc()
