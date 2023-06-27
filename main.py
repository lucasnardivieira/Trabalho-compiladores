import analisador_lexico
import analisador_sintatico

arquivo = 'teste1.mbs'

tokens = analisador_lexico.gera_tokens(arquivo)

parser = analisador_sintatico.Parser(tokens)
tree = parser.parse()
parser.print_tree(tree)