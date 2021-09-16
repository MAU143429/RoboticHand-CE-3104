from Software.Lexical_Analysis.Tokenize import tokens
from Software.Semantic.Structures_Models import *
from sys import stdin

precedence = (
    ('right', 'LET'),
    ('right', 'ASSIGN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
)
def p_main(p):
    '''
    main : FN MAIN LCRLBRACKET line RCRLBRACKET
    '''

def p_program(p):
    '''
    line : variable
         | for
         | move
         | delay
         | empty
    '''

def p_variable(p):
    '''
    variable : LET ID ASSIGN expression SEMICOLON line
    '''
    line = p.lineno(2)
    p[0] = Let(p[2], p[4], line)

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

def p_for(p):
    '''
    for : FOR ID IN INT DOTDOT INT LCRLBRACKET line RCRLBRACKET
    '''

def p_move(p):
    '''
    move : MOVE LPAREN  RPAREN
    '''

def p_delay(p):
    '''
    delay : DELAY line
    '''
    p[0] = (p[3], p[2], p[4])

def p_error(p):
    print("Syntax error found!", p)
    print("Error on line " + str(p.lineno))
    
def p_empty(p):
    '''
    empty :
    '''
    pass
    #p[0] = None
