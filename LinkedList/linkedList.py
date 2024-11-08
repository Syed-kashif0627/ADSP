from node import Node

class LinkedList:
    def __init__(self):
        self.L=None

    def insFirst(self,elem):
        if self.L is None:
            self.L=Node(elem)
        else:
            t=Node(elem);
            t.next=self.L
            self.L=t
            

l1=LinkedList()

l1.insFirst(50)
l1.insFirst(39)
l1.insFirst(43)
l1.insFirst(62)

curr=l1.L
while curr!=None:
    print(curr.data)
    curr=curr.next
        