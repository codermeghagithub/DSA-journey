# def max(a,b,c):
#     if a>b and a>c:
#         print(a)
#     elif b>a and b>c:
#         print(b)
#     else:
#          print(c)
# max(23,2,1)    

# def list1(val):
#     sum=0
#     for i in val:
#         sum=sum+i
#     return sum
# list2=[12,3,4,1]
# list3=list1(list2)
# print("sum=",list3)



# def reverse_string(str1):
#   return str1[::-1]

# str1 = "ADAMAS"
# result = reverse_string(str1)
# print(result)

# try:
#     div=int(input("enter a number: "))
#     list_no=[10,4,5,80,25,30]
#     result=list_no[5]/div

# except ZeroDivisionError:
#     print("denominator should no be zero")

# except  IndexError:
#     print("this is index error")  

# print(".......................")



            

# n=input("enter anumber")
# print(f"table of {n} :")   
# try:
#     for i in range(1,11):
#         print(f"{int(n)} x {i}={int(n)*i}")   
# except Exception as e:
#     print("it is exception error")      

# print("this is not")    

# try:
#     div=int(input("enter a number : "))
#     list1=[10,20,30,45,50]
#     res=list1[3]
# except ZeroDivisionError:
#     print("denominetor do not zero")
# except IndexError:
#     print("not in index")



# try:
#     newmenator=int(input("enterr the no: "))
#     deno=int(input("enter the no 2nd no: "))
#     result=newmenator/deno

# except ZeroDivisionError:
#     print("do npot allow zero as deno")

# else:
#     print("divition =",result)





# try:
#     num=int(input("enter a no:"))
#     assert num%2==0
# except:
#     print("not even")
# else:
#     print("not it")
# finally:
#     print("this is exception handling") 



try:
    itsalist = []
    n = int(input("Enter a number: "))
    
    for i in range(n):
        value = int(input("Enter a number of list: "))
        itsalist.append(value)
    
    index = int(input("Enter index to access value: "))
    
    if index >= n:
        raise IndexError

except IndexError:
    print("Check the index")
    
else:
    print("Value at", index, "is", itsalist[index])


# def canvote(age):
#     try:
#         if(age<18):
#             raise ValueError
#     except ValueError:
#         print("not eligable for vote")
#     else:
#         print("elegable for vote")                

# age=int(input("enter age:")) 
# canvote(age)       

# def division(divident,divisor):
#     try:
#         value=divident/divisor
#         if(divisor==0):
#             raise ArithmeticError
#     except  ArithmeticError:
#         print("divisor can npt be zero")
#     else:
#         return value

# divident=int(input("enter a no:"))
# divisor=int(input("enter a no:"))
# print("by deviding we get divisor:",division(divident,divisor))



# def power(n,m):
#     ans=1
#     try:
#         for i in range(m):
#             ans=ans*n
#             if(n==0 or m==0 ):
#                 raise ValueError
#     except:
#         print("power operation can not be zero")   
#     else:
#         return ans
# base=int (input("enter a value:"))       
# exponent=int (input("enter a value:")) 
# print("answer is ",power(base,exponent))          