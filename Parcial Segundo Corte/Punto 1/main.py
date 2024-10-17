from antlr4 import *
from OperacionesComplejasLexer import OperacionesComplejasLexer
from OperacionesComplejasParser import OperacionesComplejasParser
from OperacionesComplejasVisitor import OperacionesComplejasVisitor

class myVisitor(OperacionesComplejasVisitor):
    def __init__(self):
        self.result = None

    def visitOperar(self, ctx):
        left = self.visit(ctx.complexNumber(0))
        right = self.visit(ctx.complexNumber(1))
        op = ctx.op.type

        if op == OperacionesComplejasParser.ADD:
            self.result = (left[0] + right[0], left[1] + right[1])
            sig = " + " if self.result[1] >= 0 else " "
            result = f"{round(self.result[0], 2)}{sig}{round(self.result[1], 2)}j"
            print("El resultado de la operación es:", result)
            return self.result

        elif op == OperacionesComplejasParser.SUB:
            self.result = (left[0] - right[0], left[1] - right[1])
            sig = " + " if self.result[1] >= 0 else " "
            result = f"{round(self.result[0], 2)}{sig}{round(self.result[1], 2)}j"
            print("El resultado de la operación es:", result)
            return self.result

        elif op == OperacionesComplejasParser.MUL:
            self.result = ((left[0] * right[0]) - (left[1] * right[1]), (left[0] * right[1]) + (left[1] * right[0]))
            sig = " + " if self.result[1] >= 0 else " "
            result = f"{round(self.result[0], 2)}{sig}{round(self.result[1], 2)}j"
            print("El resultado de la operación es:", result)
            return self.result

        elif op == OperacionesComplejasParser.DIV:
            denominator = right[0]**2 + right[1]**2
            self.result = ((left[0] * right[0] + left[1] * right[1]) / denominator, (left[1] * right[0] - left[0] * right[1]) / denominator)
            sig = " + " if self.result[1] >= 0 else " "
            result = f"{round(self.result[0], 2)}{sig}{round(self.result[1], 2)}j"
            print("El resultado de la operación es:", result)
            return self.result

    def visitDefComplex(self, ctx):
        real = self.visit(ctx.realPart())
        imaginary = self.visit(ctx.imaginaryPart())
        sign = 1 if ctx.op.type == OperacionesComplejasParser.ADD else -1
        return (real, sign * imaginary)

    def visitPrint(self, ctx):
        val = self.visit(ctx.operation())
        return val

    def visitReal(self, ctx):
        return int(ctx.NUMBER().getText())

    def visitImg(self, ctx):
        return int(ctx.NUMBER().getText())

def main():
    input_stream = FileStream('input.txt')
    lexer = OperacionesComplejasLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OperacionesComplejasParser(stream)
    tree = parser.prog()

    visitor = myVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
