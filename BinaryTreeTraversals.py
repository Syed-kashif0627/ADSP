class Node:
    def __init__(self, elem):
        self.data = elem
        self.ls = None
        self.rs = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, root, elem):
        if elem != '$':
            if root is None:
                root = Node(elem)
            else:
                if root.ls is None:
                    root.ls = self.insert(root.ls, elem)
                elif root.rs is None:
                    root.rs = self.insert(root.rs, elem)
                else:
                    root.ls = self.insert(root.ls, elem)
        return root

    def inorder(self, root):
        if root is not None:
            self.inorder(root.ls)
            print(root.data, end=' ')
            self.inorder(root.rs)

    def preorder(self, root):
        if root is not None:
            print(root.data, end=' ')
            self.preorder(root.ls)
            self.preorder(root.rs)
    
    def postorder(self, root):
        if root is not None:
            self.postorder(root.ls)
            self.postorder(root.rs)
            print(root.data, end=' ')

bt = BinaryTree()
elements = [16, 10, 30, '$', '$', 20, '$', '$', 25]
for elem in elements:
    bt.root = bt.insert(bt.root, elem)

print("Preorder traversal of the binary tree:")
bt.preorder(bt.root)
print()
print("Inorder traversal of the binary tree:")
bt.inorder(bt.root)
print()
print("Postorder traversal of the binary tree:")
bt.postorder(bt.root)
print()
