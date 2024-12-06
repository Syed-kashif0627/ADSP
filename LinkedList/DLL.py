class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
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
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

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
    dll.append(num)

# b) Traverse the list and display its contents
print("Contents of the doubly linked list:")
dll.display()

# c) Delete an integer from the list and display the contents after deletion
dll.delete(3)
print("Contents of the doubly linked list after deleting 3:")
dll.display()
