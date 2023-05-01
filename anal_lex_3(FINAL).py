# TENTATIVA 3 E FINAL - MAIS SIMPLES, COLETANDO PRIMEIRO CADA LEXEMA E DEPOIS TRANSFORMANDO EM TOKENS

import re
import pandas as pd

with open("teste.c", "r") as arquivo:
    codigo = arquivo.read()

simbolos = ['!', '@', '#', '$', '%', '&', '^', '*']
operadores = ['+', '-', '*', '/', '=', '+=', '-=', '==', '<', '>', '<=', '>=']
palavras_reservadas = ['break', 'case', 'char', 'continue', 
			'double', 'else', 'float', 'for', 'if', 
			'int', 'return', 'short', 'sizeof', 
			'switch', 'unsigned', 'void', 'while']
separadores = [' ', '	', '.', ',', '\n', ';', '(', ')', '<', '>', '{', '}', '[', ']']

isStr = False
lexem = ''

lexemas = []
tokens = []
identificadores = []
constantes = []

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

	elif lexem in operadores:
		token  = {
					"nome_tk": "tk_" + lexem,
					"nome_tab": "operadores",
					"pos_tab": operadores.index(lexem)
				 }
		tokens.append(token)

	elif lexem in palavras_reservadas:
		token  = {
					"nome_tk": "tk_" + lexem,
					"nome_tab": "palavras_reservadas",
					"pos_tab": palavras_reservadas.index(lexem)
				 }
		tokens.append(token)
				
	elif re.search("^[_a-zA-Z][_a-zA-Z0-9]*$",lexem): # Expressão regular que aceita nomes de variáveis em C.
		if lexem not in identificadores: # Se não ter o lexema na tabela de id, adicionamos.
			identificadores.append(lexem)
		token  = {
					"nome_tk": "tk_id" + lexem,
					"nome_tab": "identificadores",
					"pos_tab": identificadores.index(lexem)
				 }
		tokens.append(token)
		
	elif lexem in separadores:
		token  = {
					"nome_tk": "tk_" + lexem,
					"nome_tab": "separadores",
					"pos_tab": separadores.index(lexem)
				 }
		tokens.append(token)
		
	else: # É um valor constante
		if lexem not in constantes: # Se não ter o lexema na tabela de id, adicionamos.
			constantes.append(lexem)
		token  = {
					"nome_tk": "tk_id" + lexem,
					"nome_tab": "constantes",
					"pos_tab": constantes.index(lexem)
				 }
		tokens.append(token)
				
df = pd.DataFrame(tokens)

print(df)