my_file = open('test.txt', 'r', encoding='utf-8')
# print(my_file.read())

# Leer algunos caracteres
# print(my_file.read(5))

# Leer lineas completas
# print(my_file.readline())

# iterar un archivo
# for line in my_file.readlines():
#     print(line, end='')

# Escribir en otro archivo
my_file2 = open('test_back.txt', 'a', encoding='utf-8')
my_file2.write(my_file.read())

my_file.close()
my_file2.close()
