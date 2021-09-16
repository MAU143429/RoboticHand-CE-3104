

# List of reserved words.   This is always required
reserved =  {
    'elseif': 'ELSEIF',
    'else': 'ELSE',
    'if': 'IF',   
    'while': 'WHILE',
    'let': 'LET',
    'for': 'FOR',
    'loop': 'LOOP',
    'fn': 'FN',
    'integer': 'INTEGER',
    'True': 'TRUE',
    'False': 'FALSE',
    'range': 'RANGE',
    'break': 'BREAK',
    'main': 'MAIN',
    'return': 'RETURN',
    'Move': 'MOVE',
    'Delay': 'DELAY',
    'Opera': 'OPERA',
    'Println!': 'PRINT',
    'in': 'IN'
}

# Regular expression rules for literals and simple tokens
t_PLUS              = r'\+'
t_MINUS             = r'-'
t_TIMES             = r'\*'
t_DIVIDE            = r'/'
t_EQEQ              = r'\=='
t_LTE               = r'\<='
t_GTE               = r'\=>'
t_LT                = r'\<'
t_GT                = r'\>'
t_ARROW             = r'\->'
t_LPAREN            = r'\('
t_RPAREN            = r'\)' 
t_ASSIGN            = r'\='
t_COMMA             = r'\,'
t_SEMICOLON         = r'\;'
t_LSQRBRACKET       = r'\['
t_RSQRBRACKET       = r'\]'
t_DOTDOT            = r'\..'
t_QUOT              = r'\"'
t_LCRLBRACKET       = r'\{'
t_RCRLBRACKET       = r'\}'

literals = ['P', 'I', 'M', 'A', 'Q', 'T']
#Token list
tokens = [
'ID',
'INT',
'WRONG_ID',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'EQEQ',
'LTE',
'GTE',
'LT',
'GT',
'ARROW',
'LPAREN',
'RPAREN',
'ASSIGN',
'COMMA',
'SEMICOLON',
'LSQRBRACKET', 
'RSQRBRACKET',
'DOTDOT',
'QUOT',
'LCRLBRACKET',
'RCRLBRACKET'] + list(reserved.values())

