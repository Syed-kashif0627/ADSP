
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insFirst(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def delFirst(self):
        if self.head is None:
            print("The List is Empty")
            return -1
        else:
            t = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return t

    def delLast(self):
        if self.head is None:
            print("The List is Empty")
            return -1
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            if curr.prev:
                curr.prev.next = None
            else:
                self.head = None
            return curr.data

    def insLast(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
        newNode.prev = last

    def display(self):
        curr = self.head
        print("None<=>",end='')
        while curr:
            print(curr.data, end="<=>")
            curr = curr.next
        print("None\n")

    def delete(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                if curr == self.head:  # If head node is to be deleted
                    self.head = curr.next
                del curr
                return
            curr = curr.next
        print(f"Element {key} not found in the list")

dll = DoublyLinkedList()

# a) Create a doubly linked list of integers
integers = [1, 2, 3, 4, 5]
for num in integers:
    dll.insLast(num)

# b) Traverse the list and display its contents
print("Contents of the doubly linked list:")
dll.display()

# c) Delete an integer from the list and display the contents after deletion
dll.delete(3)
print("Contents of the doubly linked list after deleting 3:")
dll.display()

# Insert an integer at the beginning of the list
dll.insFirst(0)
print("Contents of the doubly linked list after inserting 0 at the beginning:")
dll.display()

# Delete the first integer from the list
dll.delFirst()
print("Contents of the doubly linked list after deleting the first element:")
dll.display()

# Delete the last integer from the list
dll.delLast()
print("Contents of the doubly linked list after deleting the last element:")
dll.display()

