# class A:
#     def __init__(self):
#         print("in the init part")
#     def animal(self):
#         print("the animal Method")

#     def DOg(self):
#         print("this is dog")  

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("this is 2nd init me")
#     def animal2(self):
#         print("2")
        
#     def dog2(self):
#         print(dog2)  
#         # if ypu want to call the method b creating  function
#     def fill(self):
#         super().animal()    

# ob1=B()        
# ob1.animal()








# class A:
#     def __init__(self):
#         print("init in A")
#     def animal(self):
#         print("the animal Method")

#     def DOg(self):
#         print("this is dog")  

# class B():
#     def __init__(self):
#         super().__init__()
#         print("this is 2nd init me")
#     def animal2(self):
#         print("2")
        
#     def dog2(self):
#         print(dog2) 


# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print("init in c")
#     def animal2(self):
#         print("2")
        
    # def dog2(self):
    #     print(dog2)  
        # if ypu want to call the method by super keyword
   
# ob1=C()        #here do not print B init method
# 


# ob1.animal()

# class Book:
#     name=" "
#     price=0
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# # Creating an object of the Book class
# book1 = Book("Python Programming", 29.99)

# # Accessing attributes of the object
# print("Book Name:", book1.name)
# print("Book Price:", book1.price)


# CREATE STUDENT CLASS THAT NAME & MARKS OF 3 SUB AS ARGUMENTS IN CONSTRUCTOR THEN CREATE A METHOD  TO PRINTTHE AVERAGE


# Using non static method 
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def Avg(self):
#         sum=0
#         for i in self.marks:
#             sum=+i
#             # average=sum/3
#             # return self.average
#         print("Hello",self.name,"your average score  is :",sum/3)
# s1=Student("Megha",[90,89,76])  
# print(s1.Avg())



class Person:
  
  def __init__(self,n,v):
     print("Hey My name is Megha De")
     self.name=n
     self.vill=v
  def  show(self):
     print(f"{self.name} says his village name is {self.vill}")

p1=Person("Ram","Ayodhya")
p2=Person("Meg","Pririrchak")
p1.show()
p2.show()
     