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

class C(B):
    def fifth(self):
        print("this is the 5th method of sub class")
    def six(self):
        print("this is the 6th method of sub class") 


ob1=C()
ob1.first()
ob1.second()

# ob2=B()
ob1.third()
ob1.fourth()

# ob3=C()
ob1.fifth()
ob1.six()


num = int(input("Enter a number: "))

# Loop from 1 to 12 (inclusive)
for i in range(1, 13):
  # Calculate and print the product
  product = num * i
  print(f"{num} x {i} = {product}")