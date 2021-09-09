result = None
a = '10'
b = 0

try:
    result = a / b
except ZeroDivisionError as e:
    print(f'An error happend: {e}')
print(f'Result: {result}')
print('Continuamos...')
