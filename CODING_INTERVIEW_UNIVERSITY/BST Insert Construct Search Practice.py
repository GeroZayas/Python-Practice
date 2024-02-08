# CREATE A TREENODE CLASS
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# DEFINE THE **INSERT** FUNCTION
# ==================================
def insert(root, key):
    """
    Insert key in Tree
    """
    if not root:
        return TreeNode(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


# DEFINE THE **CONSTRUCTOR of BST** FUNCTION
# ==================================
def constructBST(keys):
    """
    Construct Binary Search Tree based on given keys
    """
    root = None
    for key in keys:
        root = insert(root, key)
    return root


# Some keys to create the BST
# ==================================
keys = [5, 4, 6, 2, 9, 3, 8]


# Initialize the BST
# ==================================
root = constructBST(keys)


# DEFINE the Breadth First Search function
# ==================================
def BFS(root):
    """
    Breadth First Traversal of Tree

    root: TreeNode
    """
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# DEFINE the In Order DFS Traversal function
# ==================================
def inorder_traversal(root):
    """
    In Order Traversal of Tree
    """
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)


print("BFS")
BFS(root)

# ==================================
print()
print("In Order Traversal")
inorder_traversal(root)

print()
print("*" * 40)

# ==================================
print("Search for key:")


# DEFINE the SEARCH for KEY in the BST function
def search(root, key, parent):
    """
    Search for given key in Binary Search Tree
    """
    if root is None:
        print("Key not found")
        return
    if root.data == key:
        if parent is None:
            print(f"The node with the key {key} is root node")
        elif key < parent.data:
            print(
                f"The node with the key {key} is the left node of the node with key {parent.data}"
            )
        else:
            print(
                f"The node with the key {key} is the right node of the node with key {parent.data}"
            )
        return
    if key < root.data:
        search(root.left, key, root)
    else:
        search(root.right, key, root)


# ==================================
key = 5

search(root, key, parent=None)

# ==================================
key = 6

search(root, key, parent=None)

# ==================================
key = 9

search(root, key, parent=None)

# ==================================
key = 8

search(root, key, parent=None)


# ==================================
key = 3

search(root, key, parent=None)

print("*" * 40)

# ==================================
print()
print("Search in For Loop on each key:")
for key in keys:
    search(root, key, parent=None)

print("*" * 40)
