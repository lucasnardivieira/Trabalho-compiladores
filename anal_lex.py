import re

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
    while i < len(vetor)-1:
        if vetor[i][-1] in ['!', '=', '<', '>'] and vetor[i+1][0] == '=':
            vetor[i] = vetor[i] + vetor[i+1]
            vetor.pop(i+1)
        else:
            i += 1
    return vetor

with open("teste.c", "r") as arquivo:
    codigo = arquivo.read()
    codigo = split_custom(codigo)
    codigo = concatena_strings(codigo)

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
for word in codigo:
        if word in keywords:
            tokens.append(keywords[word])
        elif re.match(regex['identifier'], word):
            tokens.append('TK_IDENTIFIER')
        elif re.match(regex['integer'], word):
            tokens.append('TK_INTEGER')
        elif re.match(regex['string'], word):
            tokens.append('TK_STRING')
        elif word in operators:
            tokens.append(operators[word])
        elif word in separators:
            tokens.append(separators[word])

print(tokens)
