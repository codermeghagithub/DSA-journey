# def Array_ins_del(list1,n):

# def Display_arr(arr,n):
#     for i in range(n):
#      print(list1[i])
   
# def insert(arr,ele): 
#   idx=int(input("Enter the index of the array:"))
#   ele=int(input("Add an ele in arr:"))
#   for i in range(0,len(list1)):
#     list1[i+1]=arr[i]
   
#   list1.insert(idx,ele)
#   def delete_ele(arr,ele):
   
    
  
#   n=int(input("Enter the size of array "))
#   for i in range(n):
#     list1.append(int(input("Enter  ele of errar:")))
#     Display()


# res=Array_ins_del(list1,n)


# using array module in python 
# from array import *;
# val=array('i',[1,2,3,4,5])
# for i in range(0,len(val)):
#   print(val[i], end=" ")


def get_integer():
  val=input("Enter a number :")

  while val.isdigit()==False:
    print("Invalid input")
    val=input("Enter nuber :")
  return int(val)  

# Create arr
def create_arr():
  lis=[]

  print("Enter size of arr:")
  n=get_integer()

  for i in range(n):
     print(f"Enter ele of arr:{i}")
     lis.append(get_integer())
  return lis

def traverse(lis):
   print("travers the array:")
   for i in range (len(lis)):
     print(lis[i],end=' ')

# Insert
def insert_ele(lis):
  print("Enter idx of :")
  idx=get_integer()
  if  idx>=0 and len(lis)>=idx:
    print("Enter ele of :")
    ele=get_integer()
    for i in range(idx-1,len(lis)):
      lis.insert(idx,ele)
      print("Inserted")
  else:
    print("Invalid index")


# del
def Delete_ele(lis):
   print("Enter index which you want to delete:")
   idx=get_integer()
   if idx<0 or idx>=len(lis):
      print("Invalid idx")
   else:   
      lis.pop(idx)
      # lis[i]=lis[idx+1]
      print("Deleted ")     

arr = create_arr()

while True:
    print("\n1. Traverse")
    print("2. Insert")
    print("3. Delete")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        traverse(arr)
        
    elif choice == '2':
        insert_ele(arr)
        
    elif choice == '3':
        Delete_ele(arr)
        
    elif choice == '4':
        print("Program Ended")
        break
        
    else:
        print("❌ Wrong choice")




