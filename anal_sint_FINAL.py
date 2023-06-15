############################################
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        self.children.remove(node)

    def __repr__(self):
        return self.data


class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"Token({self.token_type}, {self.value})"


class Parser:
    def __init__(self, tokens):
        print("# CRIOU A CLASSE PARSER #")
        self.tokens = tokens
        self.current_token = None
        self.token_index = -1
        self.root = None

    def parse(self):
        print("# CHAMOU O PARSE #")
        self.advance()
        self.root = self.init_node()
        return self.root # Retorna a raíz da árvore

    def advance(self):
        print("# --> ")
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None

    def match(self, token_type): # Método que compara o tipo do token e avança caso TRUE
        if self.current_token and self.current_token.token_type == token_type:
            self.advance()
        else:
            raise SyntaxError(f"Expected {token_type}, but found {self.current_token.token_type}")

    def init_node(self):
        print("# CRIOU O NÓ RAIZ #")
        node = TreeNode("<init>")
        node.add_child(self.function_declaration_node())
        print_tree(node)
        # node.add_child(self.main_function_node())
        return node # Retorna para o def parse

    def main_function_node(self):
        print("## nó raíz ##")
        node = TreeNode("<mainFunction>")
        self.match("functionIndicator")
        self.match("dataType")
        self.match("identifier")
        self.match("openParentheses")
        self.match("closeParentheses")
        self.match("openKey")
        node.add_child(self.content_node())
        self.match("closeKey")
        return node

    def function_declaration_node(self):
        print("# CRIOU O NÓ DECLARAÇÃO FUNÇAO #")
        node = TreeNode("<functionDeclaration>")
        print(self.current_token)
        self.match("functionIndicator")
        print(self.current_token)
        self.match("dataType")
        print(self.current_token)
        self.match("identifier")
        print(self.current_token)
        self.match("openParentheses")
        print(self.current_token)
        if self.current_token and self.current_token.token_type != "closeParentheses": # Significa que a funçao tem parametros
            node.add_child(self.function_parameters_node())
        print(self.current_token)
        self.match("closeParentheses")
        print(self.current_token)
        self.match("openKey")
        node.add_child(self.content_node()) # Conteúdo da função
        node.add_child(self.function_return_node())
        print(node.children)
        self.match("closeKey")
        return node

    def function_parameters_node(self):
        print("# CRIOU O NÓ PARAMETROS DE FUNÇAO #")
        node = TreeNode("<functionParameters>")
        node.add_child(self.data_type_node())
        node.add_child(self.identifier_node())
        while self.current_token and self.current_token.token_type == "comma": # Quando encontra uma vírgula, há mais paramêtros
            self.match("comma")
            node.add_child(self.function_parameters_node())
        return node

    def function_return_node(self):
        print("# CRIOU NÓ DE RETORNO #")
        print(self.current_token)
        node = TreeNode("<functionReturn>")
        self.match("giveBack")
        node.add_child(self.logic_expression_node())
        self.match("end")
        return node

    def content_node(self):
        print("# CRIOU O NÓ CONTEÚDO #")
        print(self.current_token)
        node = TreeNode("<content>")
        if self.current_token and self.current_token.token_type in ["dataType"]:
            node.add_child(self.variable_declaration_node())
        elif self.current_token and self.current_token.token_type in ["if", "while"]:
            node.add_child(self.selection_structure_node())
        elif self.current_token and self.current_token.token_type == "print":
            node.add_child(self.output_node())
        elif self.current_token and self.current_token.token_type == "scanf":
            node.add_child(self.input_node())
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token.token_type}")
        print(node.data)
        return node

    def variable_declaration_node(self):
        print("# CRIOU O NÓ DECLARAÇÃO VAR #")
        node = TreeNode("<variableDeclaration>")
        node.add_child(self.data_type_node())
        node.add_child(self.identifier_node())
        print(self.current_token)
        if self.current_token and self.current_token.token_type == "assignmentOperator":
            node.add_child(self.assignment_node())
            node.add_child(self.logic_expression_node())
        self.match("end")
        return node

    def logic_expression_node(self):
        print("# CRIOU O NÓ EXPRESSAO LÓGICA #")
        print(self.current_token)
        node = TreeNode("<logicalExpression>")
        node.add_child(self.expression_node())
        while self.current_token and self.current_token.token_type in ["or", "and"]:
            node.add_child(TreeNode(self.current_token.token_type))
            self.advance()
            node.add_child(self.expression_node())
        return node

    def expression_node(self):
        print("# CRIOU O NÓ EXPRESSAO #")
        print(self.current_token)
        node = TreeNode("<expression>")
        node.add_child(self.relation_node())
        while self.current_token and self.current_token.token_type in ["addition", "subtraction"]:
            node.add_child(TreeNode(self.current_token.token_type))
            self.advance()
            node.add_child(self.relation_node())
        return node

    def relation_node(self):
        print("# CRIOU O NÓ RELAÇÃO #")
        print(self.current_token)
        node = TreeNode("<relation>")
        if self.current_token and self.current_token.token_type == "openParentheses":
            self.match("openParentheses")
            node.add_child(self.logic_expression_node())
            self.match("closeParentheses")
        else:
            node.add_child(self.math_expression_node())
        return node

    def math_expression_node(self):
        print("# CRIOU O NÓ EXPRESSÃO MATEMÁTICA #")
        node = TreeNode("<mathExpression>")
        if self.current_token and self.current_token.token_type in ["addition", "subtraction"]:
            node.add_child(TreeNode(self.current_token.token_type))
            self.advance()
        node.add_child(self.term_node())
        while self.current_token and self.current_token.token_type in ["+", "-", "arithmeticOperator"]:
            node.add_child(TreeNode(self.current_token.token_type))
            self.advance()
            node.add_child(self.term_node())
        return node

    def term_node(self):
        print("# CRIOU O NÓ TERMO #")
        print(self.current_token)
        node = TreeNode("<term>")
        node.add_child(self.factor_node())
        while self.current_token and self.current_token.token_type in ["*", "/"]:
            node.add_child(TreeNode(self.current_token.token_type))
            self.advance()
            node.add_child(self.factor_node())

        return node

    def factor_node(self):
        print("# CRIOU O NÓ FACTOR #")
        print(self.current_token)
        node = TreeNode("<factor>")
        if self.current_token and self.current_token.token_type == "openParentheses":
            self.match("openParentheses")
            node.add_child(self.math_expression_node())
            self.match("closeParentheses")
        elif self.current_token and self.current_token.token_type == "identifier":
            node.add_child(self.identifier_node())
        elif self.current_token and self.current_token.token_type in ["real", "integer", "string"]:
            node.add_child(TreeNode(self.current_token.token_type))
            self.advance()
        elif self.current_token and self.current_token.token_type == "functionCall":
            node.add_child(self.function_call_node())
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token.token_type}")
        return node

    def selection_structure_node(self):
        node = TreeNode("<selectionStructure>")
        node.add_child(self.if_declaration_node())
        while self.current_token and self.current_token.token_type == "elif":
            node.add_child(self.elif_declaration_node())
        if self.current_token and self.current_token.token_type == "else":
            node.add_child(self.else_declaration_node())
        return node

    def if_declaration_node(self):
        node = TreeNode("<ifDeclaration>")
        self.match("if")
        self.match("openParentheses")
        node.add_child(self.logic_expression_node())
        self.match("closeParentheses")
        self.match("openKey")
        if self.current_token and self.current_token.token_type != "closeKey":
            node.add_child(self.content_node())
        self.match("closeKey")
        return node

    def elif_declaration_node(self):
        node = TreeNode("<elifDeclaration>")
        self.match("elif")
        self.match("openParentheses")
        node.add_child(self.logic_expression_node())
        self.match("closeParentheses")
        self.match("openKey")
        if self.current_token and self.current_token.token_type != "closeKey":
            node.add_child(self.content_node())
        self.match("closeKey")
        return node

    def else_declaration_node(self):
        node = TreeNode("<elseDeclaration>")
        self.match("else")
        self.match("openKey")
        if self.current_token and self.current_token.token_type != "closeKey":
            node.add_child(self.content_node())
        self.match("closeKey")
        return node

    def loop_node(self):
        node = TreeNode("<loop>")
        self.match("while")
        self.match("openParentheses")
        node.add_child(self.logic_expression_node())
        self.match("closeParentheses")
        self.match("openKey")
        node.add_child(self.content_node())
        self.match("closeKey")
        return node

    def output_node(self):
        node = TreeNode("<output>")
        self.match("print")
        self.match("openParentheses")
        node.add_child(self.logic_expression_node())
        while self.current_token and self.current_token.token_type == "comma":
            self.match("comma")
            node.add_child(self.logic_expression_node())
        self.match("closeParentheses")
        self.match("end")
        return node

    def input_node(self):
        node = TreeNode("<input>")
        self.match("scanf")
        self.match("openParentheses")
        node.add_child(self.identifier_node())
        self.match("closeParentheses")
        self.match("end")
        return node

    def assignment_node(self):
        print("# CRIOU O NÓ = #")
        node = TreeNode("<assignment>")
        node.add_child(TreeNode("="))
        self.match("assignmentOperator")
        return node

    def identifier_node(self):
        print("# CRIOU UM NÓ DE ID #")
        node = TreeNode("<identifier>")
        node.add_child(TreeNode(self.current_token.value))
        self.match("identifier")
        return node

    def data_type_node(self):
        print("# CRIOU UM NÓ DE TIPO #")
        node = TreeNode("<dataType>")
        node.add_child(TreeNode(self.current_token.value))
        self.match("dataType")
        return node

    def function_indicator_node(self):
        node = TreeNode("<functionIndicator>")
        node.add_child(TreeNode(self.current_token.value))
        self.match("functionIndicator")
        return node

    def function_call_node(self):
        node = TreeNode("<functionCall>")
        node.add_child(self.identifier_node())
        self.match("openParentheses")
        if self.current_token and self.current_token.token_type != "closeParentheses":
            node.add_child(self.parameter_passing_node())
        self.match("closeParentheses")
        return node

    def parameter_passing_node(self):
        node = TreeNode("<parameterPassing>")
        node.add_child(self.logic_expression_node())
        while self.current_token and self.current_token.token_type == "comma":
            self.match("comma")
            node.add_child(self.logic_expression_node())
        return node


tokens = [
    Token("functionIndicator", "def"),
    Token("dataType", "int"),
    Token("identifier", "add"),
    Token("openParentheses", "("),
    Token("dataType", "int"),
    Token("identifier", "a"),
    Token("comma", ","),
    Token("dataType", "int"),
    Token("identifier", "b"),
    Token("closeParentheses", ")"),
    Token("openKey", "{"),
    Token("dataType", "int"),
    Token("identifier", "result"),
    Token("assignmentOperator", "="),
    Token("identifier", "a"),
    Token("arithmeticOperator", "+"),
    Token("identifier", "b"),
    Token("end", ";"),
    Token("giveBack", "return"),
    Token("identifier", "result"),
    Token("end", ";"),
    Token("closeKey", "}"),
]

def print_tree(node, level=0):
    print("  " * level + f"- {node}")
    for child in node.children:
        print_tree(child, level + 1)
parser = Parser(tokens)
root_node = parser.parse()

