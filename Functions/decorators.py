def decorator(foo_a):
    def foo_b(*args, **kwargs):
        print('This happens before')
        foo_a(*args, **kwargs)
        print('This happens after')
    return foo_b

@decorator
def say_hello():
    print('Hello world')

say_hello()

print()

@decorator
def add(a, b):
    print(a + b)

add(2, 3)
