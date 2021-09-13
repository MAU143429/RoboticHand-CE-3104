import sys
import os
from Tokenize import *
from Tokenize import reserved, tokens, literals


t_ignore  = ' \t'
t_ignore_COMMENT  = r'\@.*'
myTokens = tokens
myLiterals = literals
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_FN(t):
    r'fn'
    t.type = 'FN'
    t.value = 'fn'
    return t
def t_ELSEIF(t):
    r'elseif'
    t.type = 'ELSEIF'
    t.value = 'elseif'
    return t
def t_ELSE(t):
    r'else'
    t.type = 'ELSE'
    t.value = 'else'
    return t
def t_IF(t):
    r'if'
    t.type = 'IF'
    t.value = 'if'
    return t





def t_ID(t):
    r'[a-zA-Z_#_?][a-zA-Z_0-9#_?]*'
    if 3 <= len(t.value) < 15:
        t.type = reserved.get(t.value, 'ID')  # Check for reserved words
        return t
    else:
        if str(t.value) in literals:
            t.type = reserved.get(t.value, 'ID')  # Check for reserved words
            return t
        else:
            t.type = "length_err"
            t_error(t)

def t_INT(t):
    r'\d+'
    try:
         t.value = int(t.value)
    except ValueError:
         print ("Line %d: Number %s is too large!" % (t.lineno, t.value))
         t.value = 0
    return t

def t_WRONG_ID(t):
    r'[0-9]+[a-zA-Z_0-9#_?]*'
    t.type = reserved.get(t.value, "WRONG_ID")
    t_error(t)
        
def t_error(t):
    if t.type == "length_err":
        print ("Lexical error at line "+str(t.lexer.lineno)+": ID length must be between 3 and 15")
        t.lexer.skip(1)
    elif t.type == "WRONG_ID":
        print ("Lexical error at line "+str(t.lexer.lineno)+": Identifiers cannot start with a number")
    else:
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
