class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Display list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

    # Insert at beginning
    def insert_beg(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Insert at index
    def insert_index(self, data, index):
        if index == 0:
            self.insert_beg(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 0

        while temp.next != self.head and count < index - 1:
            temp = temp.next
            count += 1

        if count != index - 1:
            print("Invalid index")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete from beginning
    def delete_beg(self):
        if self.head is None:
            print("List empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        self.head = self.head.next
        temp.next = self.head

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        prev = None
        temp = self.head

        while temp.next != self.head:
            prev = temp
            temp = temp.next

        prev.next = self.head

    # Delete at index
    def delete_index(self, index):
        if self.head is None:
            print("List empty")
            return

        if index == 0:
            self.delete_beg()
            return

        temp = self.head
        prev = None
        count = 0

        while temp.next != self.head and count < index:
            prev = temp
            temp = temp.next
            count += 1

        if count != index:
            print("Invalid index")
            return

        prev.next = temp.next

cll = CircularLinkedList()

while True:
    print("\n1.Insert Beg  2.Insert End  3.Insert Index")
    print("4.Delete Beg  5.Delete End  6.Delete Index")
    print("7.Display  8.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        cll.insert_beg(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        cll.insert_end(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        index = int(input("Enter index: "))
        cll.insert_index(data, index)

    elif choice == 4:
        cll.delete_beg()

    elif choice == 5:
        cll.delete_end()

    elif choice == 6:
        index = int(input("Enter index: "))
        cll.delete_index(index)

    elif choice == 7:
        cll.display()

    elif choice == 8:
        break

    else:
        print("Invalid choice")