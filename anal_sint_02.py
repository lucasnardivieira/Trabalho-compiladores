# Definição da função do analisador sintático
def analisador_sintatico(codigo):
    tokens = codigo.split()  # Quebra o código em tokens (palavras)
    posicao = 0  # Variável para acompanhar a posição atual na lista de tokens

    # Função auxiliar para verificar se um token corresponde a uma palavra-chave
    def verificar_palavra_chave(token):
        palavras_chave = ["if", "else", "while", "for", "int", "float", "char"]  # Lista de palavras-chave da linguagem C
        return token in palavras_chave

    # Função auxiliar para verificar se um token corresponde a um identificador
    def verificar_identificador(token):
        # Verifica se o token começa com uma letra e contém apenas letras, dígitos ou sublinhados
        return token[0].isalpha() and all(c.isalnum() or c == '_' for c in token)

    # Função auxiliar para verificar se um token corresponde a um número
    def verificar_numero(token):
        # Tenta converter o token para um número e retorna True se for bem-sucedido
        try:
            float(token)
            return True
        except ValueError:
            return False

    # Função auxiliar para verificar se um token corresponde a um operador
    def verificar_operador(token):
        operadores = ["+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">="]  # Lista de operadores válidos
        return token in operadores

    # Função auxiliar para verificar se um token corresponde a um delimitador
    def verificar_delimitador(token):
        delimitadores = ["(", ")", "{", "}", ";"]  # Lista de delimitadores válidos
        return token in delimitadores

    # Função auxiliar para verificar se um token corresponde a um caractere válido
    def verificar_caractere(token):
        return len(token) == 1

    # Função auxiliar para analisar uma expressão
    def analisar_expressao():
        nonlocal posicao  # Usada para acessar a variável 'posicao' da função pai

        token_atual = tokens[posicao]  # Obtém o token atual

        if verificar_numero(token_atual) or verificar_identificador(token_atual):
            posicao += 1  # Avança para o próximo token
        else:
            print(f"Erro de sintaxe: token inválido '{token_atual}'")

    # Função principal do analisador sintático
    while posicao < len(tokens):
        token_atual = tokens[posicao]  # Obtém o token atual

        if verificar_palavra_chave(token_atual):
            posicao += 1  # Avança para o próximo token
            if token_atual == "if":
                analisar_expressao()
                # ... Lógica adicional para análise do if
            elif token_atual == "while":
                analisar_expressao()
                # ... Lógica adicional para análise do while
            elif token_atual == "for":
                analisar_expressao()
                # ... Lógica adicional para análise do for
        elif verificar_identificador(token_atual):
            posicao += 1  # Avança para o próximo token
            # ... Lógica adicional para análise de identificadores
        elif verificar_numero(token_atual):
            posicao += 1  # Avança para o próximo token
            # ... Lógica adicional para análise de números
        elif verificar_operador(token_atual):
            posicao += 1  # Avança para o próximo token
            # ... Lógica adicional para análise de operadores
        elif verificar_delimitador(token_atual):
            posicao += 1  # Avança para o próximo token
            # ... Lógica adicional para análise de delimitadores
        elif verificar_caractere(token_atual):
            posicao += 1  # Avança para o próximo token
            # ... Lógica adicional para análise de caracteres
        else:
            print(f"Erro de sintaxe: token inválido '{token_atual}'")
            posicao += 1  # Avança mesmo em caso de erro

# Exemplo de uso do analisador sintático
codigo_c = """
int main() {
    int a = 5;
    float b = 2.3;
    if (a > b) {
        printf("a é maior que b");
    } else {
        printf("b é maior que a");
    }
    return 0;
}
"""

analisador_sintatico(codigo_c)

