import re

class SymbolTableEntry:
    def __init__(self, name, symbol_type):
        self.name = name
        self.symbol_type = symbol_type

class SymbolTable:
    def __init__(self):
        self.entries = []

    def add_entry(self, name, symbol_type):
        entry = SymbolTableEntry(name, symbol_type)
        self.entries.append(entry)

    def get_entries(self):
        return self.entries

def split_custom(input_str):
    output = []
    current_str = ""

    for char in input_str:
        if char.isalnum():
            current_str += char
        else:
            if current_str:
                output.append(current_str)
            current_str = ""
            output.append(char)
    return output

def concatena_strings(vetor):
    i = 0
    while i < len(vetor):
        if vetor[i][-1] in ['!', '=', '<', '>'] and vetor[i+1][0] == '=':
            vetor[i] = vetor[i] + vetor[i+1]
            vetor.pop(i+1)
        else:
            i += 1
    return vetor

def gera_lexemas(vetor):
    i = 0
    linhas = 1
    while i < len(vetor):
        if vetor[i] == '\n':
            linhas=linhas+1
            i=i+1
        elif vetor[i] != (' ' or '\t' or ' '):
            lexemas.append(vetor[i])
            l_lexemas.append(linhas)
            i=i+1
        else:
            i=i+1




    return vetor

lexemas = []
l_lexemas = []
tabela_simbolos = []
identificadores = []
with open("teste.c", "r") as arquivo:
    codigo = arquivo.read()
    codigo = split_custom(codigo)
    codigo = concatena_strings(codigo)
    gera_lexemas(codigo)

keywords = {
        'main': 'TK_RW_MAIN',
        'string': 'TK_RW_STRING',
        'int': 'TK_RW_INTEGER',
        'print': 'TK_RW_PRINT',
        'read': 'TK_RW_SCANF',
        'while': 'TK_RW_WHILE',
        'if': 'TK_RW_IF',
        'elif': 'TK_RW_ELIF',
        'else': 'TK_RW_ELSE',
        'def': 'TK_RW_FUNCTION',
        'return': 'TK_RW_RETURN'
    }
operators = {
        '+': 'TK_MATH_ADD',
        '-': 'TK_MATH_SUB',
        '*': 'TK_MATH_MUL',
        '/': 'TK_MATH_DIV',
        '=': 'TK_ASSIGNMENT',
        '==': 'TK_LOGIC_EQ',
        '!=': 'TK_LOGIC_DIF',
        '<': 'TK_LOGIC_LT',
        '<=': 'TK_LOGIC_LTE',
        '>': 'TK_LOGIC_GT',
        '>=': 'TK_LOGIC_GTE',
        '||': 'TK_LOGIC_OR',
        '&&': 'TK_LOGIC_AND',
        '!': 'TK_LOGIC_NOT'
    }
separators = {
        '(': 'TK_OP',
        ')': 'TK_CP',
        '{': 'TK_OK',
        '}': 'TK_CK',
        ',': 'TK_COMMA',
        ';': 'TK_END'
    }
regex = {
        'identifier': r'[a-zA-Z][a-zA-Z0-9]*',
        'integer': r'\d+',
        'string': r'"[a-zA-Z0-9@{}+\-*/=(),]+"'
    }

tokens = []
token = {}
for word in lexemas:
        if word in keywords:
            token  = {
					"token": keywords[word],
					"nome_tab": "keywords",
                    "lexema": word,
                    "linha": l_lexemas[lexemas.index(word)]
				 }
            tokens.append(token)
        elif re.match(regex['identifier'], word):
            token  = {
					"token": 'TK_IDENTIFIER_'+str(lexemas.index(word)),
					"nome_tab": "regex",
                    "lexema": word,
                    "linha": l_lexemas[lexemas.index(word)]
				 }
            tokens.append(token)
        elif re.match(regex['integer'], word):
            token  = {
					"token": 'TK_INTEGER_'+str(lexemas.index(word)),
					"nome_tab": "regex",
                    "lexema": word,
                    "linha": l_lexemas[lexemas.index(word)]
				 }
            tokens.append(token)
        elif re.match(regex['string'], word):
            token  = {
					"token": 'TK_STRING_'+str(lexemas.index(word)),
					"nome_tab": "regex",
                    "lexema": word,
                    "linha": l_lexemas[lexemas.index(word)]
				 }
            tokens.append(token)
        elif word in operators:
            token  = {
					"token": operators[word],
					"nome_tab": "operators",
                    "lexema": word,
                    "linha": l_lexemas[lexemas.index(word)]
				 }
            tokens.append(token)
        elif word in separators:
            token  = {
					"token": separators[word],
					"nome_tab": "separators",
                    "lexema": word,
                    "linha": l_lexemas[lexemas.index(word)]
				 }
            tokens.append(token)


print(tokens)
