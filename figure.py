from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self._ancho = self._validar(ancho) or 0
        self._alto = self._validar(alto) or 0

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto
    
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'<FiguraGeometrica ({self._ancho}, {self._alto})>'
    
    def  _validar(self, value):
        return value if 0 < value < 10 else False

class Color:
    def __init__(self, color):
        self._color = color
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'<Color {self._color}>'

class Cuadrado(Color, FiguraGeometrica):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)
    
    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

cuadrado = Cuadrado(5, 'red')

# MRO Method resolution order
print(Cuadrado.mro())

rectangulo = Rectangulo(-4, 5, 'blue')

print(rectangulo)
print(rectangulo.area())

# figura = FiguraGeometrica() -> error

print(FiguraGeometrica.mro())
