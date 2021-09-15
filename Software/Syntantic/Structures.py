import ply.yacc as yacc
from


def p_structure_let(p):
    '''
        structure: LET ID = expression;
    '''

