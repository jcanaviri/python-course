class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

class Color:
    def __init__(self, color):
        self.color = color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.ancho * self.alto

cuadrado = Cuadrado(5, 'red')

print(cuadrado.area())
