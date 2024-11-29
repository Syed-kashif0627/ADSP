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
def display_fifo(input_list):
    queue = Queue()
    for item in input_list:
        queue.enqueue(item)
    
    fifo_list = []
    while not queue.isEmpty():
        fifo_list.append(queue.dequeue())
    
    return fifo_list


n = int(input("Enter the size of the list: "))
input_list = []
for i in range(n):
    elem = int(input(f"Enter the {i+1}th element: "))
    input_list.append(elem)

print("Original List:")
print(input_list)

fifo_list = display_fifo(input_list)

print("List in FIFO order:")
print(fifo_list)
