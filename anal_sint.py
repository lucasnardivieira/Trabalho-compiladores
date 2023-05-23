'''
Exemplo de código:
def funcao_X(int a, char b)
{
    int soma;
    soma = a + b;

    return soma;
}
'''
# Tokens gerados pelo analisador léxico do código acima
tokens = [{'nome_tk': 'tk_def', 'nome_tab': 'palavras_reservadas', 'pos_tab': 0}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 0}, {'nome_tk': 'tk_(', 'nome_tab': 'separadores', 'pos_tab': 6}, {'nome_tk': 'tk_int', 'nome_tab': 'palavras_reservadas', 'pos_tab': 1}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 1}, {'nome_tk': 'tk_,', 'nome_tab': 'separadores', 'pos_tab': 3}, {'nome_tk': 'tk_char', 'nome_tab': 'palavras_reservadas', 'pos_tab': 3}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 2}, {'nome_tk': 'tk_)', 'nome_tab': 'separadores', 'pos_tab': 7}, {'nome_tk': 'tk_{', 'nome_tab': 'separadores', 'pos_tab': 10}, {'nome_tk': 'tk_int', 'nome_tab': 'palavras_reservadas', 'pos_tab': 1}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 3}, {'nome_tk': 'tk_;', 'nome_tab': 'separadores', 'pos_tab': 5}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 3}, {'nome_tk': 'tk_=', 'nome_tab': 'operadores', 'pos_tab': 4}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 1}, {'nome_tk': 'tk_+', 'nome_tab': 'operadores', 'pos_tab': 0}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 2}, {'nome_tk': 'tk_;', 'nome_tab': 'separadores', 'pos_tab': 5}, {'nome_tk': 'tk_return', 'nome_tab': 'palavras_reservadas', 'pos_tab': 13}, {'nome_tk': 'tk_id', 'nome_tab': 'identificadores', 'pos_tab': 3}, {'nome_tk': 'tk_;', 'nome_tab': 'separadores', 'pos_tab': 5}, {'nome_tk': 'tk_}', 'nome_tab': 'separadores', 'pos_tab': 11}]

import re
#IDEIA: montar blocos de código. Bloco para cada definição, tem que começar com token específico e fechar com outro token específico
def analisador_sintatico(tokens):
    for token in tokens:
        print(token['nome_tk'])
        # Definição de variavel

        # Definição de função

            # Definição de parametro de função

        # Definição IF

        # Definição WHILE



    

analisador_sintatico(tokens)
