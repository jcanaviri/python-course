from KeyBoard import KeyBoard
from Mouse import Mouse
from Display import Display

class Computer:
    counter = 0

    def __init__(self, name, display, keyboard, mouse):
        Computer.counter += 1
        self.computer_id = Computer.counter
        self.name = name
        self.display = display
        self.keyboard = keyboard
        self.mouse = mouse
    
    def __str__(self):
        return f'''<Computer 
        {self.computer_id}: {self.name} 
        Display: {self.display} 
        KeyBoard: {self.keyboard}
        Mouse: {self.mouse} >'''

if __name__ == '__main__':
    keyboard = KeyBoard('HP', 'USB')
    mouse = Mouse('HP', 'USB')
    display = Display('HP', 200)

    computer = Computer('DELL', display, keyboard, mouse)
    print(computer)
        