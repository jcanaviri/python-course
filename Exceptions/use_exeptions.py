result = None

try:
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    result = a / b
except ZeroDivisionError as e:
    print(f'Zero division: {e} {type(e)}')
except TypeError as e:
    print(f'Type error: {e} {type(e)}')
except Exception as e:
    print(f'Exception: {e} {type(e)}')
else:
    print('Everything is OK')
finally:
    print('Finally')

print(f'Result: {result}')
print('Continuamos...')
