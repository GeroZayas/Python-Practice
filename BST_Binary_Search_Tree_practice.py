# -----CLASS NODE------------------------------------
class Node:
    def __init__(self, data = None):
        self.data = data
        self.right = self.left = None
# ---------------------------------------------------


# IN_ORDER Traversal of the Tree (DFS)
# ---------------------------------------------------
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
# ---------------------------------------------------


# BFS TRAVERSAL
# ---------------------------------------------------
def bfs_traversal(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end = " ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
# ---------------------------------------------------


# Initialize the Tree
# ---------------------------------------------------
root = Node(5)
child1 = Node(3)
child2 = Node(7)
root.left = child1
root.right = child2 

child1.left = Node(-2)
child1.right = Node(4)
child2.left = Node(6)
child2.right = Node(10)

# SEPARATOR Printer
# ---------------------------------------------------
separator = lambda: print("\n", "-" * 45)

separator()

print('In order traversal: ')
inorder(root)


# INSERT KEY into BST
# Recursive function to insert a key into a BST
# ---------------------------------------------------
def insert(root, key):
    if not root:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root
# ---------------------------------------------------

insert(root, 11)

separator()
print('In order traversal: ')
inorder(root)

separator()
print('BFS traversal: ')
bfs_traversal(root)

insert(root, 8)

separator()
print('BFS traversal: ')
bfs_traversal(root)

insert(root, 9)

separator()
print('BFS traversal: ')
bfs_traversal(root)


# CONSTRUCT A BST from given Keys
# BST CONSTRUCTOR
# ---------------------------------------------------
def constructBST(keys):
    root = None
    for key in keys:
        root = insert(root, key)

    return root
# ---------------------------------------------------

separator()
# Construct new Tree
tree_2 = [15, 10, 20, 8, 12, 16, 25]

root_2 = constructBST(tree_2)
print("\nIn order Root 2")
inorder(root_2)
separator()
print("BFS Traversal Root 2")
bfs_traversal(root_2)