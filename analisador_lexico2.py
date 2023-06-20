import re

def match(lexem): # Essa função retorna o nome(descrição) do lexema
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



with open("teste1.c", "r") as arquivo:
    codigo = arquivo.readlines()

lexemas = []
isStr = False
isLib = False
flag_erro = False

lexem = ''
line_number = 1

for line in codigo:
    for i, char in enumerate(line):
        # ESTADO - TEXTO ENTRE ASPAS #
        if char == '"' or char == "'":
            if isStr:
                lexemas.append((lexem, (line_number, i+1)))  # Adiciona o lexema e sua posição na lista de lexemas
                lexem = ''
            isStr = not isStr
        elif isStr:
            lexem = lexem + char
	
        # ESTADO - INSERÇÃO DE BIBLIOTECAS
        elif isLib and char == '<':
            lexemas.append((lexem, (line_number, i+1)))
            lexem = ''
            lexem = lexem + char
            lexemas.append((lexem, (line_number, i+1)))
            lexem = ''
	
        elif isLib and char == '.':
            lexem = lexem + char

        elif isLib and char == '>':
            lexemas.append((lexem, (line_number, i+1)))
            lexem = ''
            lexem = lexem + char
            lexemas.append((lexem, (line_number, i+1)))
            lexem = ''
            isLib = False

        # ESTADO - É UM SÍMBOLO #
        elif char in simbolos:
            lexemas.append((char, (line_number, i+1)))
    
        # SEPARAÇÃO DE LEXEMAS #
        # ESTADO - É UM SÍMBOLO OU UM OPERADOR
        elif ((char in separadores) or (char in operadores)) and (not isLib):
            if lexem:
                lexemas.append((lexem, (line_number, i)))  # Adiciona o lexema e sua posição na lista de lexemas
                lexem = ''
        
            if not (char == ' ' or char == '\n' or char == '\t'):
                lexemas.append((char, (line_number, i+1)))
    
        # ESTADO - É ALFANUMÉRICO
        elif char.isalnum():
            lexem = lexem + char

    line_number += 1

# ETAPA 2
# Criação dos tokens {nome_tk, nome_tab, pos_tab}
for lexem in lexemas:
	if lexem in simbolos:
		token  = {
                    "lexema" : lexem,
					"nome_tk": match(lexem),
					"nome_tab": "simbolos",
					"pos_tab": simbolos.index(lexem)
				 }
		tokens.append(token)

	elif lexem in operadores:
		token  = {
                    "lexema" : lexem,
					"nome_tk": match(lexem),
					"nome_tab": "operadores",
					"pos_tab": operadores.index(lexem)
				 }
		tokens.append(token)

	elif lexem in palavras_reservadas:
		token  = {
					"lexema" : lexem,
					"nome_tk": match(lexem),
					"nome_tab": "palavras_reservadas",
					"pos_tab": palavras_reservadas.index(lexem)
				 }
		tokens.append(token)
				
	elif re.search("^[_a-zA-Z][_a-zA-Z0-9.]*$",lexem): # Expressão regular que aceita nomes de variáveis em C.
		if lexem not in identificadores: 			  # Se não ter o lexema na tabela de id, adicionamos.
			identificadores.append(lexem)
		token  = {
					"lexema" : lexem,
					"nome_tk": 'TK_IDENTIFIER',
					"nome_tab": "identificadores",
					"pos_tab": identificadores.index(lexem)
				 }
		tokens.append(token)
		
	elif lexem in separadores:
		token  = {
					"lexema" : lexem,
					"nome_tk": match(lexem),
					"nome_tab": "separadores",
					"pos_tab": separadores.index(lexem)
				 }
		tokens.append(token)
		
	else: # É um valor constante
		if lexem not in constantes: # Se não ter o lexema na tabela de id, adicionamos.
			constantes.append(lexem)
		if isinstance(lexem, str):
			nome_tk = 'TK_STRING'
		else:
			nome_tk = 'TK_INTEGER'
		token  = {
					"lexema" : lexem,
					"nome_tk": nome_tk,
					"nome_tab": "constantes",
					"pos_tab": constantes.index(lexem)
				 }
		tokens.append(token)

class Token: # É preciso transformar os tokens da lista nessa estrutura para gerar a árvore
    def __init__(self, token_type, value, tabela, pos):
        self.token_type = token_type
        self.value = value
        self.tabela = tabela
        self.pos = pos

def gera_tokens():
    tokens_final = []
    for token in tokens:
        value = token["lexema"]
        token_type = token["nome_tk"]
        tabela = token["nome_tab"]
        pos = token["pos_tab"]
        # linha = token[linha]
        tokens_final.append(Token(token_type, value, tabela, pos))
    return tokens_final