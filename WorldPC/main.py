from KeyBoard import KeyBoard
from Mouse import Mouse
from Display import Display
from Computer import Computer

from Order import Order

keyboard1 = KeyBoard('HP', 'USB')
mouse1 = Mouse('HP', 'USB')
display1 = Display('HP', 200)

computer1 = Computer('DELL', display1, keyboard1, mouse1)

keyboard2 = KeyBoard('HP', 'USB')
mouse2 = Mouse('HP', 'USB')
display2 = Display('HP', 200)

computer2 = Computer('DELL', display2, keyboard2, mouse2)

computers = [computer1, computer2]

order = Order(computers)
print(order)

keyboard3 = KeyBoard('HP', 'USB')
mouse3 = Mouse('HP', 'USB')
display3 = Display('HP', 200)

computer3 = Computer('DELL', display3, keyboard3, mouse3)

order.add_computer(computer3)
print(order)
