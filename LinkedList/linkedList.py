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

    def delFirst(self):
        if self.L is None:
            print("The List is Empty: ")
            return -1
        else:
            t=self.L.data
            k=self.L
            self.L=self.L.next
            del k
            return t
    def insLast(self,val):
        if self.L is None:
            self.L=Node(val)
        else:
            c=self.L
            while c.next!=None:
                c=c.next
            t=Node(val)
            c.next=t


l1=LinkedList()

l1.insFirst(50)
l1.insFirst(39)
l1.insFirst(43)
l1.insFirst(62)

curr=l1.L
while curr!=None:
    print(curr.data)
    curr=curr.next
        
deletedElem=l1.delFirst()
print(f'Deleted First ELement from the list : {deletedElem}')

l1.insLast(1)

print("list after insert at last and delting from first :")

curr=l1.L
while curr!=None:
    print(curr.data)
    curr=curr.next
        

