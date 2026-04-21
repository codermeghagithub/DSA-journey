def create_arr():
  lis=[]
  n=input("Enter the size of arr :")

  while  n.isdigit()==False:
    n=input("Enter integer size value :")
  n=int(n)  
  
  for i in range(n):
      ele=input(f"Enter ele in arr {i}: ")
      while  ele.isdigit()==False:
        ele=input("Enter integer ele not other data type :")
      ele=int(ele)  
     
      lis.append(ele)
  return lis
      
       
def Bubble_sort(arr):
   n=len(arr)
   for i in range(n-1):
      for j in range(0,n-i-1):
         if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
   return arr
arr=create_arr()
sort_arr=Bubble_sort(arr)
print("Sorted arr is:",sort_arr)         



