from random import randint
from collections import deque


class Node:
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.right = self.left = None

    def __repr__(self):
        return f"{self.key, self.data}"


def constructBST(keys: dict) -> Node:
    root = None
    for key, data in keys.items():
        root = insert(root, key, data)
    return root


def insert(root, key, data):
    if not root:
        return Node(key, data)
    if key < root.key:
        root.left = insert(root.left, key, data)
    else:
        root.right = insert(root.right, key, data)
    return root


def delete_node(root, key):
    parent = None
    curr = root
    while curr and curr != key:
        parent = curr
        if key < curr.data:
            curr = curr.left
        else:
            curr = curr.right


# random_keys = [randint(1, 100) for _ in range(6)]
num_keys = [1, 2, 3, 4, 5]
the_data = "Gero Mar Elisa Enrique Rafa".split()
keys = dict(zip(num_keys, the_data))

print(
    f"""
    These are the keys
    {keys}
    """
)

tree = constructBST(keys)
print(
    f"""
    This is the tree
    {tree}"""
)


def bfs_traversal(root):
    if root:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.key, "->", node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


print(bfs_traversal(tree))


def create_adj_list(root, adjacency_list):
    if root:
        adjacency_list[root.data] = []
        if root.left:
            adjacency_list[root.data].append((root.left.key, root.left.data))
            create_adj_list(root.left, adjacency_list)
        if root.right:
            adjacency_list[root.data].append((root.right.key, root.right.data))
            create_adj_list(root.right, root.data)
    return adjacency_list


adjacency_list = {}

adjacency_list_tree = create_adj_list(tree, adjacency_list)

print(
    f"""
    This is the adjacency list:
    {adjacency_list_tree}

    """
)
