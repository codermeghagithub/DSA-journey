class Student:
  college_name="AU"   # this is a class variable 

  def __init__(self,name):
    self.name=name   #  ** 
    self.sem=4          #    **this all are instace variable
  def showdetails(self):
    print("All student Welcome ",self.name,self.sem)  


s1=Student("Megha")
s1.showdetails()
# or 
# Student.showdetails(s1)
# print(s1.name)
s2=Student("Lila")
print(s2.showdetails())