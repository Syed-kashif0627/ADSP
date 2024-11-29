class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def reverseList(input_list):
    stack = Stack()
    for item in input_list:
        stack.push(item)
    
    reversedList = []
    while not stack.isEmpty():
        reversedList.append(stack.pop())
    
    return reversedList


n = int(input("Enter the size of the list: "))
input_list = []
for i in range(n):
    elem = int(input(f"Enter the {i+1}th element: "))
    input_list.append(elem)

print("Pushing into Stack")

print("Original List:")
print(input_list)

reversedList = reverseList(input_list)

print("List After Reversing using Stack:")
print(reversedList)
