result = None
a = '10'
b = 0

try:
    result = a / b
except TypeError as e:
    print(f'An error happend: {e}')
print(f'Result: {result}')
print('Continuamos...')
