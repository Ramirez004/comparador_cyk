
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
import time


expresion = "+".join(str(i) for i in range(1, 50))

entrada = InputStream(expresion)

lexer = ExprLexer(entrada)
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)

inicio = time.time()

tree = parser.prog()

fin = time.time()

print("Expresión:", expresion)
print(tree.toStringTree(recog=parser))
print("Tiempo ANTLR:", fin - inicio)
