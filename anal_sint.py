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
# REGRA init
# <init> ::= {<functionDeclaration>} <mainFunction>
root = TreeNode("<init>")

# REGRA main_function
# <mainFunction> ::= <main><openParentheses><closeParentheses><openKey>{<content>} <closeKey>
main_function = TreeNode("<mainFunction>")
main = TreeNode("<main>")
open_parentheses = TreeNode("<openParenthesis>")
close_parentheses = TreeNode("<closeParenthesis>")
open_key = TreeNode("<openKey>")
content = TreeNode("<content>")
close_key = TreeNode("<closeKey>")

# REGRA function_declaration
# <functionDeclaration> ::= <functionIndicator><dataType><identifier><openParentheses>[<functionParameters>]<closeParentheses><openKey>{<content>} <functionReturn><closeKey>
function_declaration = TreeNode("<functionDeclaration>")
function_indicator = TreeNode("<functionIndicator>")
data_type = TreeNode("<dataType>")
identifier = TreeNode("<identifier>")
open_parentheses = TreeNode("<openParentheses>")
function_parameters = TreeNode("<functionParameters>")
close_parentheses = TreeNode("<closeParentheses>")
open_key = TreeNode("<openKey>")
content = TreeNode("<content>")
function_return = TreeNode("<functionReturn>")
close_key = TreeNode("<closeKey>")

# REGRA content
# <content> ::= <variableDeclaration>| <selectionStructure>| <loop>|<output>| <input>
variable_declaration = TreeNode("<variableDeclaration>")
selection_structure = TreeNode("<selectionStructure>")
loop = TreeNode("<loop>")
output = TreeNode("<output>")
input_node = TreeNode("<input>")

# REGRA function_parameters
# function_parameters> ::= <dataType><identifier>[<comma><functionParameter>]
function_parameters = TreeNode("<functionParameters>")
data_type = TreeNode("<dataType>")
identifier = TreeNode("<identifier>")
comma = TreeNode("<comma>")
function_parameters = TreeNode("<functionParameters>")

# REGRA functionReturn
# function_return> ::= <giveBack><logicExpression><end>
function_return = TreeNode("<function_return>")
give_back = TreeNode("<giveBack>")
logic_expression = TreeNode("<logicExpression>")
end = TreeNode("<end>")

# REGRA variableDeclaration
# <variableDeclaration> ::= <dataType><identifier><end>|<dataType><identifier>
# <assignment><logicExpression><end>
variable_declaration = TreeNode("<variableDeclaration>")
data_type = TreeNode("<dataType>")
identifier = TreeNode("<identifier>")
end = TreeNode("<end>")
assignment = TreeNode("<assignment>")
logic_expression = TreeNode("<logicExpression>")

# REGRA mathExpression
# <mathExpression> ::= [<addition>| <subtraction>] <term>{(<addition>| <subtraction>) <term>}
math_expression = TreeNode("<mathExpression>")
addition = TreeNode("<addition>")
subtraction = TreeNode("<subtraction>")
term = TreeNode("<term>")

# REGRA term
# <term> ::= <factor>{(<multipliation>| <division>) [<addition>|<subtraction>] <factor>}
term = TreeNode("<term>")
factor = TreeNode("<factor>")
multiplication = TreeNode("<multiplication>")
division = TreeNode("<division>")
addition = TreeNode("<addition>")
subtraction = TreeNode("<subtraction>")

# REGRA factor
# <factor> ::= <openParentheses><mathExpression><closeParentheses>|<identifier>| <real>| <integer>| <string>| <functionCall>
factor = TreeNode("<factor>")
open_parentheses = TreeNode("<openParentheses>")
math_expression = TreeNode("<mathExpression>")
close_parentheses = TreeNode("<closeParentheses>")
identifier = TreeNode("<identifier>")
real = TreeNode("<real>")
integer = TreeNode("<integer>")
string = TreeNode("<string>")
function_call = TreeNode("<functionCall>")

# REGRA logicalExpression
# <logicalExpression> ::= <expression>{(<or>| <and>| <addition>| subtraction |<multiplication>| <division>) <expression>}
logical_expression = TreeNode("<logicalExpression>")
expression = TreeNode("<expression>")
or_operator = TreeNode("<or>")
and_operator = TreeNode("<and>")
addition = TreeNode("<addition>")
subtraction = TreeNode("<subtraction>")
multiplication = TreeNode("<multiplication>")
division = TreeNode("<division>")

# REGRA expression
# <expression> ::= <relation>{(<lessThan>| <lessThanOrEqual>| <greaterThan>| <greaterThanOrEqual>| <equal>| <notEqual>) <relation>}
expression = TreeNode("<expression>")
relation = TreeNode("<relation>")
less_than = TreeNode("<lessThan>")
less_than_or_equal = TreeNode("<lessThanOrEqual>")
greater_than = TreeNode("<greaterThan>")
greater_than_or_equal = TreeNode("<greaterThanOrEqual>")
equal = TreeNode("<equal>")
not_equal = TreeNode("<notEqual>")

