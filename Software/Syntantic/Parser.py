import ply.yacc as yacc
from Keywords import *



syntax_error = False;
semantic_error = False;


def build(lex):


    def p_value(p):
        '''
        value : expresion
              | empty
        '''

    syntactic = yacc.yacc()
