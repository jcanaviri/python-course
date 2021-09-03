class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

base = int(input('Write the base: '))
height = int(input('Write the height: '))

rectangle = Rectangle(base, height)

print(f'The area is: {rectangle.area()}')
