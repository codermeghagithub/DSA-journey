 # ABSTUCTION:

# class Car:
#    def __init__(self):
#       self.acc=False
#       self.breaks=False
#       self.clutch=False

#    def start(self):
#       self.clutch=True
#       self.breaks=True
#       print("Now car is started")
# c1=Car()
# c1.start()     #here this gives me output   Now car is started but within the method it  its internal method keeps hiding like how to write our data how to work the start method 








# How to Implement Encapsulation in Python Classes?
# Encapsulation in Python is implemented using access specifiers to control access to class members:
# Protected Access Modifier

# Public Access Specifier :
# in Python All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

# class Employee:
#   def __init__(self):
#     self.name="Megha"

# e1=Employee()
# print("The name of the emplee is:",e1.name)

#  class Employee:
#   def __init__(self):
#     self.__name="Megha"

# e1=Employee()
# # anyone can not access this private specifiers directly 
# print("The name of the emplee is:",e1.__name)

# # yes we can access this private variable helping mangling technique (in python)[inderectmethod]

# print(e1._Employee__name)
# print(e1.__dir__())




class Student:
  def __init__(self):
    self._name="Megha"

  def _funName(self):
    return "CoderMEgha"

class Subject(Student):
     pass

obj=Student()
obj1=Subject()
print(dir(obj))

print(obj._name)
print(obj._funName())

print(obj1._name)
print(obj1._funName())
