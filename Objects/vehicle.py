class Vehiculo():
    """Vehiculo (Clase Padre)"""
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'<Vehiculo {self.color}>'


class Coche(Vehiculo):
    """Coche  (Clase Hija de Vehículo)"""
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'<Coche {self.velocidad}>'


class Bicicleta(Vehiculo):
    """Bicicleta  (Clase Hija de Vehículo)"""
    def __init__(self, color, ruedas, velocidad, tipo):
        super().__init__(color, ruedas, velocidad)
        self.tipo = tipo

    def __str__(self):
        return f'<Bicicleta {self.tipo}>'
