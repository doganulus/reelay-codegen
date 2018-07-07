grammar RegExp;

namedExpr : (name=IDENTIFIER '=')? child=expr;

expr : child=binded_atom                          # Atomic
     | 'exists' '{' args=idlist '}' child=expr    # Exists
     | '~' child=expr                             # Complementation
     | child=expr '*'                             # Star
     | child=expr '+'                             # Plus
     | child=expr '?'                             # Question
     | left=expr ';' right=expr                   # Concatenation
     | left=expr '&' right=expr                   # Intersection
     | child=expr '[' '<=' u=NUMBER ']'          # RestrictLT
     | child=expr '[' '>=' l=NUMBER ']'          # RestrictGT
     | child=expr '[' l=NUMBER ',' u=NUMBER ']' # Restrict
     | left=expr '|' right=expr                   # Union
     | '(' child=expr ')'                         # Grouping
     ;

binded_atom : child=atom                         # VarConst
            | varname=IDENTIFIER '<=' child=atom # VarBind
            ;

atom : name=(TYPEDVAR | IDENTIFIER)                    # Prop
     | name=(TYPEDVAR | IDENTIFIER) '(' args=alist ')' # Pred
     | NUMBER                                        # Constant
     ;

alist : atom (',' atom)*                # AtomList
      ;

idlist : IDENTIFIER (',' IDENTIFIER)*;

IDENTIFIER : [_a-zA-Z][_a-zA-Z0-9]*;

TYPEDVAR : IDENTIFIER ':' ('bool' | 'int' | 'int32' |  'float' | 'float64' | 'double' | 'string' ); 

NUMBER : SIGN? NATURAL | SIGN? FLOATING; 

fragment
NATURAL : ZERO | DIGIT_NON_ZERO DIGIT*;

fragment
FLOATING
    :   FRACTIONALCONSTANT EXPONENTPART?
    |   DIGITS EXPONENTPART 
    ;

fragment
FRACTIONALCONSTANT
    :   DIGITS? '.' DIGITS
    |   DIGITS '.'
    ;

fragment
EXPONENTPART
    :   'e' SIGN? DIGITS
    |   'E' SIGN? DIGITS
    ;

fragment SIGN : '+' | '-';
fragment DIGITS : DIGIT+;
fragment DIGIT : ('0'..'9');
fragment DIGIT_NON_ZERO : ('0'..'9');
fragment ZERO : '0';

WS: [ \r\n\t]+ -> channel (HIDDEN);
