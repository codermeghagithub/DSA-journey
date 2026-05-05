class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size   # fixed-size array
        self.front = -1
        self.rear = -1

    # Check empty
    def isEmpty(self):
        return self.front == -1

    # Check full
    def isFull(self):
        return self.rear == self.size - 1

    # Insert (enqueue)
    def insert(self, value):
        if self.isFull():
            print("Queue is Full")
            return

        if self.front == -1:   # first element
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = value
        print(value, "inserted")

    # Delete (dequeue)
    def delete(self):
        if self.isEmpty():
            print("Queue is Empty")
            return

        removed = self.queue[self.front]
        print(removed, "deleted")

        # If only one element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

    # Display
    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return

        print("Queue elements:", end=" ")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()


# -------- User Input --------
size = int(input("Enter queue size: "))
q = Queue(size)

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        q.insert(val)

    elif choice == 2:
        q.delete()

    elif choice == 3:
        q.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")


# With build in fn       

# class Queue:
#     def __init__(self, size):
#         self.queue = []
#         self.size = size

#     def isEmpty(self):
#         return len(self.queue) == 0

#     def isFull(self):
#         return len(self.queue) == self.size

#     def insert(self, value):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.queue.append(value)
#             print(value, "inserted")

#     def delete(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             removed = self.queue.pop(0)
#             print(removed, "deleted")

#     def display(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Queue:", self.queue)


# # -------- User Input Part --------
# size = int(input("Enter queue size: "))
# q = Queue(size)

# while True:
#     print("\n1. Insert")
#     print("2. Delete")
#     print("3. Display")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         value = int(input("Enter value to insert: "))
#         q.insert(value)

#     elif choice == 2:
#         q.delete()

#     elif choice == 3:
#         q.display()

#     elif choice == 4:
#         print("Exiting...")
#         break

#     else:
#         print("Invalid choice")