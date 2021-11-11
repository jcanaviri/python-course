foo = lambda a, b: a + b
print(foo(4, 5))

foo = lambda: 'Lambda foo'
print(foo())

double = lambda x: 2 * x
print(double(7))

factor = lambda x, mulp=2: mulp * x
print(factor(2))
print(factor(2, 4))
print(factor(2, 9))

add_all = lambda *args: sum(args)
print(add_all(1, 2, 3))
print(add_all(1, 2, 3, 4, 5, 6, 7, 8 ,9, 10))
