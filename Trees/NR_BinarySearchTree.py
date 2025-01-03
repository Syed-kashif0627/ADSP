class Node:
    def __init__(self,elem):
        self.data=elem
        self.ls=None
        self.rs=None

class NRBST:
    def __init__(self):
        self.root=None
    
    def constBST(self,root,elem):
        newNode=Node(elem)
        if root==None:
            root=newNode
        else:
            p=None
            curr=root
            while curr!=None:
                p=curr
                if elem<curr.data:
                    curr=curr.ls
                else:
                    curr=curr.rs
            if elem<p.data:
                p.ls=newNode
            else:
                p.rs=newNode
        return root
    
    def inorderTraversal(self,root):
        if root!=None:
            self.inorderTraversal(root.ls)
            print(root.data, end=' ')
            self.inorderTraversal(root.rs)

    def NRSearch(self,root,key):
        curr=root
        while(curr!=None):
            if key==curr.data:
                return curr
            elif key<curr.data:
                curr=curr.ls
            else:
                curr=curr.rs

tree=NRBST()

arr=[16,10,30,20,25,35]

for i in arr:
    tree.root=tree.constBST(tree.root,i)

print("The inorder Traversal of Binary Search Tree is : ")

tree.inorderTraversal(tree.root)

print()

Key=20
res=tree.NRSearch(tree.root,Key)

if res:
    print(f'The key {Key} is fround in Binary Search Tree')
else:
    print(f'The key {Key} is not found in Binary Search Tree')



