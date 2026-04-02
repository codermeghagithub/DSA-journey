import sys
sys.setrecursionlimit(2000)                  # HERE IF I WANT TO CHANGE LIMIT OF RECURTION NUMBER IN THAT TIME USE THIS METHOD 

print(sys.getrecursionlimit())              #If you want to know limit of recursion sys.getrecursionlimit())  this is the method which is count how many time it can print but here donot any print 

def second():
    print("hi")
    second()


