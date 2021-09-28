def A():
    variable1 = 42
    def B():
        variable2 = 24
        nonlocal variable1
        variable1 = 'new value'
    B()
    print(f'variable1 = {variable1}')
# A()

counter = 0
def show_counter():
    print(counter)

def change_counter(c):
    global counter
    counter = c
change_counter(4)
show_counter()

# Functions are first class citizens
def add(a, b):
    return a + b
# 1.- set a variable
foo = add
print(foo)
print(type(foo))

# execute that function
result = foo(5, 8)
print(result)

# 2.- foo as an argument
def operation(a, b, foo):
    print(foo(a, b))

operation(3, 2, add)

# 3.- Return a foo
def get_foo():
    return add

foo = get_foo()
print(foo(2, 2))
