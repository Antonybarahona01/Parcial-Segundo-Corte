grammar Funciones;
prog:   stat+ ;

stat:   mapFunction NEWLINE                                     
    |   filterFunction NEWLINE                                  
    ;
mapFunction: 'map' '(' opcion ',' iterable ')';

filterFunction: 'filter' '(' expression ',' iterable ')';

expression: arith_expression_comp
          | len_expression
          | id_expression
          ;


opcion:    arith_expression2
          | len_expression2
          | index_expression
          | capitalize_expression
          ;

arith_expression2: term2 ((ADD | SUB | MUL | DIV | MOD | POW) term2)*;

term2: factor2 ((ADD | SUB | MUL | DIV | MOD | POW) factor2)*;

factor2: (ADD | SUB | MUL | DIV | MOD | POW) factor | atom2;

atom2: ID | INT | FLOAT | STRING | '(' opcion ')';

len_expression2: 'len' '(' ID ')';

index_expression: ID '[' INT ']';

capitalize_expression: ID '.'  '(' ID ')';




arith_expression_comp: arith_expression comp_operator arith_expression ;

len_expression: 'len' '(' ID ')' comp_operator INT ;

id_expression: ID comp_operator INT ;

arith_expression: term ((ADD | SUB | '%') term)*;

term: factor ((MUL | DIV) factor)*;

factor: (ADD | SUB) factor | atom;

atom: ID | INT | FLOAT | STRING | '(' expression ')';

comp_operator: '==' | '!=' | '<' | '<=' | '>' | '>=';

                                   


iterable:list|tuple; 
list: '[' elements? ']';
tuple: '(' elements? ')';
elements: expr (',' expr)* ;
expr: INT | FLOAT | STRING ;
INT: [0-9]+;
ID: [a-zA-Z]+;
FLOAT: [0-9]+'.'[0-9]+;
STRING: ('"' .*? '"') ;
MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
MOD: '%';   
POW: '**';
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
