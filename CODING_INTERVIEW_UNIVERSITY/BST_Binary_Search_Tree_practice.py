from collections import deque


# ======================================
# CLASS NODE
# ======================================
class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = self.left = None


# ======================================
# IN ORDER Traversal
# ======================================
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# ======================================
# BFS Traversal
# ======================================
def bfs_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# ======================================
# Initialize the tree
# ======================================
root = Node(5)
child1 = Node(3)
child2 = Node(7)
root.left = child1
root.right = child2

child1.left = Node(-2)
child1.right = Node(4)
child2.left = Node(6)
child2.right = Node(10)

# ======================================
# Terminal Separator printer
# ======================================
separator = lambda: print("\n", "=" * 90)

separator()


# ==================================
print("In order traversal: ")
inorder(root)


# ======================================
# Recursive INSERT Function
# ======================================
def insert(root, key):
    if not root:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


# ---------------------------------------------------


# ======================================
# Iterative INSERT Function
# ======================================
def iterative_insert(root, key):
    current = root  # we start with the root node
    parent = None  # pointer to store the parent of the current node
    if root is None:  # if there's no root (tree is empty), we create one
        return Node(key)
    while current:  # traverse the tree and find parent node of given key
        parent = current
        if key < current.data:  # if key is less, we go to left subtree
            current = current.left
        else:
            current = current.right  # otherwise, we go to the right subtree
    if key < parent.data:  # construct a node and assign it to appropiate parent pointer
        parent.left = Node(key)
    else:
        parent.right = Node(key)
    return root


# ---------------------------------------------------

insert(root, 11)

separator()
print("In order traversal: ")
inorder(root)

separator()
print("BFS traversal: ")
bfs_traversal(root)

insert(root, 8)

separator()
print("BFS traversal: ")
bfs_traversal(root)

insert(root, 9)

separator()
print("BFS traversal: ")
bfs_traversal(root)

root.right.right.right.right = Node(-4)

insert(root, 1)


# ======================================
# BST Constructor Function
# ======================================
def constructBST(keys):
    root = None
    for key in keys:
        root = insert(root, key)

    return root


# --------------------------------------- #
# ----------- NEW ROOT 2 TREE ----------- #
# --------------------------------------- #

separator()
# Construct new Tree
tree_2 = [15, 10, 20, 8, 12, 16, 25, 4]

# We construct root_2 BST here:
root_2 = constructBST(tree_2)

# ---------------------------------------------------
print("\nIn order Root 2")
inorder(root_2)

# ---------------------------------------------------
separator()

# ---------------------------------------------------
print("BFS Traversal Root 2")
bfs_traversal(root_2)


# ============================================
# Recursive function to SEARCH in a given BST
# ============================================
def search(root, key, parent):
    # if the key is not present in the key
    if root is None:
        print("Key not found")
        return

    # if the key is found
    if root.data == key:
        if parent is None:
            print(f"The node with key {key} is root node")
        elif key < parent.data:
            print(
                f"The given key [{key}] is the left node of the node with key",
                parent.data,
            )
        else:
            print(
                f"The given key [{key}] is the right node of the node with key",
                parent.data,
            )

        return

    # if the given key is less than the root node, recur for the left subtree;
    # otherwise, recur for the right subtree

    if key < root.data:
        search(root.left, key, root)
    else:
        search(root.right, key, root)


# ============================================
# IS IN? -> Recursive function to check if Key is in BST
# ============================================
def is_in_tree(root, key):
    if not root:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return is_in_tree(root.left, key)
    else:
        return is_in_tree(root.right, key)


# -------------------------------------------
separator()
check_key = 8
print("Is key {} in tree 'root 1'?".format(check_key))
print(is_in_tree(root, check_key), end="\n\n")

check_key = 14
print("Is key {} in tree 'root 1'?".format(check_key))
print(is_in_tree(root, check_key), end="\n\n")

check_key = 25
print("Is key {} in tree 'root 2'?".format(check_key))
print(is_in_tree(root_2, check_key), end="\n\n")

# ---------------------------------------------------
separator()
# ---------------------------------------------------
print("SEARCH")
search(root_2, 16, None)

# ---------------------------------------------------
separator()


# ======================================
# CREATE ADJANCENCY LIST Function
# ======================================
def create_adj_list(root, adjacency_list):
    """
    Creates Adjacency List to represent each Node and its children
    """
    if root:
        adjacency_list[root.data] = []
        if root.left:
            adjacency_list[root.data].append(root.left.data)
            create_adj_list(root.left, adjacency_list)
        if root.right:
            adjacency_list[root.data].append(root.right.data)
            create_adj_list(root.right, adjacency_list)


# ---------------------------------------------------
adjacency_list = {}

# ---------------------------------------------------
res = create_adj_list(root, adjacency_list)

# ---------------------------------------------------
print("This is the adjacency_list de root 1:\n")
for node, neighbor in adjacency_list.items():
    print(node, neighbor)


# ---------------------------------------------------
separator()

# ---------------------------------------------------
adjacency_list = {}

# ---------------------------------------------------
res = create_adj_list(root_2, adjacency_list)
print("This is the adjacency_list of root_2:\n")
for node, neighbor in adjacency_list.items():
    print(node, neighbor)

separator()


# ======================================
# GET NODE COUNT Function
# ======================================
def get_node_count(node):
    if not node:
        return 0
    return 1 + get_node_count(node.left) + get_node_count(node.right)


print(
    f"""
    == Get Node Count Function == 
    
    Root 1:
    -> {get_node_count(root)}
    
    Root 2:
    -> {get_node_count(root_2)}
    """
)

separator()


# ======================================
# GET MIN VALUE Function
# ======================================
def get_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.data


print("Min Value in Root 1:")
print(get_min(root))

print("Min Value in Root 2:")
print(get_min(root_2))


separator()


# ======================================
# IS BST Function
# ======================================
def is_bst(root, min_value, max_value):
    node = root
    if node is None:
        return True
    if node.data < min_value or node.data > max_value:
        return False
    return is_bst(node.left, min_value, node.data - 1) and (
        is_bst(node.right, node.data + 1, max_value)
    )


print("Is BST?:")
print("Root 1 = ", is_bst(root, min_value=float("-inf"), max_value=float("inf")))
print("Root 2 = ", is_bst(root_2, min_value=float("-inf"), max_value=float("inf")))