# REGRA relation
# <relation> ::= <openParentheses><logicExpression><closeParentheses>|<mathExpression>
relation = TreeNode("<relation>")
open_parentheses = TreeNode("<openParentheses>")
logic_expression = TreeNode("<logicExpression>")
close_parentheses = TreeNode("<closeParentheses>")
math_expression = TreeNode("<mathExpression>")

# REGRA selectionStructure
# <selectionStructure> ::= <ifDeclaration>{<elifDeclaration>} [<elseDeclaration>]
selection_structure = TreeNode("<selectionStructure>")
if_declaration = TreeNode("<ifDeclaration>")
elif_declaration = TreeNode("<elifDeclaration>")
else_declaration = TreeNode("<elseDeclaration>")

# REGRA if
# <ifDeclaration> ::= <rwIf><op><logicExpression><cp><ok>[<content>] <ck>
if_declaration = TreeNode("<ifDeclaration>")
rw_if = TreeNode("<rwIf>")
op = TreeNode("<op>")
logic_expression = TreeNode("<logicExpression>")
cp = TreeNode("<cp>")
ok = TreeNode("<ok>")
content = TreeNode("<content>")
ck = TreeNode("<ck>")

# REGRA elif
# <elifDeclaration> ::= <rwElseIf><op><logicExpression><cp><ok>[<content>] <ck>
elif_declaration = TreeNode("<elifDeclaration>")
rw_else_if = TreeNode("<rwElseIf>")
op = TreeNode("<op>")
logic_expression = TreeNode("<logicExpression>")
cp = TreeNode("<cp>")
ok = TreeNode("<ok>")
content = TreeNode("<content>")
ck = TreeNode("<ck>")

# REGRA else
# <elseDeclaration> ::= <rwElse><ok>[<content>] <ck>
else_declaration = TreeNode("<elseDeclaration>")
rw_else = TreeNode("<rwElse>")
ok = TreeNode("<ok>")
content = TreeNode("<content>")
ck = TreeNode("<ck>")

# REGRA loop
# <loop> ::= <rwWhile><op><logicExpression><cp><ok><content><ck>
loop = TreeNode("<loop>")
rw_while = TreeNode("<rwWhile>")
op = TreeNode("<op>")
logic_expression = TreeNode("<logicExpression>")
cp = TreeNode("<cp>")
ok = TreeNode("<ok>")
content = TreeNode("<content>")
ck = TreeNode("<ck>")

# REGRA output
# <output> ::= <rwPrint><op><logicExpression>{<comma><logicExpression>} <cp><end>
output = TreeNode("<output>")
rw_print = TreeNode("<rwPrint>")
op = TreeNode("<op>")
logic_expression = TreeNode("<logicExpression>")
comma = TreeNode("<comma>")
cp = TreeNode("<cp>")
end = TreeNode("<end>")

# REGRA input
# <input> ::= <rwScanf><op><identifier><cp><end>
input_declaration = TreeNode("<input>")
rw_scanf = TreeNode("<rwScanf>")
op = TreeNode("<op>")
identifier = TreeNode("<identifier>")
cp = TreeNode("<cp>")
end = TreeNode("<end>")

# REGRA valueToVar
# <valueToVariable> ::= <identifier><assignment><logicExpression><end>
value_to_variable = TreeNode("<valueToVariable>")
identifier = TreeNode("<identifier>")
assignment = TreeNode("<assignment>")
logic_expression = TreeNode("<logicExpression>")
end = TreeNode("<end>")

# REGRA functionCall
# <functionCall> ::= <identifier><openParentheses>[<parameterPassing>]<closeParentheses>
function_call = TreeNode("<functionCall>")
identifier = TreeNode("<identifier>")
open_parentheses = TreeNode("<openParentheses>")
parameter_passing = TreeNode("<parameterPassing>")
close_parentheses = TreeNode("<closeParentheses>")

# REGRA parameterPassing
# <parameterPassing> ::= <logicExpression>{<comma><logicExpression>}
parameter_passing = TreeNode("<parameterPassing>")
logic_expression = TreeNode("<logicExpression>")
comma = TreeNode("<comma>")


## EXEMPLO CRIANDO UMA ÁRVORE ##
root.add_child(function_declaration)
root.add_child(main_function)

main_function.add_child(main)
main_function.add_child(open_parentheses)
main_function.add_child(close_parentheses)
main_function.add_child(open_key)
main_function.add_child(content)
main_function.add_child(close_key)

function_indicator.add_child(data_type)
function_indicator.add_child(identifier)
function_indicator.add_child(open_parentheses)
function_indicator.add_child(function_parameters)
function_indicator.add_child(close_parentheses)
function_indicator.add_child(open_key)
function_indicator.add_child(content)
function_indicator.add_child(function_return)
function_indicator.add_child(close_key)

content.add_child(variable_declaration)
content.add_child(selection_structure)
content.add_child(loop)
content.add_child(output)
content.add_child(input_node)

def print_tree(node, level=0):
    print("  " * level + str(node))
    for child in node.children:
        print_tree(child, level + 1)

print_tree(root)
