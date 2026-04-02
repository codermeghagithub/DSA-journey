# super() Function:
# super() function is used to call the parent class’s methods. In particular, it is commonly used in the child class’s __init__() method to initialize inherited attributes. This way, the child class can leverage the functionality of the parent class.

# Parent Class: Person
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# Child Class: Employee
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)  # Using super() to call Person's __init__()
        self.salary = salary
        self.post = post
