# HERE I WANT TO CHANGE VALUE OF VARIABLE USING INIT METHOD

class Person:
    def __init__(self):
        self.name="santu"
        self.sex="male"

    def update(self):
       self.name="san"

    def compare(self,other):
       if self.name==other.name:
        return True
       else:
        return False


p1=Person()
p2=Person()
p1.name="lesa"

if p1.compare(p2):
    print("they are same")
else:
    ("not")

# p2.name="Megh"
# p2.sex="fmale"

print("name is",p1.name)
print("name is",p2.name)

# print("name is",p1.sex)
# print("name is",p2.sex)




# 1. Default Constructor
# A default constructor does not take any parameters other than self. It initializes the object with default attribute values.


class Car:
    def __init__(self, make, model, year):
      
        #Initialize the Car with specific attributes.
        self.make = make
        self.model = model
        self.year = year

# Creating an instance using the parameterized constructor
car = Car("Honda", "Civic", 2022)
print(car.make)
print(car.model)
print(car.year)

class Car:
    def __init__(self):

        #Initialize the Car with default attributes
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

# Creating an instance using the default constructor
car = Car()
print(car.make)
print(car.model)
print(car.year)


#  Parameterized Constructor
# A parameterized constructor accepts arguments to initialize the object’s attributes with specific values.
class Car:
    def __init__(self, make, model, year):
      
        #Initialize the Car with specific attributes.
        self.make = make
        self.model = model
        self.year = year

# Creating an instance using the parameterized constructor
car = Car("Honda", "Civic", 2022)
print(car.make)
print(car.model)
print(car.year)