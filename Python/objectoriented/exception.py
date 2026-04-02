# num=input("Enter a number :")
# print(f"Multiplication table of {num} is: ")

# try:
#   for i in range(1,11):
#      print(f"{int(num)} X {i} = {int(num)*i}")

# except:
#    print("Invalid input") 
# print("this is important portion")    

try:
    num=int(input("Enter a number: "))
    lis=[3,4]
    print(lis[num])
except ValueError:
    print("Which number you have entered that numver is not integer.") 
except IndexError:
    print("Index Error")    


