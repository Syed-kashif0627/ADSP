class Deque:
    def __init__(self):
        self.dq = []

    def isempty(self):
        return len(self.dq) == 0
    
    def addFirst(self, elem):
        self.dq.insert(0, elem)

    def addLast(self, elem):
        self.dq.append(elem)

    def delFirst(self):
        if self.isempty():
            print("Empty D Queue!!")
            return -1
        return self.dq.pop(0)
    
    def delLast(self):
        if self.isempty():
            print("Empty Queue!!")
            return -1
        return self.dq.pop()
    
    def front(self):
        if self.isempty():
            print("Empty Queue!!")
            return -1
        return self.dq[0]
    
    def rear(self):
        if self.isempty():
            print("Empty Queue!!")
            return -1
        return self.dq[-1]
    
    def size(self):
        return len(self.dq)

# Example usage
dqu = Deque()
dqu.addFirst(14)
dqu.addLast(3)

print(f'size of deque after adding elements: {dqu.size()}')

dqu.addFirst(4)
dqu.addLast(10)

print(f'front value of deque is: {dqu.front()} rear value of deque is: {dqu.rear()}')
