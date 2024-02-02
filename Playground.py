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
