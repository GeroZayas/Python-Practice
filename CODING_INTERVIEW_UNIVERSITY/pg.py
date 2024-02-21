# Binary Search Tree
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __repr__(self):
        return f"{self.data}"

    def bfs(self):
        if self:
            queue = deque([self])
            while queue:
                node = queue.popleft()
                print(node.data, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


keys_to_build_bst = [1, 2, 3, 4, 5, 6]


def constructBST(keys):
    root = None
    for key in keys:
        root = insert(root, key)
    return root


def insert(root, key):
    if not root:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


BST = constructBST(keys_to_build_bst)

print(BST.bfs())
