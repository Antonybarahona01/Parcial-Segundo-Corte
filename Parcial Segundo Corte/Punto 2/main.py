from antlr4 import *
from FuncionesLexer import FuncionesLexer
from FuncionesParser import FuncionesParser
from FuncionesVisitor import FuncionesVisitor

class miVisitor(FuncionesVisitor):
    def __init__(self):
        self.resultado = None

    def visitFilterFunction(self, ctx):
        nombre_funcion = ctx.expression().getText()
        nombre_funcion = "lambda x: " + nombre_funcion
        
        elementos_iterables = ctx.iterable().getText()
        elementos_iterables = list(elementos_iterables[1:-1].split(','))

        if elementos_iterables[0].isdigit():
            elementos_iterables = list(map(int, elementos_iterables))
        
        resultado = list(filter(eval(nombre_funcion), elementos_iterables))
        print(f"Resultado de filter: {resultado}")  # Mostramos el resultado
        return resultado

    def visitMapFunction(self, ctx):
        nombre_funcion = ctx.opcion().getText()
        nombre_funcion = "lambda x: " + nombre_funcion
        
        elementos_iterables = ctx.iterable().getText()
        elementos_iterables = list(elementos_iterables[1:-1].split(','))
        elementos_iterables = [elem.strip(' "') if elem.startswith('"') else elem for elem in elementos_iterables]

        if elementos_iterables[0].isdigit():
            elementos_iterables = list(map(int, elementos_iterables))

        resultado = list(map(eval(nombre_funcion), elementos_iterables))
        print(f"Resultado de map: {resultado}")  # Mostramos el resultado
        return resultado

def main():
    input_stream = FileStream('input.txt')
    lexer = FuncionesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FuncionesParser(stream)
    tree = parser.prog()
    visitor = miVisitor()
    resultado = visitor.visit(tree)

if __name__ == '__main__':
    main()
