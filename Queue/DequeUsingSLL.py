class Node:
    def __init__(self,elem):
        self.data=elem
        self.next=None

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0

    def isEmpty(self):
        return self.size==0
    
    def getSize(self):
        return self.size
    
    def addFirst(self,elem):
        newNode=Node(elem)
        if self.isEmpty():
            self.front=self.rear=newNode
        else:
            newNode.next=self.front
            self.front=newNode
        self.size+=1

    def addLast(self,elem):
        newNode=Node(elem)
        if self.isEmpty():
            self.front=self.rear=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode
        self.size+=1
    
    def delFirst(self):
        if self.isEmpty():
            print("Deque is Empty!!")
        data=self.front.data
        self.front=self.front.next
        if self.front==None:
            self.rear=None
        self.size-=1
        return data
    
    def delLast(self):
        if self.isEmpty():
            print("Deque is Empty!!")
        data=self.rear.data
        if self.front==self.rear:
            self.front=self.rear=None
        else:
            curr=self.front
            while curr.next!=self.rear:
                curr=curr.next
            curr.next=None
            self.rear=curr
        self.size-=1
        return data
    
# Create a deque
deque = Deque()

# Add elements to the front and rear
deque.addFirst(10)
deque.addLast(20)
deque.addFirst(5)
deque.addLast(30)

# Display the size of the deque
print("Size of deque:", deque.getSize())

# Remove elements from the front and rear
print("Removed from front:", deque.delFirst())
print("Removed from rear:", deque.delLast())

# Display the size of the deque
print("Size of deque:", deque.getSize())


    
