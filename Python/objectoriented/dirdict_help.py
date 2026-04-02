# x=[1,2,3,4] 
# x=(1,2,3,4) #if you store this value within the tuple so you can know about tuple 
# print(dir(x))  #this gives how manu methods present which are the attribute
# print(x.__add__)  #this gives  what is the __add__ what methods can we run here 


class student:
  def __init__(self,name,roll):
    self.name=name
    self.roll=roll

s1=student("Ram",3)
print(s1.__dict__)   # this tell me all about class

# print(help(student))
print(help(str))   #this tell me all abi=out string 

