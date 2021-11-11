def foo1(a, b):
    def foo2():
        return a + b
    return foo2

def foo(a, b):
    return lambda: a + b

print(foo(2, 3)())
result = foo(2, 3)
print(result())
