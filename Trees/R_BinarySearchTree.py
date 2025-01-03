class Node:
    def __init__(self,elem):
        self.data=elem
        self.ls=None
        self.rs=None

class RBST:
    def __init__(self):
        self.root=None
    
    def constBST(self,root,elem):
        if root==None:
            return Node(elem)

        if elem<root.data:
            root.ls=self.constBST(root.ls,elem)
        else:
            root.rs=self.constBST(root.rs,elem)

        return root
    
    def inorderTraversal(self,root):
        if root!=None:
            self.inorderTraversal(root.ls)
            print(root.data, end=' ')
            self.inorderTraversal(root.rs)

    def search(self,root,key):
        if root==None or root.data==key:
            return root
        if key<root.data:
            return self.search(root.ls,key)
        else:
            return self.search(root.rs,key)
        
tree=RBST()
arr=[20,30,10,5,15,25,35]

for i in arr:
    tree.root=tree.constBST(tree.root,i)

print("The inorder Traversal of Binary Search Tree is : ")

tree.inorderTraversal(tree.root)

print()

Key=25
res=tree.search(tree.root,Key)

if res:
    print(f'The key {Key} is fround in Binary Search Tree')
else:
    print(f'The key {Key} is not found in Binary Search Tree')
