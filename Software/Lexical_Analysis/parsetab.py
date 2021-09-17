
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightLETrightASSIGNleftPLUSMINUSleftTIMESDIVIDEleftLPARENRPARENA ARROW ASSIGN ASTR BREAK COMMA DELAY DIVIDE DOTDOT ELSE ELSEIF EQEQ EXPR FALSE FN FOR GT GTE I ID IF IN INT INTEGER LCRLBRACKET LET LOOP LPAREN LSQRBRACKET LT LTE M MAIN MIL MIN MINUS MOVE OPERA P PLUS PRINT Q QUOT RANGE RCRLBRACKET RETURN RPAREN RSQRBRACKET SEG SEMICOLON T TIMES TRUE WHILE WRONG_ID\n    main : FN MAIN LPAREN RPAREN LCRLBRACKET line RCRLBRACKET\n    \n    line : loop\n         | for\n         | let\n         | move\n         | delay\n         | println\n         | opera\n         | empty\n    \n    loop : LOOP LCRLBRACKET line RCRLBRACKET line\n    \n    for : FOR ID IN INT DOTDOT INT LCRLBRACKET line RCRLBRACKET line\n    \n    move : MOVE LPAREN QUOT ID QUOT COMMA expression RPAREN SEMICOLON line\n    \n    finger : P\n           | I\n           | M\n           | A\n           | Q\n           | T\n    \n    delay : DELAY LPAREN INT COMMA unit RPAREN SEMICOLON line\n    \n    unit : QUOT MIN QUOT\n         | QUOT MIL QUOT\n         | QUOT SEG QUOT\n    \n    println : PRINT EXPR LPAREN QUOT text QUOT RPAREN SEMICOLON line\n\n    \n    text : ID\n\n    \n    opera : OPERA LPAREN operator COMMA operand COMMA operand RPAREN SEMICOLON line\n          | OPERA LPAREN operator COMMA operand COMMA operand RPAREN\n    \n    operator : PLUS\n             | MINUS\n             | DIVIDE\n             | ASTR\n             | TIMES\n    \n    operand : INT\n            | ID\n            | opera\n    \n    let : LET ID ASSIGN INT SEMICOLON line\n             | LET ID ASSIGN expression SEMICOLON line\n    \n    expression : TRUE\n               | FALSE\n               | ID\n    \n    empty :\n    '
    
