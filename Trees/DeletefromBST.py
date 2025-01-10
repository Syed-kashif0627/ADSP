class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, name):
        if self.root is None:
            self.root = Node(name)
        else:
            current = self.root
            parent = None
            while current:
                parent = current
                if name < current.name:
                    current = current.left
                else:
                    current = current.right
            if name < parent.name:
                parent.left = Node(name)
            else:
                parent.right = Node(name)

    def delete(self, name):
        self.root = self._delete(self.root, name)

    def _delete(self, node, name):
        if node is None:
            return node

        if name < node.name:
            node.left = self._delete(node.left, name)
        elif name > node.name:
            node.right = self._delete(node.right, name)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min_value_node(node.right)
            node.name = temp.name
            node.right = self._delete(node.right, temp.name)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.name, end=' ')
            self.inorder(node.right)

# Example usage
bst = BST()
names = ["John", "Alice", "Bob", "Diana", "Charlie"]
for name in names:
    bst.insert(name)

print("Inorder traversal before deletion:")
bst.inorder(bst.root)
print("\nDeleting 'Bob'")
bst.delete("Bob")
print("Inorder traversal after deletion:")
bst.inorder(bst.root)
