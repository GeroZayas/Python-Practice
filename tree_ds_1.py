# create the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

# we Initialize a Tree
root = Node(10)
root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.right = Node(50)

# print(root.data)

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

print("This is preorder of root")
preorder(root)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)



print("This is inorder of root")
inorder(root)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

print("This is postorder of root")
postorder(root)
