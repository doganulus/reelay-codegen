grammar PastTL;

namedExpr : (name=IDENTIFIER '=')? child=expr;

expr : child=binded_atom                                            # Atomic
     | 'exists' '{' args=idlist '}' child=expr                      # Exists
     | ('!' | 'not') child=expr                                     # Negation
     | left=expr ('&&' | 'and') right=expr                          # Conjunction           
     | left=expr ('||' | 'or') right=expr                           # Disjunction
     | left=expr ('->' | 'implies') right=expr                      # Implication
     | 'pre' child=expr                                             # Previous
     | 'once' child=expr                                            # Once
     | 'once' '[' '>=' l=NUMBER ']' child=expr                      # TimedOnceGT
     | 'once' '[' '<=' u=NUMBER ']' child=expr                      # TimedOnceLT
     | 'once' '[' l=NUMBER ',' u=NUMBER ']' child=expr              # TimedOnce
     | 'always' child=expr                                          # Always
     | 'always' '[' '>=' l=NUMBER ']' child=expr                    # TimedAlwaysGT
     | 'always' '[' '<=' u=NUMBER ']' child=expr                    # TimedAlwaysLT
     | 'always' '[' l=NUMBER ',' u=NUMBER ']' child=expr            # TimedAlways
     | left=expr 'since' right=expr                                 # Since     
     | left=expr 'since' '[' '>=' l=NUMBER ']' right=expr           # TimedSinceGT
     | left=expr 'since' '[' '<=' u=NUMBER ']' right=expr           # TimedSinceLT
     | left=expr 'since' '[' l=NUMBER ',' u=NUMBER ']' right=expr   # TimedSince
     | '(' child=expr ')'                                           # Grouping
     ;

binded_atom : child=atom                         # VarConst
            | varname=IDENTIFIER '<=' child=atom # VarBind
            ;

atom : name=(TYPEDVAR | IDENTIFIER)                    # Prop
     | name=(TYPEDVAR | IDENTIFIER) '(' args=alist ')' # Pred
     | NUMBER                                          # Constant
     ;

alist : atom (',' atom)*                # AtomList
      ;

idlist : IDENTIFIER (',' IDENTIFIER)*;

IDENTIFIER : [a-zA-Z][_a-zA-Z0-9]*;

TYPEDVAR : IDENTIFIER ':' ('bool' | 'int' | 'float' | 'string'); 


NUMBER: DIGIT | (DIGIT_NOT_ZERO DIGIT+);

WS: [ \r\n\t]+ -> channel (HIDDEN);

fragment DIGIT: ('0'..'9');
fragment DIGIT_NOT_ZERO: ('1'..'9');