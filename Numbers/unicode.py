print('Hello\u0020World')

print('Notacion simple: \u0041')
print('Notacion extendida: \U00000041')
print('Notacion hexagecimal: \x41')

print('Heart \u2665')
print('Smile \U0001f600')
print('Snake \U0001f40d')

character = chr(64)
print(character)

# Conversion
string = 'Español'
print(f'Original: {string}')
str_bytes = string.encode('utf-8')
print(f'Codificado: {str_bytes}')

bytes_str = str_bytes.decode('utf-8')
print(f'Decodificado {bytes_str}')
