class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            parent = None
            while current:
                parent = current
                if value < current.value:
                    current = current.left
                else:
                    current = current.right
            if value < parent.value:
                parent.left = Node(value)
            else:
                parent.right = Node(value)

    def preorder_non_recursive(self):
        if self.root is None:
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.value, end=' ')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
    def postorder_non_recursive(self):
        if self.root is None:
            return
        stack1 = [self.root]
        stack2 = []
        
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        while stack2:
            node = stack2.pop()
            print(node.value, end=' ')


    def inorder_non_recursive(self):
        stack = []
        current = self.root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print(current.value, end=' ')
                current = current.right

# Example usage
bt = BinaryTree()
values = [10, 5, 15, 3, 7, 12, 18]
for value in values:
    bt.insert(value)

print("Non-recursive Preorder traversal:")
bt.preorder_non_recursive()
print("\nNon-recursive Inorder traversal:")
bt.inorder_non_recursive()
