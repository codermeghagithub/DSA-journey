# not user input 

# class Node:
#   def __init__(self,data,next=None):
#     self.data=data
#     self.next=next  


# class SingleLL:
#   def __init__(self,head=None):
#     self.head=head
     
#   def insertAt_end(self,value):

#     temp=Node(value)
#     if(self.head!=None):
#       t1=self.head  # head can't move so t1 like pointer it move one node to another  node 
#       while(t1.next!=None):
#          t1=t1.next
#       t1.next=temp
#     else:  #there is no node 
#       self.head=temp # self.head point to temp
    


#   def insertAt_big(self,value):
#     temp=Node(value)
#     temp.next=self.head 
#     self.head=temp 


#   def insertAt_idx(self,value,idx):
#     temp=Node(value)




#   def deleteAt_big(self):
#     t1=self.head
#     # if(t1.data==value):
#     self.head=t1.next

#   def deleteAt_end(self):
#     if self.head is None:
#         print("Empty list")
    
#     elif self.head.next is None:
#         self.head = None

#     else:
#         t1 = self.head

#         while t1.next.next is not None:
#             t1 = t1.next

#         t1.next = None


#   def deleteByValue(self, value):

#     if self.head is None:
#         print("Empty list")
#         return

#     t1 = self.head
#     prev = None

#     while t1 is not None:

#         if t1.data == value:

#             if prev is None:
#                 self.head = t1.next
#             else:
#                 prev.next = t1.next

#             return

#         prev = t1
#         t1 = t1.next

#     print("Value not found")
  
     
#   def DisplayLL(self):
#     t1=self.head
#     while(t1.next!=None):
#       print(t1.data)
#       t1=t1.next
#     print(t1.data)  

# obj1=SingleLL()
# obj1.insertAt_end(10)
# obj1.insertAt_end(20)
# obj1.insertAt_end(30)
# obj1.insertAt_big(1)
# obj1.deleteAt_big()
# obj1.deleteAt_end()
# obj1.deleteByValue(20)
# obj1.DisplayLL()





# using user input 

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SingleLL:
    def __init__(self, head=None):
        self.head = head

    # Insert at End
    def insertAt_end(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp

    # Insert at Beginning
    def insertAt_big(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    # Insert at Index
    def insertAt_idx(self, value, idx):
        temp = Node(value)

        if idx == 0:
            temp.next = self.head
            self.head = temp
            return

        t1 = self.head
        count = 0

        while t1 is not None and count < idx - 1:
            t1 = t1.next
            count += 1

        if t1 is None:
            print("Invalid Index")
        else:
            temp.next = t1.next
            t1.next = temp

    # Delete at Beginning
    def deleteAt_big(self):
        if self.head is None:
            print("List is Empty")
        else:
            self.head = self.head.next

    # Delete at End
    def deleteAt_end(self):
        if self.head is None:
            print("List is Empty")

        elif self.head.next is None:
            self.head = None

        else:
            t1 = self.head

            while t1.next.next is not None:
                t1 = t1.next

            t1.next = None

    # Delete at Index
    def deleteAt_idx(self, idx):
        if self.head is None:
            print("List is Empty")
            return

        if idx == 0:
            self.head = self.head.next
            return

        t1 = self.head
        count = 0

        while t1.next is not None and count < idx - 1:
            t1 = t1.next
            count += 1

        if t1.next is None:
            print("Invalid Index")
        else:
            t1.next = t1.next.next

    # Display
    def DisplayLL(self):
        if self.head is None:
            print("List is Empty")
        else:
            t1 = self.head
            while t1 is not None:
                print(t1.data, end=" -> ")
                t1 = t1.next
            print("None")


# Object
obj1 = SingleLL()

# Menu
while True:
    print("\n1.Insert at End")
    print("2.Insert at Beginning")
    print("3.Insert at Index")
    print("4.Delete at Beginning")
    print("5.Delete at End")
    print("6.Delete at Index")
    print("7.Display")
    print("8.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        obj1.insertAt_end(value)

    elif choice == 2:
        value = int(input("Enter value: "))
        obj1.insertAt_big(value)

    elif choice == 3:
        value = int(input("Enter value: "))
        idx = int(input("Enter index: "))
        obj1.insertAt_idx(value, idx)

    elif choice == 4:
        obj1.deleteAt_big()

    elif choice == 5:
        obj1.deleteAt_end()

    elif choice == 6:
        idx = int(input("Enter index: "))
        obj1.deleteAt_idx(idx)

    elif choice == 7:
        obj1.DisplayLL()

    elif choice == 8:
        break

    else:
        print("Invalid Choice")







# Node class
# class Node:
#     def __init__(self, data,next=None):
#         self.data = data
#         self.next = next


# # Linked List class
# class LinkedList:
#     def __init__(self,head=None):
#         self.head = head

#     # Insert at beginning
#     def insert_begin(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     # Insert at end
#     def insert_end(self, data):
#         new_node = Node(data)
        
#         if self.head is None:
#             self.head = new_node
#             return
        
#         temp = self.head
#         while temp.next is not None:
#             temp = temp.next
        
#         temp.next = new_node

#     # Delete from beginning
#     def delete_begin(self):
#         if self.head is None:
#             print("List is empty")
#             return
        
#         self.head = self.head.next

#     # Delete by value
#     def delete_value(self, value):
#         temp = self.head

#         # If head node itself holds the value
#         if temp is not None and temp.data == value:
#             self.head = temp.next
#             return

#         prev = None
#         while temp is not None and temp.data != value:
#             prev = temp
#             temp = temp.next

#         if temp is None:
#             print("Value not found")
#             return

#         prev.next = temp.next

#     # Display list
#     def display(self):
#         temp = self.head
#         if temp is None:
#             print("List is empty")
#             return
        
#         while temp is not None:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

# ll = LinkedList()

# while True:
#     print("\n1. Insert at Beginning")
#     print("2. Insert at End")
#     print("3. Delete from Beginning")
#     print("4. Delete by Value")
#     print("5. Display")
#     print("6. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         val = int(input("Enter value: "))
#         ll.insert_begin(val)

#     elif choice == 2:
#         val = int(input("Enter value: "))
#         ll.insert_end(val)

#     elif choice == 3:
#         ll.delete_begin()

#     elif choice == 4:
#         val = int(input("Enter value to delete: "))
#         ll.delete_value(val)

#     elif choice == 5:
#         ll.display()

#     elif choice == 6:
#         break

#     else:
#         print("Invalid choice")