_lr_action_items = {'FN':([0,],[2,]),'$end':([1,23,],[0,-1,]),'MAIN':([2,],[3,]),'LPAREN':([3,19,20,22,29,],[4,27,28,30,36,]),'RPAREN':([4,8,9,10,11,12,13,14,15,43,45,48,49,54,56,57,59,64,65,66,68,69,75,78,79,80,81,82,84,87,88,89,90,91,92,93,94,95,96,],[5,-2,-3,-4,-5,-6,-7,-8,-9,-40,-39,-37,-38,-10,-40,-40,71,-32,-33,-34,-35,-36,83,86,-40,-20,-21,-22,89,-19,-40,-26,-40,-40,-23,-40,-11,-12,-25,]),'LCRLBRACKET':([5,16,67,],[6,24,77,]),'LOOP':([6,24,43,56,57,77,79,88,90,91,93,],[16,16,16,16,16,16,16,16,16,16,16,]),'FOR':([6,24,43,56,57,77,79,88,90,91,93,],[17,17,17,17,17,17,17,17,17,17,17,]),'LET':([6,24,43,56,57,77,79,88,90,91,93,],[18,18,18,18,18,18,18,18,18,18,18,]),'MOVE':([6,24,43,56,57,77,79,88,90,91,93,],[19,19,19,19,19,19,19,19,19,19,19,]),'DELAY':([6,24,43,56,57,77,79,88,90,91,93,],[20,20,20,20,20,20,20,20,20,20,20,]),'PRINT':([6,24,43,56,57,77,79,88,90,91,93,],[21,21,21,21,21,21,21,21,21,21,21,]),'OPERA':([6,24,43,53,56,57,76,77,79,88,90,91,93,],[22,22,22,22,22,22,22,22,22,22,22,22,22,]),'RCRLBRACKET':([6,7,8,9,10,11,12,13,14,15,24,31,43,54,56,57,68,69,77,79,85,87,88,89,90,91,92,93,94,95,96,],[-40,23,-2,-3,-4,-5,-6,-7,-8,-9,-40,43,-40,-10,-40,-40,-35,-36,-40,-40,90,-19,-40,-26,-40,-40,-23,-40,-11,-12,-25,]),'COMMA':([8,9,10,11,12,13,14,15,35,37,38,39,40,41,42,43,54,56,57,58,63,64,65,66,68,69,79,87,88,89,90,91,92,93,94,95,96,],[-2,-3,-4,-5,-6,-7,-8,-9,51,53,-27,-28,-29,-30,-31,-40,-10,-40,-40,70,76,-32,-33,-34,-35,-36,-40,-19,-40,-26,-40,-40,-23,-40,-11,-12,-25,]),'ID':([17,18,33,34,52,53,70,76,],[25,26,45,50,62,65,45,65,]),'EXPR':([21,],[29,]),'IN':([25,],[32,]),'ASSIGN':([26,],[33,]),'QUOT':([27,36,50,51,61,62,72,73,74,],[34,52,58,60,75,-24,80,81,82,]),'INT':([28,32,33,53,55,76,],[35,44,46,64,67,64,]),'PLUS':([30,],[38,]),'MINUS':([30,],[39,]),'DIVIDE':([30,],[40,]),'ASTR':([30,],[41,]),'TIMES':([30,],[42,]),'TRUE':([33,70,],[48,48,]),'FALSE':([33,70,],[49,49,]),'DOTDOT':([44,],[55,]),'SEMICOLON':([45,46,47,48,49,71,83,86,89,],[-39,56,57,-37,-38,79,88,91,93,]),'MIN':([60,],[72,]),'MIL':([60,],[73,]),'SEG':([60,],[74,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main':([0,],[1,]),'line':([6,24,43,56,57,77,79,88,90,91,93,],[7,31,54,68,69,85,87,92,94,95,96,]),'loop':([6,24,43,56,57,77,79,88,90,91,93,],[8,8,8,8,8,8,8,8,8,8,8,]),'for':([6,24,43,56,57,77,79,88,90,91,93,],[9,9,9,9,9,9,9,9,9,9,9,]),'let':([6,24,43,56,57,77,79,88,90,91,93,],[10,10,10,10,10,10,10,10,10,10,10,]),'move':([6,24,43,56,57,77,79,88,90,91,93,],[11,11,11,11,11,11,11,11,11,11,11,]),'delay':([6,24,43,56,57,77,79,88,90,91,93,],[12,12,12,12,12,12,12,12,12,12,12,]),'println':([6,24,43,56,57,77,79,88,90,91,93,],[13,13,13,13,13,13,13,13,13,13,13,]),'opera':([6,24,43,53,56,57,76,77,79,88,90,91,93,],[14,14,14,66,14,14,66,14,14,14,14,14,14,]),'empty':([6,24,43,56,57,77,79,88,90,91,93,],[15,15,15,15,15,15,15,15,15,15,15,]),'operator':([30,],[37,]),'expression':([33,70,],[47,78,]),'unit':([51,],[59,]),'text':([52,],[61,]),'operand':([53,76,],[63,84,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> FN MAIN LPAREN RPAREN LCRLBRACKET line RCRLBRACKET','main',7,'p_main','SyntacticAnalizer.py',17),
  ('line -> loop','line',1,'p_program','SyntacticAnalizer.py',22),
  ('line -> for','line',1,'p_program','SyntacticAnalizer.py',23),
  ('line -> let','line',1,'p_program','SyntacticAnalizer.py',24),
  ('line -> move','line',1,'p_program','SyntacticAnalizer.py',25),
  ('line -> delay','line',1,'p_program','SyntacticAnalizer.py',26),
  ('line -> println','line',1,'p_program','SyntacticAnalizer.py',27),
  ('line -> opera','line',1,'p_program','SyntacticAnalizer.py',28),
  ('line -> empty','line',1,'p_program','SyntacticAnalizer.py',29),
  ('loop -> LOOP LCRLBRACKET line RCRLBRACKET line','loop',5,'p_loop','SyntacticAnalizer.py',39),
  ('for -> FOR ID IN INT DOTDOT INT LCRLBRACKET line RCRLBRACKET line','for',10,'p_for','SyntacticAnalizer.py',52),
  ('move -> MOVE LPAREN QUOT ID QUOT COMMA expression RPAREN SEMICOLON line','move',10,'p_move','SyntacticAnalizer.py',64),
  ('finger -> P','finger',1,'p_finger','SyntacticAnalizer.py',71),
  ('finger -> I','finger',1,'p_finger','SyntacticAnalizer.py',72),
  ('finger -> M','finger',1,'p_finger','SyntacticAnalizer.py',73),
  ('finger -> A','finger',1,'p_finger','SyntacticAnalizer.py',74),
  ('finger -> Q','finger',1,'p_finger','SyntacticAnalizer.py',75),
  ('finger -> T','finger',1,'p_finger','SyntacticAnalizer.py',76),
  ('delay -> DELAY LPAREN INT COMMA unit RPAREN SEMICOLON line','delay',8,'p_delay','SyntacticAnalizer.py',88),
  ('unit -> QUOT MIN QUOT','unit',3,'p_unit','SyntacticAnalizer.py',95),
  ('unit -> QUOT MIL QUOT','unit',3,'p_unit','SyntacticAnalizer.py',96),
  ('unit -> QUOT SEG QUOT','unit',3,'p_unit','SyntacticAnalizer.py',97),
  ('println -> PRINT EXPR LPAREN QUOT text QUOT RPAREN SEMICOLON line','println',9,'p_println','SyntacticAnalizer.py',107),
  ('text -> ID','text',1,'p_text','SyntacticAnalizer.py',115),
  ('opera -> OPERA LPAREN operator COMMA operand COMMA operand RPAREN SEMICOLON line','opera',10,'p_opera','SyntacticAnalizer.py',127),
  ('opera -> OPERA LPAREN operator COMMA operand COMMA operand RPAREN','opera',8,'p_opera','SyntacticAnalizer.py',128),
  ('operator -> PLUS','operator',1,'p_operators','SyntacticAnalizer.py',135),
  ('operator -> MINUS','operator',1,'p_operators','SyntacticAnalizer.py',136),
  ('operator -> DIVIDE','operator',1,'p_operators','SyntacticAnalizer.py',137),
  ('operator -> ASTR','operator',1,'p_operators','SyntacticAnalizer.py',138),
  ('operator -> TIMES','operator',1,'p_operators','SyntacticAnalizer.py',139),
  ('operand -> INT','operand',1,'p_operand','SyntacticAnalizer.py',145),
  ('operand -> ID','operand',1,'p_operand','SyntacticAnalizer.py',146),
  ('operand -> opera','operand',1,'p_operand','SyntacticAnalizer.py',147),
  ('let -> LET ID ASSIGN INT SEMICOLON line','let',6,'p_let','SyntacticAnalizer.py',159),
  ('let -> LET ID ASSIGN expression SEMICOLON line','let',6,'p_let','SyntacticAnalizer.py',160),
  ('expression -> TRUE','expression',1,'p_expression_bool','SyntacticAnalizer.py',168),
  ('expression -> FALSE','expression',1,'p_expression_bool','SyntacticAnalizer.py',169),
  ('expression -> ID','expression',1,'p_expression_bool','SyntacticAnalizer.py',170),
  ('empty -> <empty>','empty',0,'p_empty','SyntacticAnalizer.py',182),
]
