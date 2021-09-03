class Arimethic:
    """Make the operations of add, rest"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def subs(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


arithm1 = Arimethic(2, 4)
print(f'Add: {arithm1.add()}')
print(f'Subs: {arithm1.subs()}')
print(f'Subs: {arithm1.multiplication()}')
print(f'Subs: {arithm1.division():.2f}')
