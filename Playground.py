keys = [5, 4, 6, 2, 9, 3, 8]


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if not root:
        return TreeNode(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def constructBST(keys):
    root = None
    for key in keys:
        root = insert(root, key)
    return root
