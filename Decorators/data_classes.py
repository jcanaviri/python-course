from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Person:
    name: str
    age: int

    count: ClassVar[int] = 0

    def __post_init__(self):
        if not self.name:
            raise ValueError('The name is empty')
        if self.age <= 0:
            raise ValueError('The age is not a valid value')

john = Person('John', 17)
print(john)
print(john.__dict__)

print(Person.count)

empty_person = Person('Aegon', 36)
print(empty_person)
