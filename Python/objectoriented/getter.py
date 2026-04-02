

# class MyClass:
#   def __init__(self,value):
#     self._value=value 
# #Why use self._value instead of self.value?
# # _value (with underscore): It's a private variable used to store data inside the class.
# # value (without underscore): This is a public property that allows controlled access to _value.

#   def show(self):
#     print(f"value is :{self._value}")

#   @property   #this is decoretor 
#   def value(self):
#     return self._value

# obj=MyClass(10) 
# print(obj._value) 
# obj.show()

# setter

class MyClass:
  def __init__(self,value):
    self._value=value

  def show(self):
    print(f"value is {self._value}")

  @property
  def ten_value(self):
    return 10*self._value
  

  @ten_value.setter   # tenx value name er property made  so i create ten_value decoretor by using setter bec i cant do using getter 
  def ten_value(self,new_value):   # here i have  created  a method but i have made it in a way that it behave like a property and i was able to print this as aproperty
    self._value=new_value/10

obj=MyClass(10)
obj.ten_value=30  #by this i change this value of ten_value 
print(obj.ten_value)
obj.show()


