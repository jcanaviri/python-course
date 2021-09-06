from InputDevice import InputDevice

class KeyBoard(InputDevice):
    counter = 0

    def __init__(self, mark, type_input):
        KeyBoard.counter += 1
        self.keyboard_id = KeyBoard.counter
        super().__init__(mark, type_input)

    def __str__(self):
        return f'<KeyBoard {self.keyboard_id}: {self.mark} {self.type_input}>'

if __name__ == '__main__':
    keyboard1 = KeyBoard('HP', 'usb')
    keyboard2 = KeyBoard('Gamer', 'bluetooth')
    
    print(keyboard1)
    print(keyboard2)
