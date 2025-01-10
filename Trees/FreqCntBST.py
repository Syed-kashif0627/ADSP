class Node:
    def __init__(self, word):
        self.word = word
        self.count = 1
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, word):
        if node is None:
            return Node(word)
        if word == node.word:
            node.count += 1
        elif word < node.word:
            node.left = self.insert(node.left, word)
        else:
            node.right = self.insert(node.right, word)
        return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"{node.word}: {node.count}")
            self.inorder(node.right)

def count_words(text):
    words = text.split()
    bst = BST()
    for word in words:
        bst.root = bst.insert(bst.root, word)
    return bst

# Example usage
text = "this is a sample text with several words. this is a test"
bst = count_words(text)
bst.inorder(bst.root)
