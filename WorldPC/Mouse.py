from InputDevice import InputDevice

class Mouse(InputDevice):
    counter = 0

    def __init__(self, mark, type_input):
        Mouse.counter += 1
        self.mouse_id = Mouse.counter
        super().__init__(mark, type_input)

    def __str__(self):
        return f'<Mouse {self.mouse_id}: {self.mark} {self.type_input}>'

if __name__ == "__main__":
    mouse = Mouse('HP', 'USB')
    mouse2 = Mouse('Acer', 'Bluetooth')

    print(mouse)
    print(mouse2)
