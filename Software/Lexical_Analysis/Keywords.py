class Keywords:
    def __init__(self):
        self.reserved = self.getReserved()
        self.literals = self.getLiterals()
        self.tokens = self.getTokens() + tuple(self.reserved.values())
        
    def getReserved(self):
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

        }
        return reserved
    def getTokens(self):
        tokens = (
            'INT',
            'EQEQ',
            'ARROW',
            'POINTS',
            'ID',
            )
        return tokens
    def getLiterals(self):
        literals = ['{', '}', ';', '(', ')', '+', '-', '*', '/', '=', '<', '>']
        return literals
    def getArrowRule(self):
        arrowRule = r'\=='
        return arrowRule
    def getEqEqRule(self):
        EqEqRule = r'\->'
        return EqEqRule
    def getDotsRule(self):
        DotsRule = r'\..'
        return DotsRule

