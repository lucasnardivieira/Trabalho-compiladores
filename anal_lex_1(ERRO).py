# PRIMEIRA TENTATIVA, BASEANDO NO AUTOMATO INICIAL.
import re

separadores = [' ', '(', ')', '{', '}', ';']
operadores = ['+', '-', '/', '*', '^']
palavras_reservadas = ['int', 'float','char','if', 'else', 'for', 'while', 'main', 'printf', 'continue', 'break', 'return']

#Lendo arquivo com o código a ser analisado
with open("teste.txt", "r") as arquivo:
    codigo = arquivo.read()

token = ""
for i in codigo:
    if re.match(r"([A-Za-z])", i):
        estado = 1
        # print(f"é uma letra {i}")
    
    if re.match(r"[0-9]", i ):
        estado = 2
        # print(f"é um numero {i}")
    
    if re.match(r"[\"]", i):
        estado = 3
        # print(f"é aspas {i}")

    if i in separadores:
        estado = 4
        # print(f"é um separador {i}")

    if i in operadores:
        estado = 5
        # print(f"é um operador {i}")


    if estado == 1:
        print("--- Estado 1 ---")
        if re.match(r"[\w]", i): #Aceita caracteres alfanuméricos
            token = token + i   #Vai juntando os caracteres e formando o token(palavra)
            # print(token)
    
    if estado == 2:
        print("--- Estado 2 ---")
        if re.match(r"[0-9]", i): #Aceita caracteres numéricos
            token = token + i   #Vai juntando os caracteres e formando o token(palavra)
            # print(token)
    
    if estado == 3:
        print("--- Estado 3 ---")
        print(token)
        token = ""

    if estado == 4:
        print("--- Estado 4 ---")
        print(token)
        token = ""
    
    if estado == 5:
        print("--- Estado 5 ---")
        print(token)
        token = ""

    