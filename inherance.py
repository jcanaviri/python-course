class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Employee(Person):
    def __init__(self, name, age, salary):
        super(Employee, self).__init__(name, age)
        self.salary = salary

    def __str__(self):
        return f'<Employee {self.name}>'

employee = Employee('John', 23, 500)
print(employee)
