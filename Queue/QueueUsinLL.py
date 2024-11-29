class Node:
    def __init__(self,data):
        self.info=data
        self.next=None

class Queue:
    def __init__(self):
        self.f=None
        self.r=None
        self.c=0

    def enqueue(self,elem):
        t=Node(elem)
        if self.r==None:
            self.f=t
            self.r=t
        else:
            self.r.next=t
            self.r=t
        self.c+=1

    def dequeue(self):
        if self.f==None:
            print("Queue is Empty")
            return -1
        elem=self.f.info
        t=self.f
        self.f=self.f.next
        del t
        self.c-=1
        return elem
    def size(self):
        return self.c

q=Queue()

q.enqueue(1)
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.enqueue(18)

print(f'size of Queue after insertions at the end: {q.size()}')
print(f'Deque function : {q.dequeue()}')
print(f'Deque function : {q.dequeue()}')
print(f'Deque function : {q.dequeue()}')
print(f'Deque function : {q.dequeue()}')
print(f'Deque function : {q.dequeue()}')
print(f'size of queue after dequeing all elements: ')
q.dequeue()

