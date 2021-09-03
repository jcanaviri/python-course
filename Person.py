class Person:
    def __init__(self, name, last_name, age):
        self._name = name
        self.last_name = last_name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def show_detail(self):
        print(f'Person {self.name} {self.last_name}')


if __name__ == '__main__':
    me = Person('Josue', 'Canaviri', 23)
    you = Person('John', 'Doe', 36)

    print(f'The object {me.name} {me.last_name} - {me.age}')
    print(f'The object {you.name} {you.last_name} - {you.age}')

    me.show_detail()
    you.show_detail()

    Person.show_detail(me)

