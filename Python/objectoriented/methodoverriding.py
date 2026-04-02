class shape:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def area(self):
    return self.x*self.y

class Circle(shape):
  def __init__(self,radius):
    self.radius=radius
    super().__init__(radius,radius)    #radius=x,radius=y
  def area(self):   #here is the overriding method 
    return 3.14*super().area()  #  it means 3.14*self.radius*self.radius
# rec = Shape(3, 5)
# print(rec.area())

c = Circle(5)
print(c.area())  