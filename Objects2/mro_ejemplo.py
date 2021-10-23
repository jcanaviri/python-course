class Class1:
    def __init__(self):
        print('Class1.__init__')

    def method(self):
        print('Method of Class1')


class Class2(Class1):
    def __init__(self):
        print('Class2.__init__')
        super().__init__()

    def method(self):
        print('Method of Class2')
        super().method()


class Class3(Class1):
    def __init__(self):
        print('Class3.__init__')
        super().__init__()

    def method(self):
        print('Method of Class3')
        super().method()


class Class4(Class2, Class3):
    def method(self):
        print('Method of Class4')
        super().method()

# Test
class4 = Class4()
print(Class4.__bases__)
print(Class4.__mro__)

class4.method()
