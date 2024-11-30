class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Function to display list of integers in FIFO order using the Queue class
def displayFIFO(list):
    queue = Queue()
    for item in list:
        queue.enqueue(item)
    
    fifoList = []
    while not queue.isEmpty():
        fifoList.append(queue.dequeue())
    
    return fifoList


n = int(input("Enter the size of the list: "))
list = []
for i in range(n):
    elem = int(input(f"Enter the {i+1}th element: "))
    list.append(elem)

print("Original List:")
print(list)

fifoList = displayFIFO(list)

print("List in FIFO order:")
print(fifoList)
