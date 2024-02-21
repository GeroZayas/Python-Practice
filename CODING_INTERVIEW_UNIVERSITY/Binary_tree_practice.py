from collections import deque


# Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __repr__(self):
        return f"{self.data}"


# Initialize the Tree
root = Node("Hobbies")
child1 = Node("Physical")
child2 = Node("Intellectual")
root.left = child1
root.right = child2

child1.left = Node("Football")
child1.right = Node("MMA")
child2.left = Node("Chess")
child2.right = Node("Writing")

separator = lambda: print("-" * 45)


# ==================================
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


# ==================================
def bfs(root):
    if root:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# ==================================
def bfs_reversed(root):
    revrsd = deque()
    if root:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            revrsd.appendleft(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    print("\n".join(list(revrsd)))


# ==================================
def preorder_dfs(root):
    if root:
        print(root.data)
        preorder_dfs(root.left)
        preorder_dfs(root.right)


# ==================================
separator()
print("Preorder Traversal:")
separator()

preorder_dfs(root)


# ==================================
separator()
print("Inorder Traversal:")
separator()

inorder(root)

# ==================================
separator()
print("BFS Traversal:")
separator()

bfs(root)

# ==================================
separator()
print("Reversed BFS Traversal:")
separator()

bfs_reversed(root)
