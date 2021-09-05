class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary    

    def __str__(self):
        return f'<Employee {self.name} {self.salary}>'

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f'<Manager {self.name} {self.department}>'


def print_details(obj):
    print(obj)
    print(type(obj))

employee = Employee('John', 500)
print_details(employee)

manager = Manager('Susan', 600, 'Engenieer')
print_details(manager)
