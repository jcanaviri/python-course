class Display:
    counter = 0
    
    def __init__(self, mark, size):
        Display.counter += 1
        self.display_id = Display.counter
        self.mark = mark
        self.size = size

    def __str__(self):
        return f'<Display {self.display_id} {self.mark} {self.size}>'

if __name__ == '__main__':
    display1 = Display('HP', 15)
    display2 = Display('Acer', 16)
    
    print(display1)
    print(display2)
