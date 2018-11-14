LEXER_MAP = {
    'FLOAT': r"-?\d+.\d+",
    'INTEGER': r"-?\d+",
    'STRING': r"(\"\"\".*\"\"\")|(\".*\")|(\'.*\')",
    'BOOLEAN': r"true(?!\w)|false(?!\w)",
    'IF': r"if(?!\w)",
    'ELSE': r"else(?!\w)",
    'END': r"end(?!\w)",
    'AND': r"and(?!\w)",
    'OR': r"or(?!\w)",
    'NOT': r"not(?!\w)",
    'VAR': r"var(?!\w)",
    'FUNCTION': r"func(?!\w)",
    'MODULE': r"mod(?!\w)",
    'IMPORT': r"import(?!\w)",
    'IDENTIFIER': r"[a-zA-Z_][a-zA-Z0-9_]*",
    '==': r"\==",
    '!=': r"\!=",
    '>=': r"\>=",
    '<=': r"\<=",
    '>': r"\>",
    '<': r"\<",
    '=': r"\=",
    '[': r"\[",
    ']': r"\]",
    '{': r"\{",
    '}': r"\}",
    '|': r"\|",
    ',': r"\,",
    'DOT': r"\.",
    'COLON': r"\:",
    'PLUS': r"\+",
    'MINUS': r"\-",
    'MUL': r"\*",
    'DIV': r"\/",
    'MOD': r"\%",
    'SEMICOLOR' : r"\;",
    '(': r"\(",
    ')': r"\)",
    'NEWLINE': r"\n"
}

PARSER_TOKENS = [
    'STRING', 'INTEGER', 'FLOAT', 'IDENTIFIER', 'BOOLEAN', 'PLUS', 'MINUS', 'MUL', 'DIV', 'IF', 'ELSE', 'COLON', 'END', 'AND', 'OR', 'NOT', 'VAR','WHILE', '(', ')', '=', '==', '!=', '>=', '<=', '<', '>', '[', ']', ',', '{','}', '$end', 'NEWLINE', 'FUNCTION'
]

PARSER_PRECEDENCE = [ 
        ('left', ['FUNCTION',]), 
        ('left', ['LET',]), 
        ('left', ['=']), 
        ('left', ['[',']',',']), 
        ('left', ['IF', 'COLON', 'ELSE', 'END', 'NEWLINE','WHILE',]), 
        ('left', ['AND', 'OR',]), 
        ('left', ['NOT',]), 
        ('left', ['==', '!=', '>=','>', '<', '<=',]), 
        ('left', ['PLUS', 'MINUS',]), 
        ('left', ['MUL', 'DIV',]), 
] 