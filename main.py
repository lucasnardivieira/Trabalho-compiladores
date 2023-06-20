import analisador_lexico
import analisador_sintatico

tokens = analisador_lexico.gera_tokens()

parser = analisador_sintatico.Parser(tokens)
parser = analisador_sintatico.Parser(tokens)
tree = parser.parse()
parser.print_tree(tree)