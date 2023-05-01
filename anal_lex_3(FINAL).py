# TENTATIVA 3 E FINAL - MAIS SIMPLES, COLETANDO PRIMEIRO CADA LEXEMA E DEPOIS TRANSFORMANDO EM TOKENS

import re

with open("teste.c", "r") as arquivo:
    codigo = arquivo.read()

simbolos = ['!', '@', '#', '$', '%', '&', '^', '*']
operadores = ['+', '-', '*', '/', '=', '+=', '-=', '==', '<', '>', '<=', '>=']
palavras_reservadas = ['break', 'case', 'char', 'continue', 
			'double', 'else', 'float', 'for', 'if', 
			'int', 'return', 'short', 'sizeof', 
			'switch', 'unsigned', 'void', 'while']
separadores = [' ', '	', '.', ',', '\n', ';', '(', ')', '<', '>', '{', '}', '[', ']']


in_keywords = []
in_spl_symbols = []
in_oparators = []
in_delimiters = []
in_identifiers = []
in_constants = []

isStr = False
isWord = False
isCmt = 0
lexem = ''

lexemas = []
tokens = []

# ETAPA 1
# Coleta dos lexemas
for i in codigo:
	# ESTADO - TEXTO ENTRE ASPAS #
	if i == '"' or i == "'":
		if isStr:
			lexemas.append(lexem)				# Assim que encontrar aspas fechando, adicionamos o token a lista.
			lexem = ''
		isStr = not isStr 						# Transformo isStr em True, e isso vai ser alterado assim que encontrar
												# a próxima aspas fechando.
	elif isStr:
		lexem = lexem+i 						#Adicionando todo caractere que está depois das aspas ao token.
    
	# ESTADO - É UM SÍMBOLO #
	elif i in simbolos:
		lexemas.append(i)
    
	# SEPARAÇÃO DE LEXEMAS #
	# ESTADO - É UM SÍMBOLO OU UM OPERADOR
	elif (i in separadores) or (i in operadores):
		if lexem: 								# Token está preenchido e o estado atual é um delimitador, ou seja, o nome  
			lexemas.append(lexem)				# do token já está coletado.
			lexem = ''
        
		if not (i==' ' or i=='\n' or i=='	'): # Token está vazio e o estado atual i não é espaço, nem \n e nem \t
			lexemas.append(i)

	# ESTADO - É ALFANUMÉRICO
	elif  i.isalnum():
		lexem = lexem+i


# ETAPA 2
# Criação dos tokens {nome_tk, nome_tab, pos_tab}
for lexem in lexemas:
	if lexem in simbolos:
		token  = {
					"nome_tk": "tk_" + lexem,
					"nome_tab": "simbolos",
					"pos_tab": simbolos.index(lexem)
				 }
		tokens.append(token)
		in_spl_symbols.append(lexem)

	elif lexem in operadores:
		in_oparators.append(lexem)

	elif lexem in palavras_reservadas:
		in_keywords.append(lexem)
				
	elif re.search("^[_a-zA-Z][_a-zA-Z0-9]*$",lexem):
		in_identifiers.append(lexem)
		
	elif lexem in separadores:
		in_delimiters.append(lexem)
		
	else:
		in_constants.append(lexem)
	
						
print(lexemas)
print(tokens)