class Node:
    def __init__(self,elem):
        self.info=elem
        self.next=None

class Stack:
    def __init__(self):
        self.s=None
        self.c=0

    
    def isempty(self):
        if self.s==None:
            return True
        else:
            return False
        
    def push(self,elem):
        if self.s==None:
             self.s=Node(elem)
        else:
            t=Node(elem)
            t.next=self.s
            self.s=t
        self.c+=1

    def pop(self):
        if self.isempty():
            print("Empty Stack!!")
            return -1
        else:
            elem=self.s.info
            t=self.s
            self.s=t.next
            del t
            self.c-=1
            return elem
    def size(self):
        return self.c


s=Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(f'Stack Size after Pushing elements: {s.size()}')

print(f'Using pop function top value from the stack is :{s.pop()}')