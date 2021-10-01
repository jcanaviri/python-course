mulp = (i * i for i in range(4))
print(mulp)
print(type(mulp))

print(next(mulp))
print(next(mulp))


names = ['John', 'Susan']
gen = (val for val in names)

print(next(gen))
print(next(gen))
