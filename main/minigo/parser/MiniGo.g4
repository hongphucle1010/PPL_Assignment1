grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
	super().__init__(input, output)
	self.checkVersion("4.9.2")
	self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
	self._actions = None
	self._predicates = None
	self.preType = None

def emit(self):
    self.ltk = self.type
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language = Python3;
}

program: many_declarations? EOF;

many_declarations: declaration many_declarations | declaration;

declaration: (
		varDeclaration
		| constDeclaration
		| structDeclaration
		| interfaceDeclaration
	) SEMI
	| ( funcDeclaration | methodDeclaration) SEMI?;

// Variable Declaration
varDeclaration:
	VAR ID typeSpec (ASSIGN expression)?
	| VAR ID ASSIGN expression;

// Constant Declaration
constDeclaration: CONST ID ASSIGN expression;

// Function Declaration
funcDeclaration:
	FUNC ID LPAREN paramList? RPAREN typeSpec? block;
paramList: param (COMMA paramList)?;
param: multiID typeSpec;
multiID: ID (COMMA multiID)?;

// Method Declaration
methodDeclaration:
	FUNC methodReceiver ID LPAREN paramList? RPAREN typeSpec? block;
methodReceiver: LPAREN ID ID RPAREN;

// Struct Declaration
structDeclaration: TYPE ID STRUCT LBRACE structFields? RBRACE;
structFields: field SEMI structFields?;
field: param;

// Interface Declaration
interfaceDeclaration:
	TYPE ID INTERFACE LBRACE methodSignatures? RBRACE;
methodSignatures: methodSignature SEMI methodSignatures?;
methodSignature: ID LPAREN paramList? RPAREN typeSpec?;

// Statements
block: LBRACE stmtList? RBRACE;
stmtList: statement stmtList | statement;
statement:
	(
		| assignStmt
		| breakStmt
		| continueStmt
		| callStmt
		| returnStmt
	) SEMI
	| varDeclaration
	| constDeclaration
	| ifStmt SEMI?
	| forStmt SEMI?;

assignStmt: lhs assignmentOp expression;
lhs:
	ID
	| lhs LBRACK expression RBRACK // Array element access
	| lhs DOT ID; // Struct field access
assignmentOp:
	DECLARE
	| ASSIGN
	| ADD_ASSIGN
	| SUB_ASSIGN
	| MUL_ASSIGN
	| DIV_ASSIGN
	| MOD_ASSIGN;

// If Statement
ifStmt:
	IF LPAREN expression RPAREN block (ELSE ifStmt)?
	| ifElseStmt;
ifElseStmt: IF LPAREN expression RPAREN block (ELSE block)?;

// For Statement
forStmt: FOR forCondition block;
forCondition: forExpr | forLoop | forRange;
forExpr: expression;
forLoop:
	(varDeclaration | assignStmt)? SEMI expression? SEMI assignStmt?;
forRange: (ID COMMA ID | UNDERSCORE COMMA ID) DECLARE RANGE ID;

// Other Statements
breakStmt: BREAK;
continueStmt: CONTINUE;
callStmt: funcCall | methodCall;
returnStmt: RETURN expression?;

// Types
primitiveType: INT | FLOAT | STRING | BOOLEAN;
typeSpec: arrayType | primitiveType | ID;

// Literals
literal:
	INT_LIT
	| FLOAT_LIT
	| STR_LIT
	| TRUE
	| FALSE
	| NIL
	| arrayLiteral
	| structLiteral;
arrayLiteral: arrayType LBRACE exprList? RBRACE;
arrayType: LBRACK INT_LIT RBRACK typeSpec;
structLiteral: ID LBRACE structElements? RBRACE;
structElements: structElement (COMMA structElements)?;
structElement: ID COLON expression;

// Expressions
exprList: expression COMMA exprList | expression;
expression: expression OR expr1 | expr1;
expr1: expr1 AND expr2 | expr2;
expr2: expr2 compOp expr3 | expr3;
compOp:
	EQUAL
	| NOTEQUAL
	| LESS
	| LESSEQUAL
	| GREATER
	| GREATEREQUAL;
expr3: expr3 addOp expr4 | expr4;
addOp: ADD | SUB;
expr4: expr4 mulOp expr5 | expr5;
mulOp: MUL | DIV | MOD;
expr5: (NOT | SUB) expr6 | expr6;
expr6:
	expr6 LBRACK expression RBRACK
	| expr6 DOT (ID | funcCall)
	| expr7;
expr7:
	literal
	| ID
	| LPAREN expression RPAREN
	| funcCall
	| methodCall;
funcCall: ID LPAREN exprList? RPAREN;
methodCall: ID DOT ID LPAREN exprList? RPAREN;

// ! ---------------- LEXER DEADLINE PASS 13 TEST CASE 23:59 16/1 ----------------------- */

//TODO Keywords 3.3.2 pdf
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';
BOOLEAN: 'boolean';
CONST: 'const';

//TODO Operators 3.3.3 pdf
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

EQUAL: '==';
NOTEQUAL: '!=';
LESS: '<';
LESSEQUAL: '<=';
GREATER: '>';
GREATEREQUAL: '>=';

DECLARE: ':=';
ASSIGN: '=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';

AND: '&&';
OR: '||';
NOT: '!';
DOT: '.';

//TODO Separators 3.3.4 pdf
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
SEMI: ';';
COLON: ':';

//TODO Literals 3.3.5 pdf
INT_LIT: '0' | [1-9] [0-9]*;
BIN_LIT: '0' [bB] [01]+;
OCT_LIT: '0' [oO] [0-7]+;
HEX_LIT: '0' [xX] [0-9a-fA-F]+;
FLOAT_LIT: [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?;

fragment ESC_LETTER: [ntr"\\];
fragment ESCAPE: '\\' ESC_LETTER;
fragment STR_CHAR: ~[\n"\\] | ESCAPE;
STR_LIT: '"' STR_CHAR* '"';
UNDERSCORE: '_';

//TODO Identifiers 3.3.1 pdf
ID: [a-zA-Z_][a-zA-Z_0-9]*;

//TODO skip 3.1 and 3.2 pdf
NEWLINE:
	'\r'? '\n' {
    if hasattr(self, 'ltk') and self.ltk in [
		self.ID, self.INT_LIT, self.HEX_LIT, self.BIN_LIT, self.OCT_LIT, self.FLOAT_LIT, self.BOOLEAN, self.STR_LIT, 
		self.RPAREN, self.RBRACK, self.RBRACE, self.STRING, self.INT, self.FLOAT, self.BOOLEAN, self.NIL, self.TRUE, self.FALSE,
		self.RETURN, self.CONTINUE, self.BREAK
	]:
        self.text = ';'
        self.type = self.SEMI
    else:
        self.skip()
};

WS: [ \t\f\r]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;

//TODO ERROR pdf BTL1 + lexererr.py
UNCLOSE_STRING:
	'"' STR_CHAR* ('\r\n' | '\n' | EOF) {
if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
    raise UncloseString(self.text[:-2])  # Case \r\n
elif (self.text[-1] == '\n'):
    raise UncloseString(self.text[:-1])  # Case \n
else:
    raise UncloseString(self.text)    # Case EOF
};
fragment ESCAPE_ILLEGAL: '\\' ~[ntr"\\];
ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESCAPE_ILLEGAL {
    raise IllegalEscape(self.text)
};
ERROR_CHAR: . {raise ErrorToken(self.text)};