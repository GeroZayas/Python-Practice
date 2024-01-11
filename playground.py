class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
    
    def __repr__(self) -> str:
        return " ".join(str(c.value) for c in self.children)

# Example of creating a tree
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)

root.add_child(child1)
root.add_child(child2)

child1.add_child(TreeNode(4))
child1.add_child(TreeNode(5))

child2.add_child(TreeNode(6))

# Visualizing the tree structure
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

print(root)