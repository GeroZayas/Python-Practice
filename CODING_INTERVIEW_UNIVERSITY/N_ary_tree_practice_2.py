from collections import deque


# implement a n-ary tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __repr__(self):
        if not isinstance(self.data, str):
            self.data = str(self.data)

        return f"{self.data}"

    def add_child(self, new_child):
        self.children.append(new_child)


# Initialize the Tree
root = TreeNode("Hobbies")
child1 = TreeNode("Physical")
child2 = TreeNode("Intellectual")
root.add_child(child1)
root.add_child(child2)

child1.add_child(TreeNode("Football"))
child1.add_child(TreeNode("MMA"))
child2.add_child(TreeNode("Chess"))
child2.add_child(TreeNode("Writing"))
child2.add_child(TreeNode("Reading"))

# print(root.children)

# IMPLEMENT DF Traversals in N-ary trees

# DF Traversal N-Ary tree


# -------------------------------------------
# PREORDER TRAVERSAL
def preorder_df_traversal(root):
    if root:
        print(root.data)
        if root.children:
            for child in root.children:
                preorder_df_traversal(child)


print(preorder_df_traversal(root))


def separator():
    separator = "*" * 40
    print(separator)


separator()

# -------------------------------------------
# DF Traversal N-Ary tree


def postorder_df_traversal(root):
    if root:
        if root.children:
            for child in root.children:
                postorder_df_traversal(child)
        print(root.data)


print(postorder_df_traversal(root))


# -------------------------------------------
# LEVEL TRAVERSAL or BFS Traversal
def bfs_traversal(root):
    # we use a queue for this
    # we can use deque for this
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data)
        if node.children:
            for child in node.children:
                queue.append(child)


separator()
print("This is BFS Traversal:")
separator()
print(bfs_traversal(root))

# -------------------------------------------

# SEARCH in N-ary Tree

separator()


# BFS
def bfs_search(root):
    if not root:
        return None
    queue = deque([root])
    counter = 0
    while queue:
        counter += 1
        node = queue.popleft()
        if node.data == target:
            return f"Target found in node {node}, counter {counter}"
        for child in node.children:
            queue.append(child)


target = "MMA"
print(f"This is BFS search of target {target}")

print(bfs_search(root))

separator()

# -------------------------------------------


# DFS
def dfs_search(root):
    if not root:
        return None
    stack = [root]
    counter = 0
    while stack:
        # print("This is stack",stack)
        counter += 1
        node = stack.pop()
        if node.data == target:
            return f"Target found in node {node}, counter {counter}"
        for child in node.children:
            stack.append(child)


print(f"This is DFS search of target {target}")

print(dfs_search(root))
