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

root = TreeNode("<init>")

# REGRA main_function
main_function = TreeNode("<mainFunction>")
main = TreeNode("<main>")
open_parentheses = TreeNode("<openParenthesis>")
close_parentheses = TreeNode("<closeParenthesis>")
open_key = TreeNode("<openKey>")
content = TreeNode("<content>")
close_key = TreeNode("<closeKey>")

# REGRA function_declaration
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
variable_declaration = TreeNode("<variableDeclaration>")
selection_structure = TreeNode("<selectionStructure>")
loop = TreeNode("<loop>")
output = TreeNode("<output>")
input_node = TreeNode("<input>")

# REGRA function_parameters
<dataType><identifier>[<comma><functionParameter>]

# REGRA functionReturn
<giveBack><logicExpression><end>

# REGRA variableDeclaration
<dataType><identifier><end>|<dataType><identifier>
<assignment><logicExpression><end>

# REGRA mathExpression
[<addition>| <subtraction>] <term>{(<addition>| <subtraction>) <term>}

# REGRA term
<factor>{(<multipliation>| <division>) [<addition>|
<subtraction>] <factor>}

# REGRA factor
<openParentheses><mathExpression><closeParentheses>|
<identifier>| <real>| <integer>| <string>| <functionCall>

# REGRA logicalExpression
<expression>{(<or>| <and>| <addition>| subtraction |
<multiplication>| <division>) <expression>}

# REGRA expression
<relation>{(<lessThan>| <lessThanOrEqual>| <greaterThan>| <greaterThanOrEqual>| <equal>| <notEqual>) <relation>}

# REGRA relation
<openParentheses><logicExpression><closeParentheses>|
<mathExpression>

# REGRA selectionStructure
<selectionStructure> ::= <ifDeclaration>{<elifDeclaration>} [<elseDeclaration>]

# REGRA if
<ifDeclaration> ::= <rwIf><op><logicExpression><cp><ok>
[<content>] <ck>

# REGRA elif
<elifDeclaration> ::= <rwElseIf><op><logicExpression><cp><ok>
[<content>] <ck>

# REGRA else
<elseDeclaration> ::= <rwElse><ok>[<content>] <ck>

# REGRA loop
<loop> ::= <rwWhile><op><logicExpression><cp><ok>
<content><ck>

# REGRA output
<output> ::= <rwPrint><op><logicExpression>
{<comma><logicExpression>} <cp><end>

# REGRA input
<input> ::= <rwScanf><op><identifier><cp><end>

# REGRA valueToVar
<valueToVariable> ::= <identifier><assignment><logicExpression><end>

# REGRA functionCall
<functionCall> ::= <identifier><openParentheses>[<parameterPassing>]
<closeParentheses>

# REGRA parameterPassing
<parameterPassing> ::= <logicExpression>{<comma><logicExpression>}



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
