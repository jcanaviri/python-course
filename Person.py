class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

me = Person('Josue', 'Canaviri', 23)
you = Person('John', 'Doe', 36)

print(f'The object {me.name} {me.last_name} - {me.age}')
print(f'The object {you.name} {you.last_name} - {you.age}')
