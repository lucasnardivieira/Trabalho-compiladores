'''
Exemplo de código:

int a = 10;
float b = 20;
char soma = a + b;

'''
import re
# Tokens gerados pelo analisador léxico do código acima
tokens = [{'nome_tk': 'tk_int', 'nome_tab': 'palavras_reservadas', 'pos_tab': 1}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 0}, {'nome_tk': 'tk_=', 'nome_tab': 'operadores', 'pos_tab': 4}, {'nome_tk': 'tk_id10', 'nome_tab': 'constantes', 'pos_tab': 0}, {'nome_tk': 'tk_;', 'nome_tab': 'separadores', 'pos_tab': 5}, {'nome_tk': 'tk_float', 'nome_tab': 'palavras_reservadas', 'pos_tab': 1}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 1}, {'nome_tk': 'tk_=', 'nome_tab': 'operadores', 'pos_tab': 4}, {'nome_tk': 'tk_id20', 'nome_tab': 'constantes', 'pos_tab': 1}, {'nome_tk': 'tk_;', 'nome_tab': 'separadores', 'pos_tab': 5}, {'nome_tk': 'tk_int', 'nome_tab': 'palavras_reservadas', 'pos_tab': 1}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 2}, {'nome_tk': 'tk_=', 'nome_tab': 'operadores', 'pos_tab': 4}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 0}, {'nome_tk': 'tk_+', 'nome_tab': 'operadores', 'pos_tab': 0}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 1}, {'nome_tk': 'tk_;', 'nome_tab': 'separadores', 'pos_tab': 5}]

def analisador_sintatico(token):
    print(token)
    if (token == "tk_int" or token == "tk_float" or token == "tk_char"):
        print("Definição de um tipo")
        

for token in tokens:
    analisador_sintatico(token['nome_tk'])
