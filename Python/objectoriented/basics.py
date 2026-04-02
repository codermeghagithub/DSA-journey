# class car:
#     brand=" "
#     model=" "
#     price=0
#     def show(self):
#         self.brand="sujuki"
#         self.model="2nd"
#         self.price=40000
#     def disp(self):
#          print(self.brand) 
#          print(self.model) 
#          print(self.price)   
# c1=car()
# c1.show()
# c1.disp()      





# USE OF SELF KEYWORD
# class Details:
#     name = "Rohan"
#     age = 20

#     def desc(self):
#         print("My name is", self.name, "and I'm", self.age, "years old.")

# obj1 = Details()
# obj1.desc()


# 3.

# class Student:
  
#   def __init__(self,name):  //creating constructor 
#      self.name=name
#      print("adding new student in database")

# stu=Student("Ram")
# print(stu.name)    

# stu1=Student("Megha")
# print(stu1.name)


# class Student:
#   def __init__(self):
#      pass  #this is a default contractor 
  
#   def __init__(self,name,section): #this is a parameterized contractor 
#      self.name=name
#      self.section=section

#      print("adding new student in database")

# stu=Student("Ram","D")
# print(stu.name,stu.section)    

# stu1=Student("Megha","D")
# print(stu1.name,stu1.section)


# How do you confirm object > class preference?
# The rule applies when the same name is accessed through the object.

# Example:
# print(d1.dep_name)  # <- Object attribute is checked first!
# MCA

# class Department:
#    college_name="AU" # here i have created class attribute  
#    dep_name="BCA"  #   always gets preference first class attribute   obj_attribute > class_attribute
#    def __init__(self,dep_name):
#       self.dep_name=dep_name  #creating obj attri 
#       print("Yes  this is your depertment")
# d1=Department("MCA")  
    
# print(d1.dep_name)
# print(Department.dep_name)

      
# class Employee:
#     emp_id=" "
#     emp_name=" "
#     salary=0  
#     def __init__(self,emp_id=" ",emp_name=" ",salary=0  ):
#         self.emp_id=emp_id
#         self.emp_name=emp_name
#         self.salary=salary
#     def show(self):
#         print(self.emp_id,self.emp_name,self.salary)   
# obj1=Employee(33,"nadiya",450000)      
# obj1.show() 


# non static method 

# creating method 

# class Student:
  
#   def __init__(self,name,marks):
#      self.name=name
#      self.marks=marks

#      print("adding new student in database")

#   def Hello(self):
#      print("Hello all of the students from my side ")   
#   def fetch(self):
#      return self.marks
  
# stu=Student("Ram",98)
# print(stu.name)    
# stu.Hello()
# print(stu.fetch())


# Static Method :when we use static method that time as a parameter there do not need any self parammeter 

# Methos that donot use the self parameter (Work at class level )

# class Student:
#    @staticmethod      #decorator
#    def University():
#       print("AU")


class Student:
  
  def __init__(self,name,marks):
     self.name=name
     self.marks=marks

     print("adding new student in database")

  def Hello(self):
     print("Hello all of the students frommy side ")   
  def fetch(self):
     return self.marks
#   in static method do not need any self 
  @staticmethod
  def get_data():
     print("HI student are you doing well" )
     
  
stu=Student("Ram",98)
print(stu.name)    
stu.Hello()
print(stu.fetch())
stu.get_data()


# # ABSTUCTION

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
# c1.start()      




# practice creating constractor 

# class Car:


#    def __init__(self,brand ,col):
#       self.brand=brand
#       self.col=col
#    def dis(self):
#       print(self.brand)   
#       print(self.col)   


# ob1=Car("Toyota","red")
# ob1.dis()