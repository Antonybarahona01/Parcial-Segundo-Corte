# main.py

from antlr4 import *
from fourierLexer import fourierLexer
from fourierParser import fourierParser
from fourierVisitor import fourierVisitor

class myVisitor(fourierVisitor):
    def __init__(self):
        self.result = None

    def visitRecta(self, ctx):
        print("La transformada de Fourier para esta función sigue la forma: Tsinc(T*w/(2π)) ")
        return 
    
    def visitTriang(self, ctx):
        print("La transformada de Fourier para esta función sigue la forma: T*sinc^2(T*w/(2π))")
        return
    
    def visitSign(self, ctx):
        print("La transformada de Fourier para esta función sigue la forma: 1/(jπf)")
        return
    
    def visitU(self, ctx):
        print("La transformada de Fourier para esta función sigue la forma: 1/(jw) + (jπf)")
        return
    
    def visitD(self, ctx):
        print("La transformada de Fourier para esta función sigue la forma: 2πδ(-w)")
        return
    
    def visitCos(self, ctx):
        print("La transformada de Fourier para esta función sigue la forma: πδ(w-w0) + πδ(w+w0)")
        return
    
    def visitSin(self, ctx):
        print("La transformada de Fourier para esta función sigue la forma: (π/j)δ(w-w0)-(π/j)δ(w-w0)")
        return
    
    def visitSum(self, ctx):
        print("La transformada de Fourier para esta función sigue la forma:  1/Ts * SUM( inf, n = -inf , 2πδ(w  -n *((2π)/Ts) ))")
        return

def main():
    input_stream = FileStream('input.txt')
    lexer = fourierLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = fourierParser(stream)
    tree = parser.prog()

    visitor = myVisitor()
    visitor.visit(tree)
    
if __name__ == '__main__':
    main()
