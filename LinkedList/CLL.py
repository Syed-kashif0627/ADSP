class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.L = None

    def insFirst(self, elem):
        newNode = Node(elem)
        if self.L is None:
            self.L = newNode
            newNode.next = self.L
        else:
            newNode.next = self.L
            curr = self.L
            while curr.next != self.L:
                curr = curr.next
            curr.next = newNode
            self.L = newNode

    def delFirst(self):
        if self.L is None:
            print("The List is Empty")
            return -1
        else:
            curr = self.L
            while curr.next != self.L:
                curr = curr.next
            if self.L == self.L.next:
                t = self.L.data
                self.L = None
            else:
                t = self.L.data
                k = self.L
                curr.next = self.L.next
                self.L = self.L.next
                del k
            return t

    def insLast(self, val):
        newNode = Node(val)
        if self.L is None:
            self.L = newNode
            newNode.next = self.L
        else:
            curr = self.L
            while curr.next != self.L:
                curr = curr.next
            curr.next = newNode
            newNode.next = self.L

    def display(self):
        if self.L is None:
            print("The List is Empty")
            return
        curr = self.L
        while True:
            print(curr.data, end=" -> ")
            curr = curr.next
            if curr == self.L:
                break
        print("Start")

    def delete(self, key):
        if self.L is None:
            return
        curr = self.L
        prev = None
        while True:
            if curr.data == key:
                if prev is None:
                    temp = self.L
                    while temp.next != self.L:
                        temp = temp.next
                    temp.next = self.L.next
                    self.L = self.L.next
                else:
                    prev.next = curr.next
                return
            elif curr.next == self.L:
                return
            prev = curr
            curr = curr.next

# Create a circular linked list
cll = CircularLinkedList()

# Insert integers to the list
cll.insLast(1)
cll.insLast(2)
cll.insLast(3)
cll.insLast(4)

# Display the list
print("Original list:")
cll.display()

# Delete an integer from the list
cll.delete(3)

# Display the list after deletion
print("List after deleting 3:")
cll.display()
