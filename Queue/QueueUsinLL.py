class Node:
    def __init__(self, data):
        self.info = data
        self.next = None

class Queue:
    def __init__(self):
        self.f = None
        self.r = None
        self.c = 0

    def enqueue(self, elem):
        t = Node(elem)
        if self.r is None:
            self.f = t
            self.r = t
        else:
            self.r.next = t
            self.r = t
        self.c += 1

    def dequeue(self):
        if self.f is None:
            print("Queue is Empty")
            return -1
        elem = self.f.info
        t = self.f
        self.f = self.f.next
        if self.f is None:
            self.r = None
        del t
        self.c -= 1
        return elem

    def isEmpty(self):
        return self.c == 0

    def size(self):
        return self.c


q = Queue()

# Read a list of integers
input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]

print('Inserting Into Queue using Enqueue.....')
for num in input_list:
    q.enqueue(num)
print('Elements Inserted Successfully In the Queue!!')
print('\nDequeuing From the Queue......')
print("The integers in the same order (FIFO):")
while not q.isEmpty():
    print(q.dequeue(), end=" ")

