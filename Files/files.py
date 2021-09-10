try:
    my_file = open('test.txt', 'w', encoding='utf-8')
    my_file.write('Hello, World!!!')
except Exception as e:
    print(e)
finally:
    my_file.close()
    print('file was closed')
