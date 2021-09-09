result = None
a = '10'
b = 0

try:
    result = a / b
except ZeroDivisionError as e:
    print(f'Zero division: An error happend: {e}')
except TypeError as e:
    print(f'Type error: An error happend: {e}')
except Exception as e:
    print(f'Exception: An error happend: {e}')

print(f'Result: {result}')
print('Continuamos...')
