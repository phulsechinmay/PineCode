from rply import ParserGenerator, LexerGenerator
from boxes import *
import json
import ast
import pprint
from parser_constants import *

lg = LexerGenerator()
for key in LEXER_MAP:
    lg.add(key, LEXER_MAP[key])
lg.ignore(r"\s+")

pg = ParserGenerator(PARSER_TOKENS, precedence=PARSER_PRECEDENCE)

lexer = lg.build()

# -----------------------------------------------------------------
# -----------------------------------------------------------------
# ----------------- Parser Production Functions -------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------

@pg.production('statement : expression')
def statement_expression(p):
    return p[0]

#region ----------------- Value --> Expression -------------------

@pg.production('expression : INTEGER')
def expression_integer(p):
    return Integer(int(p[0].getstr()))

@pg.production('expression : FLOAT')
def expression_float(p):
    return Float(float(p[0].getstr()))

@pg.production('expression : STRING')
def expression_string(p):
    return String(str(p[0].getstr()))

@pg.production('expression : BOOLEAN')
def expression_boolean(p):
    return Bool(bool(p[0].getstr()))

#endregion

#region ----------------- Expression combinations --> Expression -------------------

@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MINUS expression')
@pg.production('expression : expression MUL expression')
@pg.production('expression : expression DIV expression')
def expression_binary_op(p):
    right = p[2]
    left = p[0]
    if p[1].gettokentype() == "PLUS":
        return Add(left, right)

#endregion

#region ----------------- Statements & Variables -------------------

@pg.production('statement : VAR IDENTIFIER')
def variable_declaration(p):
    return Variable(p[1].getstr())

@pg.production('statement : VAR IDENTIFIER = expression')
def variable_assignment(p):
    return Assignment(Variable(p[1].getstr()),p[3])

#endregion

# ----------------- Parser Build -------------------

parser = pg.build()

# ----------------- Helper Functions -------------------

def GetLexerOutput(file_name):
    content = open(file_name).read()
    lexed_content = lexer.lex(content)
    return lexed_content