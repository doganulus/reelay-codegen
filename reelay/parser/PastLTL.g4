grammar PastLTL;

namedExpr : (name=IDENTIFIER '=')? child=expr;

expr : child=atom                          # Atomic
     | ('!' | 'not') child=expr            # Negation
     | left=expr ('&&' | 'and') right=expr # Conjunction           
     | left=expr ('||' | 'or') right=expr  # Disjunction
     | 'once' child=expr                   # Once
     | 'always' child=expr                 # Always
     | left=expr 'since' right=expr        # Since
     | '(' child=expr ')'                  # Grouping    
     ;

atom : name=IDENTIFIER                     # Prop
	 | name=IDENTIFIER '(' args=idlist ')' # Pred
	 ;

idlist : param=IDENTIFIER (',' param=IDENTIFIER)*;


IDENTIFIER : [_a-zA-Z][_a-zA-Z0-9]*;

WS         : [ \r\n\t]+ -> channel (HIDDEN);

fragment DIGIT: ('0'..'9');
fragment DIGIT_NOT_ZERO: ('1'..'9');
