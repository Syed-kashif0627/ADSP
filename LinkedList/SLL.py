class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.L = None

    def insFirst(self, elem):
        if self.L is None:
            self.L = Node(elem)
        else:
            t = Node(elem)
            t.next = self.L
            self.L = t

    def delFirst(self):
        if self.L is None:
            print("The List is Empty")
            return -1
        else:
            t = self.L.data
            k = self.L
            self.L = self.L.next
            del k
            return t

    def insLast(self, val):
        if self.L is None:
            self.L = Node(val)
        else:
            c = self.L
            while c.next is not None:
                c = c.next
            t = Node(val)
            c.next = t

    def display(self):
        curr = self.L
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def delete(self, key):
        curr = self.L

        if curr and curr.data == key:
            self.L = curr.next
            curr = None
            return

        p = None
        while curr and curr.data != key:
            p = curr
            curr = curr.next

        if curr is None:
            return

        p.next = curr.next
        curr = None

# Create a linked list
ll = LinkedList()

# Insert integers to the list
ll.insLast(1)
ll.insLast(2)
ll.insLast(3)
ll.insLast(4)

# Display the list
print("Original list:")
ll.display()

# Delete an integer from the list
ll.delete(3)

# Display the list after deletion
print("List after deleting 3:")
ll.display()
