class A:
    def first(self):
        print("this is the first method  of super class")
    
    def second(self):
        print("this is the second method of super class")

class B(A):
    def third(self):
        print("this is the third method of sub class")
    def fourth(self):
        print("this is the fourth method of sub class") 


ob1=A()
ob1.first()
ob1.second()

ob2=B()
ob2.third()
ob2.fourth()