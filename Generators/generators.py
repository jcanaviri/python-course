def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

for value in my_generator():
    print(value)



def num_gen():
    for num in range(1, 6):
        yield num
        print('execution')

gen = num_gen()
try:
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
except StopIteration as e:
    print(f'Error: {e}')
