a = 3
b = 2

addition = a + b
substraction = a - b
multiplication = a * b
division = a // b
module = 3 % 2
exponent = 3 ** 2

assert addition == 5
assert substraction == 1
assert multiplication == 6
assert division == 1
assert module == 1
assert exponent == 9

# Asingment
span = 12

span += 1
assert span == 13

span -= 7
assert span == 6

span *= 2
assert span == 12

span /= 4
assert span == 3

a, b = 4, 2

assert not a == b
assert a != b
assert a > b
assert a >= b
assert not a < b
assert not a <= b


def is_even():
    number = int(input('Write a number: '))

    if number % 2 == 0:
        print('Is even')
    else:
        print('Is odd')

def is_in_range():
    age = int(input('Write a number: '))
    
    if age >= 20 and age <= 40:
        print('Inside the range')
    else:
        print('Outside the range')

def is_greater():
    num1 = int(input('Proporciona el numero1: '))
    num2 = int(input('Proporciona el numero1: '))

    if num1 > num2:
        print(f'El mayor es: {num1}')
    else:
        print(f'El mayor es: {num2}')
