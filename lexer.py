import ply.lex as lex
from keywords import keywords

# different classification of tokens
tokens = (
  'KEYWORD',
  'IDENTIFIER',
  'PUNCTUATOR',
  'CONSTANT',
  'OPERATOR',
  'LITERAL',
)


# regex for constants
t_CONSTANT = r"[\+\-]?\d+(\.\d+)?"
# regex for punctuators
t_PUNCTUATOR = r"[\(\)\}\{\.\;\,\[\]\#\:] | \#\# | ::"
# regex for operators
t_OPERATOR = r"\+\+|--|\+=|-=|\*=|\/=|%=|&=|\|=|\^=|<<=|>>=|\+|-|\*|\/|%|==|!=|<=|>=|&&|\|\||!|&|\||\^|~|<<|>>|=|\?|:|,|&|\*|->"


# function for checking if it is reserved keyword or identifier
def t_IDENTIFIER(t):
  r"[a-zA-Z_][a-zA-Z_0-9]*"
  # if it can not be found in keyword dictionary it is an identifier
  t.type = keywords.get(t.value, 'IDENTIFIER')
  return t

# function for identifying literals
def t_LITERAL(t):
  # regex for literal
  r"\"([^\"\\]|\\.)*\" | \'.\'"
  # t.value = t.value[1:len(t.value) - 1]
  return t

# function for handling errors, if lexem can not be matched prints error message
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  # skips the lexem
  t.lexer.skip(1)


t_ignore  = ' \t\n'
t_ignore_comment = r"\/\/ | \/*^[*]\*//"

lexer = lex.lex()

with open('input.txt', 'r') as file:
  data = file.read()

lexer.input(data)

# Tokenize
tokens = []
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    tokens.append(tok)

print(f"Total number of tokens {len(tokens)}")
for tok in tokens: 
  print(tok)
