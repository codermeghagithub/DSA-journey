
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Display List
    def display(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head
        print("NULL <- ", end="")
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("NULL")

    # Insert at Beginning
    def insert_beg(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp



    def insert_index(self, index, data):
        if index == 0:
            self.insert_beg(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 0

        while temp is not None and count < index - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid Index")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

# del b
    def delete_beg(self):
        if self.head is None:
            print("List Empty")
            return

        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    # Del End
    def delete_end(self):
        if self.head is None:
            print("List Empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

    # Delete at Index
    def delete_index(self, index):
        if self.head is None:
            print("List Empty")
            return

        if index == 0:
            self.delete_beg()
            return

        temp = self.head
        count = 0

        while temp is not None and count < index:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid Index")
            return

        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next


# Main Program
dll = DoublyLinkedList()

while True:
    print("\n1.Insert Beginning")
    print("2.Insert End")
    print("3.Insert At Index")
    print("4.Delete Beginning")
    print("5.Delete End")
    print("6.Delete At Index")
    print("7.Display")
    print("8.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        val = int(input("Enter Value: "))
        dll.insert_beg(val)

    elif ch == 2:
        val = int(input("Enter Value: "))
        dll.insert_end(val)

    elif ch == 3:
        idx = int(input("Enter Index: "))
        val = int(input("Enter Value: "))
        dll.insert_index(idx, val)

    elif ch == 4:
        dll.delete_beg()

    elif ch == 5:
        dll.delete_end()

    elif ch == 6:
        idx = int(input("Enter Index: "))
        dll.delete_index(idx)

    elif ch == 7:
        dll.display()

    elif ch == 8:
        print("Program End")
        break

    else:
        print("Invalid Choice")