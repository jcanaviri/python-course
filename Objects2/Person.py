class Father:
    def __init__(self):
        print('Father Constructor')

    def method(self):
        print('Method of Father')

class Son(Father):
    def __init__(self):
        print('Son constructor')
        super().__init__()

    def method(self):
        print('Method of Son')

# father = Father()
# father.method()
son = Son()
son.method()
