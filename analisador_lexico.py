import re

with open("teste2.mbs", "r") as arquivo:
    codigo = arquivo.read()

def match(lexem): 
    dici = {
        "mushroomkingdom":"TK_MAIN",
        "peach":"TK_DT_CHAR",
        "luigi": "TK_DT_FLOAT",
        'mario': 'TK_DT_INTEGER',
        'toad': 'TK_DT_STRING',
        'yoshi': 'TK_PRINT',
        'lakitu': 'TK_SCANF',
        'luma': 'TK_WHILE',
        'koopa': 'TK_IF',
        'goomba': 'TK_ELIF',
        'koopatroopa': 'TK_ELSE',
        'bowser': 'TK_FUNCTION',
        'bulletbill': 'TK_RETURN',
        'rosalina': 'TK_CONTINUE',
        'kamek': 'TK_BREAK',
        '(': 'TK_OP',
        ')': 'TK_CP',
        '{': 'TK_OK',
        '}': 'TK_CK',
        ',': 'TK_COMMA',
        '+': 'TK_MATH_ADD',
        '-': 'TK_MATH_SUB',
        '*': 'TK_MATH_MUL',
        '/': 'TK_MATH_DIV',
        '||': 'TK_LOGIC_OR',
        '&&': 'TK_LOGIC_AND',
        '!': 'TK_LOGIC_NOT',
        '!=': 'TK_LOGIC_DIF',
        '<': 'TK_LOGIC_LT',
        '<=': 'TK_LOGIC_LTE',
        '>': 'TK_LOGIC_GT',
        '>=': 'TK_LOGIC_GTE',
        '=': 'TK_ASSIGNMENT',
        '==': 'TK_LOGIC_EQ',
        ';': 'TK_END'
    }
    nome_tk = dici[lexem]
    return nome_tk    

lexemas = []
tokens = []

## TABELAS DE SÍMBOLOS PRÉ DEFINIDAS
simbolos = ['!', '@', '#', '$', '%', '&', '^', '*']

operadores = ['+', '-', '*', '/', '=', '+=', '-=', '==', '<', '>', '<=', '>=']

palavras_reservadas = ['bowser', 'mario', 'luigi','peach','koopa', 'koopatroopa', 'luma', 'mushroomkingdom',
                       'yoshi', 'lakitu', 'rosalina', 'kamek', 'bulletbill']

separadores = [' ', '	', '.', ',', '\n', ';', '(', ')', '<', '>', '{', '}', '[', ']']

### TABELAS DE SÍMBOLOS A SEREM CRIADAS
identificadores = []
constantes = []

isStr = False
isLib = False
lexem = ''
flag_erro = False

# ETAPA 1
# Coleta dos lexemas
linha = 1  # Variável para armazenar a linha atual
for i in codigo:
    if i == '\n':  # Incrementa a linha atual ao encontrar uma quebra de linha
        linha += 1

    # ESTADO - TEXTO ENTRE ASPAS #
    if i == '"' or i == "'":
        if isStr:
            lexemas.append((lexem, linha))  # Adiciona o lexema e a linha atual à lista
            lexem = ''
        isStr = not isStr
    elif isStr:
        lexem = lexem + i

    # ESTADO - INSERÇÃO DE BIBLIOTECAS
    elif isLib and i == '<':
        lexemas.append((lexem, linha))
        lexem = ''
        lexem = lexem + i
        lexemas.append((lexem, linha))
        lexem = ''

    elif isLib and i == '.':
        lexem = lexem + i

    elif isLib and i == '>':
        lexemas.append((lexem, linha))
        lexem = ''
        lexem = lexem + i
        lexemas.append((lexem, linha))
        lexem = ''
        isLib = False

    # ESTADO - É UM SÍMBOLO #
    elif i in simbolos:
        lexemas.append((i, linha))

    # SEPARAÇÃO DE LEXEMAS #
    # ESTADO - É UM SÍMBOLO OU UM OPERADOR
    elif ((i in separadores) or (i in operadores)) and (not isLib):
        if lexem:
            lexemas.append((lexem, linha))
            lexem = ''

        if not (i == ' ' or i == '\n' or i == '	'):
            lexemas.append((i, linha))

    # ESTADO - É ALFANUMÉRICO
    elif i.isalnum():
        lexem = lexem + i

    if i == '#':
        isLib = True

    if ord(i) > 127:
        flag_erro = True
        break

if flag_erro:
    print("ERRO: CARACTERE INVALIDO")
    print("ERRO na linha: ", linha)

# ETAPA 2
# Criação dos tokens {nome_tk, nome_tab, pos_tab}
for lexem, linha in lexemas:
    if lexem in simbolos:
        token = {
            "lexema": lexem,
            "nome_tk": match(lexem),
            "nome_tab": "simbolos",
            "pos_tab": simbolos.index(lexem),
            "linha": linha
        }
        tokens.append(token)

    elif lexem in operadores:
        token = {
            "lexema": lexem,
            "nome_tk": match(lexem),
            "nome_tab": "operadores",
            "pos_tab": operadores.index(lexem),
            "linha": linha
        }
        tokens.append(token)

    elif lexem in palavras_reservadas:
        token = {
            "lexema": lexem,
            "nome_tk": match(lexem),
            "nome_tab": "palavras_reservadas",
            "pos_tab": palavras_reservadas.index(lexem),
            "linha": linha
        }
        tokens.append(token)

    elif re.search("^[_a-zA-Z][_a-zA-Z0-9.]*$", lexem):
        if lexem not in identificadores:
            identificadores.append(lexem)
        token = {
            "lexema": lexem,
            "nome_tk": 'TK_IDENTIFIER',
            "nome_tab": "identificadores",
            "pos_tab": identificadores.index(lexem),
            "linha": linha
        }
        tokens.append(token)

    elif lexem in separadores:
        token = {
            "lexema": lexem,
            "nome_tk": match(lexem),
            "nome_tab": "separadores",
            "pos_tab": separadores.index(lexem),
            "linha": linha
        }
        tokens.append(token)

    else:
        if lexem not in constantes:
            constantes.append(lexem)
        if isinstance(lexem, str):
            nome_tk = 'TK_STRING'
        else:
            nome_tk = 'TK_INTEGER'
        token = {
            "lexema": lexem,
            "nome_tk": nome_tk,
            "nome_tab": "constantes",
            "pos_tab": constantes.index(lexem),
            "linha": linha
        }
        tokens.append(token)


class Token:
    def __init__(self, token_type, value, tabela, pos, linha):
        self.token_type = token_type
        self.value = value
        self.tabela = tabela
        self.pos = pos
        self.linha = linha - 1


def gera_tokens():
    tokens_final = []
    for token in tokens:
        value = token["lexema"]
        token_type = token["nome_tk"]
        tabela = token["nome_tab"]
        pos = token["pos_tab"]
        linha = token["linha"]
        tokens_final.append(Token(token_type, value, tabela, pos, linha))
    return tokens_final
