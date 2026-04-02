# class Account:
#   def __init__(self,acc_IFC):
#     self .acc_IFC=acc_IFC 


  


# acc1=Account("4561")
# print(acc1)

# del acc1
# print(acc1)


# class Account:
#   def __init__(self,acc_no,acc_IFC):
#     self .__acc_no=acc_no #Here i have create private attribute 
#     self .__acc_IFC=acc_IFC #Here i have create private attribute usinf before .__acc_no


#   def reset(self):
#     print(self.__acc_no)
   


# acc1=Account("4561","ac1234")
# # print(acc1.__acc_no)   #AttributeError: 'Account' object has no attribute '__acc_no'  here we can not access this attributes 
# print(acc1.reset())   #here is another way to access the private attribute 

# # if we can not access this attributes  so we can create   function






# class Account:
#   def __init__(self,acc_no,acc_IFC):
#     self .__acc_no=acc_no  
#     self .__acc_IFC=acc_IFC


#   def __reset(self):
#     print(self.__acc_no)

#   def  hello(self):
#     self.__reset()   
   


# acc1=Account("4561","ac1234")
# # print(acc1.__acc_no)   #AttributeError: 'Account' object has no attribute '__acc_no'  here we can not access this attributes 
# # print(acc1.reset())   #here is another way to access the private attribute 
# print(acc1.hello())





