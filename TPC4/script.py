import ply.lex as lex

reserved = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'and': 'AND',
    'or': 'OR',
    'like': 'LIKE',
    'inner': 'INNER',
    'outer': 'OUTER',
    'left': 'LEFT',
    'right': 'RIGHT',
    'full': 'FULL',
    'on': 'ON',
}

tokens = [
    'IDENTIFIER',
    'COMMA',
    'PERIOD',
    'SEMICOLON',
    'OPERATOR',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'NUMBER',
    'STRING',
] + list(reserved.values())

t_COMMA = r','
t_PERIOD = r'\.'
t_SEMICOLON = r';'
t_OPERATOR = r'[=<>]=?'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_STRING = r"'[^']*'"

def t_IDENTIFIER(t):
    r'\b[a-zA-Z]\w*?\b'
    t.type = reserved.get(t.value.lower(), 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_COMMENT(t):
    r'--.*'
    pass

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

sql_query = """
SELECT id, nome, salario FROM empregados WHERE salario >= 820
"""
lexer.input(sql_query)

for tok in lexer:
    print(tok)