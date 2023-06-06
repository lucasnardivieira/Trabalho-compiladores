from lark import Lark

# Gramática para a linguagem C simplificada
grammar = """
    start: function
    function: "int" "main" "(" ")" "{" statement+ "}"
    statement: declaration | assignment | if_statement | print_statement
    declaration: "int" NAME "=" NUMBER ";"
    assignment: NAME "=" expression ";"
    if_statement: "if" "(" expression ")" "{" statement+ "}"
    print_statement: "printf" "(" STRING ")" ";"
    expression: atom ">" atom -> gt
              | atom
    atom: NUMBER -> number
        | NAME -> variable
        | "(" expression ")"
    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.STRING
    %import common.WS
    %ignore WS
"""

# Função para interpretar uma expressão
def interpret_expression(tree):
    if tree.data == 'gt':
        left = interpret_expression(tree.children[0])
        right = interpret_expression(tree.children[1])
        return left > right
    elif tree.data == 'number':
        return int(tree.children[0])
    elif tree.data == 'variable':
        variable_name = tree.children[0]
        if variable_name in variables:
            return variables[variable_name]
        else:
            raise ValueError(f"Variável '{variable_name}' não definida")
    else:
        raise ValueError(f"Expressão inválida: {tree.data}")

# Função para interpretar uma declaração
def interpret_declaration(tree):
    variable_name = tree.children[0]
    value = interpret_expression(tree.children[1])
    variables[variable_name] = value

# Função para interpretar uma atribuição
def interpret_assignment(tree):
    variable_name = tree.children[0]
    value = interpret_expression(tree.children[1])
    if variable_name in variables:
        variables[variable_name] = value
    else:
        raise ValueError(f"Variável '{variable_name}' não definida")

# Função para interpretar uma instrução de impressão
def interpret_print_statement(tree):
    string = tree.children[0].strip('"')
    print(string)

# Função para interpretar uma instrução condicional 'if'
def interpret_if_statement(tree):
    condition = interpret_expression(tree.children[0])
    if condition:
        for statement in tree.children[1:]:
            interpret_statement(statement)

# Função para interpretar uma instrução
def interpret_statement(tree):
    if tree.data == 'declaration':
        interpret_declaration(tree)
    elif tree.data == 'assignment':
        interpret_assignment(tree)
    elif tree.data == 'if_statement':
        interpret_if_statement(tree)
    elif tree.data == 'print_statement':
        interpret_print_statement(tree)
    else:
        raise ValueError(f"Instrução inválida: {tree.data}")

# Função para interpretar um programa
def interpret_program(tree):
    for statement in tree.children:
        interpret_statement(statement)

# Código-fonte em C
source_code = """
int main() {
    int a = 5;
    int b = 10;
    int c = a + b;
    
    if (c > 15) {
        printf("C é maior que 15");
    } else {
        printf("C é menor ou igual a 15");
    }
    
    return 0;
}
"""

# Construir o analisador sintático
parser = Lark(grammar, start='start')

# Interpretar o código-fonte
variables = {}
tree = parser.parse(source_code)
interpret_program(tree)
