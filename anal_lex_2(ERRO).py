# SEGUNDA TENTATIVA, UTILIZANDO SPLIT, MAS NÃO É A MANEIRA CORRETA.

palavras_reservadas = ['int', 'float','char','if', 'else', 'for', 'while', 'main', 'printf', 'continue', 'break', 'return']
separadores = ['(', ')', '{', '}', ';', '"']
operadores = ['+', '-', '/', '*', '^', '<', '<=', '>=', '=', '!=', '==']
identificadores = [] # É uma lista de dicionários.
tokens_total = [] # É uma lista de dicionários.

with open("teste.txt", "r") as arquivo:
    codigo = arquivo.read().replace('\n', '')

# A PRIMEIRA ETAPA SERIA PERCORRER O TEXTO POR CARACTERE E INSERIR ' ' ANTES E DEPOIS DE CARACTERES ESPECÍFICOS.

codigo = codigo.split(';')

# Token é um dicionário, com o formato: tk = {
#                                              id_tabela : ,
#                                              pos_tabela : ,
#                                              token_nome :
#                                              token_valor : ,
#                                             }

def gerador_token(id, pos, tk_name, tk_value):
    token = {
            "id_tabela": id,
            "pos_tabela": pos,
            "token_nome": tk_name,
            "token_valor": tk_value
    }
    return token

def busca_valor(linha, palavra):
    valor = 0
    return valor

for linha in codigo:
    palavras = linha.split()
    for palavra in palavras:

        if palavra in palavras_reservadas:
            pos_tabela = palavras_reservadas.index(palavra)
            token_nome = "tk_" + palavra
            token = gerador_token(1, pos_tabela, token_nome, "")
            tokens_total.append(token)
            continue
        
        if palavra in separadores:
            pos_tabela = separadores.index(palavra)
            token_nome = "tk_" + palavra
            token = gerador_token(2, pos_tabela, token_nome, "")
            tokens_total.append(token)
            continue

        if palavra in operadores:
            pos_tabela = operadores.index(palavra)
            token_nome = "tk_" + palavra
            token = gerador_token(3, pos_tabela, token_nome, "")
            tokens_total.append(token)
            continue
        else: 
            # Se for um identificador com valor(atribuição de variável)
            print(linha)
            print(palavra)
            try:
                prox_palavra = palavras[palavras.index(palavra) + 1]
            except:
                continue
            print(prox_palavra)
            if prox_palavra == '=':
                if len(identificadores) > 0:
                    for index in range(len(identificadores)):
                        cont  = index + 1
                        if identificadores[index]['token_nome'] == palavra:
                            token = identificadores[index]
                            tokens_total.append(token)
                            cont = 0
                            break
                        else:
                            continue
                    if cont == len(identificadores): # Não encontrou o token na tabela de identificadores.
                        pos_tabela = cont
                        token_nome = palavra
                        token_valor = busca_valor(linha, palavra)
                        token = gerador_token(4, pos_tabela, token_nome, "")
                        tokens_total.append(token)
                        identificadores.append(token)
                
                else: # Adiciona o primeiro token na tabela de identificadores.
                    pos_tabela = 0
                    token_nome = palavra
                    token = gerador_token(4, pos_tabela, token_nome, "")
                    tokens_total.append(token)
                    identificadores.append(token)
            
            
            continue

print(identificadores)


        

