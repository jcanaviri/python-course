from ManageFiles import ManageFiles

with ManageFiles('test.txt') as my_file:
    print(my_file.read())
