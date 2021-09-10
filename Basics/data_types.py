# The types means nothing to python
# it is just a hint for us
x = 10
print(type(x))

y = 'this is a string'
print(type(y))

z = True
print(type(z))

# Floating
x = 2.54
print(type(x))

# String concatenation
band = 'My chemical romance'

print('I use to hear ' + band)
print('I use to hear', band)
print('I use to hear %s' % band)
print(f'I use to hear {band}')

is_valid = False
print(is_valid)

is_greater = 11 > 5
print(is_greater)

name = input('Tell me your name: ')

print(f'Hi, {name}!')

# Score the day
question = input('How was your day? (1..10)')
print(f'My day was: {question}')
