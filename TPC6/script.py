"""
GRAMÁTICA

G = {T,N,S,P}

REGRAS:


PROGRAMA -> INSTRUCOES
INSTRUCOES -> INSTRUCAO INSTRUCOES
            | ε
INSTRUCAO -> ATRIBUICAO
           | ENTRADA
           | SAIDA
ATRIBUICAO -> ID '=' EXP
ENTRADA -> '?' ID
SAIDA -> '!' EXP
EXP -> TERMO '+' EXP
     | TERMO '-' EXP
     | TERMO
TERMO -> FATOR '*' TERMO
       | FATOR '/' TERMO
       | FATOR
FATOR -> '(' EXP ')'
       | NUM
       | ID
"""

# Parte LEXER
import ply.lex as lex

tokens = (
    'NUM',
    'ID',
    'PLUS', 'MINUS', 'MULT', 'DIV',
    'INPUT', 'OUTPUT', 'EQUAL',
    'LPAREN', 'RPAREN',
)

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_MULT   = r'\*'
t_DIV    = r'/'
t_INPUT  = r'\?'
t_OUTPUT = r'!'
t_EQUAL  = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t\n'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Parte YACC
import ply.yacc as yacc

def p_programa(p):
    "PROGRAMA : INSTRUCOES"
    p[0] = p[1]

def p_instrucoes_recursivo(p):
    "INSTRUCOES : INSTRUCAO INSTRUCOES"
    p[0] = [p[1]] + p[2]

def p_instrucoes_base(p):
    "INSTRUCOES : "
    p[0] = []

def p_instrucao(p):
    """
    INSTRUCAO : ATRIBUICAO
              | ENTRADA
              | SAIDA
    """
    p[0] = p[1]

def p_atribuicao(p):
    "ATRIBUICAO : ID EQUAL EXP"
    p[0] = ('ATRIBUICAO', p[1], p[3])

def p_entrada(p):
    "ENTRADA : INPUT ID"
    p[0] = ('ENTRADA', p[2])

def p_saida(p):
    "SAIDA : OUTPUT EXP"
    p[0] = ('SAIDA', p[2])

def p_exp_plus(p):
    "EXP : TERMO PLUS EXP"
    p[0] = ('+', p[1], p[3])

def p_exp_minus(p):
    "EXP : TERMO MINUS EXP"
    p[0] = ('-', p[1], p[3])

def p_exp_termo(p):
    "EXP : TERMO"
    p[0] = p[1]

def p_termo_mult(p):
    "TERMO : FATOR MULT TERMO"
    p[0] = ('*', p[1], p[3])

def p_termo_div(p):
    "TERMO : FATOR DIV TERMO"
    p[0] = ('/', p[1], p[3])

def p_termo_fator(p):
    "TERMO : FATOR"
    p[0] = p[1]

def p_fator_exp(p):
    "FATOR : LPAREN EXP RPAREN"
    p[0] = p[2]

def p_fator_num(p):
    "FATOR : NUM"
    p[0] = ('NUM', p[1])

def p_fator_id(p):
    "FATOR : ID"
    p[0] = ('ID', p[1])

def p_error(p):
    parser.success = True
    print("Syntax error in input!")

input_data = """
?x
y=x*2/(27-3)+5
!y*(x+3)
"""

parser = yacc.yacc()
parser.success = True

result = parser.parse(input_data)
print(result)

if parser.success:
    print('Parsing completed!')
else:
    print('Parsing failed!')