from parser import *
import sys

LEXER_MAP_FILE = "lexer_map.dict"
TEST_FILE = "test.pc"

lexer_output = GetLexerOutput(TEST_FILE)
parser_output = parser.parse(lexer_output)
print(parser_output)
