import analisador_lexico 

class Token: # É preciso transformar os tokens da lista nessa estrutura para gerar a árvore
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

class Node:  # Estrutura dos nós da árvore
    def __init__(self, label):
        self.label = label
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return self.label

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens # Lista de tokens
        self.current_token = None # Token atual armazenado para comparações
        self.token_index = 0 # Índice da lista
        self.tree = None

    def parse(self):
        self.advance()
        self.tree = self.init() #Iniciando a árvore
        return self.tree

    def advance(self): # Enquanto ainda há tokens na lista, esse método apenas avança para o próximo
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
            self.token_index += 1
        else:
            self.current_token = None

    def match(self, expected_token): # Compara o token atual com o Token desejado, caso FALSE, erro sintático
        if self.current_token and self.current_token.token_type == expected_token:
            print("Token atual:" + self.current_token.token_type + "( " + self.current_token.value + " )") # Para acompanhar o estado atual
            self.advance()
        else:
            raise SyntaxError(f"Esperava '{expected_token}', mas recebi '{self.current_token.token_type}'.")

    # <init> ::= {functionDeclaration}<mainFunction>
    def init(self):
        node = Node("<init>")
        while self.current_token and self.current_token.token_type != 'TK_MAIN':
            node.add_child(self.functionDeclaration())
        node.add_child(self.mainFunction())
        return node

    # <functionDeclaration> ::= <functionIndicator><TK_IDENTIFIER><TK_OP>[<functionParameters>]<TK_CP><TK_OK>{<content>} <functionReturn><TK_CK>
    def functionDeclaration(self):
        node = Node("<functionDeclaration>")
        self.match('TK_FUNCTION')
        TK_IDENTIFIER_node = Node(f'<TK_IDENTIFIER > ({self.current_token.value})')
        TK_IDENTIFIER_node.add_child(self.current_token)
        node.add_child(TK_IDENTIFIER_node)
        self.match('TK_IDENTIFIER')
        self.match('TK_OP')
        if self.current_token and self.current_token.token_type != 'TK_CP': # Encerra parametrso quando for )
            node.add_child(self.function_parameters())
        self.match('TK_CP')
        self.match('TK_OK')
        node.add_child(self.content())
        self.match('TK_RETURN')
        self.match('TK_IDENTIFIER')
        self.match('TK_END')
        self.match('TK_CK')
        return node
    
    # <function_parameters> ::= <dataType><TK_IDENTIFIER>[<TK_COMMA><functionParameter>]
    def function_parameters(self):
        node = Node('<function_parameters>')
        node.add_child(self.current_token.token_type)
        self.match(self.current_token.token_type)
        TK_IDENTIFIER_node = Node(f'<TK_IDENTIFIER > ({self.current_token.value})')
        TK_IDENTIFIER_node.add_child(self.current_token)
        node.add_child(TK_IDENTIFIER_node)
        self.match('TK_IDENTIFIER')
        while self.current_token and self.current_token.token_type == 'TK_COMMA':
            self.match('TK_COMMA')
            node.add_child(self.function_parameters())
        return node

    # <mainFunction> ::= <main><TK_OP><TK_CP><TK_OK><content><TK_CK>
    def mainFunction(self):
        node = Node('<mainFunction>')
        self.match('TK_MAIN')
        self.match('TK_OP')
        self.match('TK_CP')
        self.match('TK_OK')
        node.add_child(self.content())
        self.match('TK_CK')
        return node

    # <content> ::= <variableDeclaration> | <output> | <input> | <selectionStructure> | <loop>
    def content(self):
        node = Node('<content>')
        print(self.current_token.token_type)
        while self.current_token and self.current_token.token_type in ['TK_DT_INTEGER', 'TK_DT_CHAR', 'TK_STRING', 'TK_DT_FLOAT', 'TK_PRINT', 'TK_SCANF', 'TK_IF', 'TK_WHILE']:
            if self.current_token.token_type in ['TK_DT_INTEGER', 'TK_DT_CHAR', 'TK_STRING']:
                node.add_child(self.variableDeclaration())
            elif self.current_token.token_type == 'TK_PRINT':
                node.add_child(self.output())
            elif self.current_token.token_type == 'TK_SCANF':
                node.add_child(self.input())
            elif self.current_token.token_type == 'TK_IF':
                node.add_child(self.selectionStructure())
            elif self.current_token.token_type == 'TK_WHILE':
                node.add_child(self.loop())
            elif self.current_token.token_type == 'identifier':
                node.add_child(self.functionCall())
        return node

    # <variableDeclaration> ::= <dataType><TK_IDENTIFIER><TK_END> | <dataType><TK_IDENTIFI><assignment><logicExpression><TK_END>
    def variableDeclaration(self):
        node = Node(f'<variableDeclaration> ({self.current_token.value})')
        self.match(self.current_token.token_type)
        TK_IDENTIFIER_node = Node(f'<TK_IDENTIFIER > ({self.current_token.value})')
        TK_IDENTIFIER_node.add_child(self.current_token)
        node.add_child(TK_IDENTIFIER_node)
        self.match('TK_IDENTIFIER')
        if self.current_token and self.current_token.token_type == "TK_ASSIGNMENT":
            node.add_child(self.assignment_node())
            node.add_child(self.logicExpression())
            
        self.match('TK_END')
        return node
    
    # =
    def assignment_node(self):
        node = Node(f'<assignment> ({self.current_token.value})')
        self.match("TK_ASSIGNMENT")
        return node
    
    # <output> ::= <TK_PRINT><TK_OP><logicExpression>{<TK_COMMA><logicExpression>} <TK_CP><TK_END>
    def output(self):
        node = Node('<output>')
        self.match('TK_PRINT')
        self.match('TK_OP')
        node.add_child(self.logicExpression())
        while self.current_token and self.current_token.token_type == 'TK_COMMA':
            self.match('TK_COMMA')
            node.add_child(self.logicExpression())
        self.match('TK_CP')
        self.match('TK_END')
        return node
    
    # <input> ::= <TK_SCANF><TK_OP><TK_IDENTIFIER><TK_CP><TK_END>
    def input(self):
        node = Node('<input>')
        self.match('TK_SCANF')
        self.match('TK_OP')
        TK_IDENTIFIER_node = Node(f'<TK_IDENTIFIER > ({self.current_token.value})')
        TK_IDENTIFIER_node.add_child(self.current_token)
        node.add_child(TK_IDENTIFIER_node)
        self.match('TK_IDENTIFIER')
        self.match('TK_CP')
        self.match('TK_END')
        return node
    
    #################################################################################################
    ### OS MÉTODOS SEGUINTES TRABALHAM EM CONJUNTO PARA DEFINIÇÃO GERAL DE todo TIPO DE EXPRESSÃO ###
    #################################################################################################
    # <logicExpression> ::= <expression> {(<or>| <and>| <TK_MATH_ADD>| subtraction |<multiplication>| <division>) <expression>}
    def logicExpression(self):
        node = Node(f'<logicExpression> ({self.current_token.value})')
        node.add_child(self.expression())
        while self.current_token and self.current_token.token_type in ['or', 'and', 'TK_MATH_ADD', 'subtraction', 'multiplication', 'division']:
            operator_node = Node(f'<operator> ({self.current_token.value})')
            operator_node.add_child(self.current_token)
            node.add_child(operator_node)
            self.advance()
            node.add_child(self.expression())
        return node

    # <expression> ::= <relation> {(<lessThan> | <lessThanOrEqual> | <TK_LOGIC_GT> | <TK_LOGIC_GTOrEqual> | <equal> | <notEqual>) <relation>}
    def expression(self):
        node = Node('<expression>')
        if self.current_token and self.current_token.token_type == 'TK_IDENTIFIER':
            if self.tokens[self.token_index].token_type == 'TK_OP':
                node.add_child(self.functionCall())
                return node
        node.add_child(self.relation())
        while self.current_token and self.current_token.token_type in ['TK_LOGIC_LT', 'TK_LOGIC_LTE', 'TK_LOGIC_GT', 'TK_LOGIC_GTOrEqual', 'TK_LOGIC_EQ', 'TK_LOGIC_DIF']:
            operator_node = Node(f'<operator> ({self.current_token.value})')
            operator_node.add_child(self.current_token)
            node.add_child(operator_node)
            self.advance()
            node.add_child(self.relation())
        return node

    # <relation> ::= <TK_OP><logicExpression><TK_CP>|<mathExpression>
    def relation(self):
        node = Node('<relation>')
        if self.current_token and self.current_token.token_type == 'TK_OP':
            self.match('TK_OP')
            node.add_child(self.logicExpression())
            self.match('TK_CP')
        else:
            node.add_child(self.mathExpression())
        return node
    
    # <mathExpression> ::= [<TK_MATH_ADD>| <subtraction>] <term> {(<TK_MATH_ADD>| <subtraction>) <term>}
    def mathExpression(self):
        node = Node('<mathExpression>')
        if self.current_token and self.current_token.token_type in ['TK_MATH_ADD', 'subtraction']:
            operator_node = Node(f'<operator> ({self.current_token.value})')
            operator_node.add_child(self.current_token)
            node.add_child(operator_node)
            self.advance()
        node.add_child(self.term())
        while self.current_token and self.current_token.token_type in ['TK_MATH_ADD', 'subtraction']:
            operator_node = Node(f'<operator> ({self.current_token.value})')
            operator_node.add_child(self.current_token)
            node.add_child(operator_node)
            self.advance()
            node.add_child(self.term())
        return node

    # <term> ::= <factor>{(<multipliation>| <division>) [<TK_MATH_ADD>|<subtraction>] <factor>}
    def term(self):
        node = Node('<term>')
        node.add_child(self.factor())
        while self.current_token and self.current_token.token_type in ['multiplication', 'division']:
            operator_node = Node(f'<operator> ({self.current_token.value})')
            operator_node.add_child(self.current_token)
            node.add_child(operator_node)
            self.advance()
            node.add_child(self.factor())
        return node

    # <factor> ::= <TK_OP><mathExpression><TK_CP>|<TK_IDENTIFIER>| <real>| <integer>| <TK_STRING>
    def factor(self):
        node = Node(f'<factor> ({self.current_token.value})')
        if self.current_token and self.current_token.token_type == 'TK_OP':
            self.match('TK_OP')
            node.add_child(self.mathExpression())
            self.match('TK_CP')
        else:
            node.add_child(self.current_token)
            self.advance()
        return node
    
    #################################################################################################
    #################################################################################################

    # <selectionStructure> ::= <ifDeclaration>{<elifDeclaration>} [<elseDeclaration>]
    def selectionStructure(self):
        node = Node('<selectionStructure>')
        node.add_child(self.ifDeclaration())
        while self.current_token and self.current_token.token_type == 'TK_ELIF':
            node.add_child(self.elifDeclaration())
        if self.current_token and self.current_token.token_type == 'TK_ELSE':
            node.add_child(self.elseDeclaration())
        return node

    # <ifDeclaration> ::= <TK_IF ><TK_OP><logicExpression><TK_CP><TK_OK><content><TK_CK>
    def ifDeclaration(self):
        node = Node('<ifDeclaration>')
        self.match('TK_IF')
        self.match('TK_OP')
        node.add_child(self.logicExpression())
        self.match('TK_CP')
        self.match('TK_OK')
        node.add_child(self.content())
        self.match('TK_CK')
        return node

    # <elifDeclaration> ::= <rwElif><TK_OP><logicExpression><TK_CP><TK_OK> [<content>] <TK_CK>
    def elifDeclaration(self):
        node = Node('<elifDeclaration>')
        self.match('rwElif')
        self.match('TK_OP')
        node.add_child(self.logicExpression())
        self.match('TK_CP')
        self.match('TK_OK')
        node.add_child(self.content())
        self.match('TK_CK')
        return node

    # <elseDeclaration> ::= <TK_ELSE><TK_OK> [<content>] <TK_CK>
    def elseDeclaration(self):
        node = Node('<elseDeclaration>')
        self.match('TK_ELSE')
        self.match('TK_OK')
        node.add_child(self.content())
        self.match('TK_CK')
        return node
    
    # <loop> ::= <TK_WHILE><TK_OP><logicExpression><TK_CP><TK_OK><content><TK_CK>
    def loop(self):
        node = Node('<loop>')
        self.match('TK_WHILE')
        self.match('TK_OP')
        node.add_child(self.logicExpression())
        self.match('TK_CP')
        self.match('TK_OK')
        node.add_child(self.content())
        self.match('TK_CK')
        return node
    
    # <functionCall> ::= <identifier><openParentheses>[<parameterPassing>]<closeParentheses>
    def functionCall(self):
        node = Node('<functionCall>')
        identifier_node = Node(f'<TK_IDENTIFIER> ({self.current_token.value})')
        identifier_node.add_child(self.current_token)
        node.add_child(identifier_node)
        self.match('TK_IDENTIFIER')
        self.match('TK_OP')
        if self.current_token and self.current_token.token_type != 'TK_CP':
            node.add_child(self.parameterPassing())
        self.match('TK_CP')
        self.match('TK_END')
        return node
    
    # <parameterPassing> ::= <logicExpression>{<comma><logicExpression>}
    def parameterPassing(self):
        node = Node('<parameterPassing>')
        node.add_child(self.logicExpression())
        while self.current_token and self.current_token.token_type == 'comma':
            self.match('comma')
            node.add_child(self.logicExpression())
        return node

    def print_tree(self, node, indent=''):
        print(indent + str(node))
        if hasattr(node, 'children'):
            for child in node.children:
                self.print_tree(child, indent + '  ')


tokens = analisador_lexico.gera_tokens()

parser = Parser(tokens)
tree = parser.parse()
parser.print_tree(tree)
