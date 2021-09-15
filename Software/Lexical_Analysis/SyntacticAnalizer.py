import ply.yacc as yacc
from Tokenize import tokens
from sys import stdin

precedence = (
    ('right', 'LET'),
    ('right', 'ASSIGN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
)

def p_calc(p):
    '''
    line : variable
         | empty
    '''
    print(p[1])
    
def p_variable(p):
    '''
    variable : LET ID ASSIGN expression SEMICOLON
    '''
    p[0] = (p[3], p[2], p[4])

def p_expression(p):
    '''
    expression : INT
               | TRUE
               | FALSE
    '''
    p[0] = p[1]
    
def p_expression_var(p):
    '''
    expression : ID
    '''
    p[0] = ('let', p[1])

def p_error(p):
    print("Syntax error found!")
    
def p_empty(p):
    '''
    empty :
    '''
    p[0] = None
