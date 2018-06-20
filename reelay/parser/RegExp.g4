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
     | child=expr '[' '<=' u=NATURAL ']'          # RestrictLT
     | child=expr '[' '>=' l=NATURAL ']'          # RestrictGT
     | child=expr '[' l=NATURAL ',' u=NATURAL ']' # Restrict
     | left=expr '|' right=expr                   # Union
     | '(' child=expr ')'                         # Grouping
     ;

binded_atom : child=atom                         # VarConst
            | varname=IDENTIFIER '<=' child=atom # VarBind
            ;

atom : name=(TYPEDVAR | IDENTIFIER)                    # Prop
     | name=(TYPEDVAR | IDENTIFIER) '(' args=alist ')' # Pred
     | CONSTANT                                        # Constant
     ;

alist : atom (',' atom)*                # AtomList
      ;

idlist : IDENTIFIER (',' IDENTIFIER)*;

IDENTIFIER : [a-zA-Z][_a-zA-Z0-9]*;

TYPEDVAR : IDENTIFIER ':' ('bool' | 'int' | 'int32' |  'float' | 'float64' | 'double' | 'string' ); 

CONSTANT : SIGN? NATURAL | SIGN? FLOATING; 

NATURAL
    :   DIGITS
    ;

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

WS: [ \r\n\t]+ -> channel (HIDDEN);
