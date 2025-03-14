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
t_OPERATOR = r"\+\+|--|\+=|-=|\*=|\/=|%=|&=|\|=|\^=|<<=|>>=|\+|-|\*|\/|%|==|!=|<=|>=|&&|\|\||!|&|\||\^|~|<<|>>|=|\?|:|,|&|\*|->|>|<"


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
  return (t.value[0], t.lineno, t.lexpos)


t_ignore  = ' \t\n'
t_ignore_comment = r"\/\/ | \/*^[*]\*//"


# Transform the list of tokens into a string
def token_list_to_string( list_tokens ):
    
    str_tokens = f"The total number of tokens is: {len(list_tokens)}\n" + "Type\t\tValue\t\tLine\t\tPosition\n"

    for tok in list_tokens:
        str_tokens += f"{tok.type}\t\t{tok.value}\t\t{tok.lineno}\t\t{tok.lexpos}\n"
    
    return str_tokens

# Transform the error list into a string
def error_list_to_string( list_errors ):
   
    str_errors = "\n"

    for error in list_errors:
        str_errors += f"ERROR\t\t{error[0]}\t\t{error[1]}\t\t{error[2]}\n"

    return str_errors

# Function to analyze the input data
def Lexer_analyzer( input_data ):
    
    # Initialize the lexer
    lexer = lex.lex()

    # Pass the input data to the lexer
    lexer.input(input_data)

    # Tokenize
    list_tokens = []
    list_errors = []
    while True:
        tok = lexer.token()
        if type(tok) == tuple:
            list_errors.append(tok)
            continue
        if not tok: 
            break
        list_tokens.append(tok)
    
    string_tokens = token_list_to_string(list_tokens)
    string_errors = error_list_to_string(list_errors)

    return string_tokens + string_errors


if __name__ == "__main__":
    
    lexer = lex.lex()

    with open('input.txt', 'r') as file:
      data = file.read()

    lexer.input(data)

    # Tokenize
    tokens = []
    while True:
        tok = lexer.token()
        if not tok: 
            break
        tokens.append(tok)

    print(f"The total number of tokens is: {len(tokens)}")
    print("Type\t\tValue\t\tLine\t\tPosition")
    for tok in tokens: 
      print(f"{tok.type}\t\t{tok.value}\t\t{tok.lineno}\t\t{tok.lexpos}\n")



