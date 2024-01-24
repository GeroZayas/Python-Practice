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
root = TreeNode('Hobbies')
child1 = TreeNode('Physical')
child2 = TreeNode('Intellectual')
root.add_child(child1)
root.add_child(child2)

child1.add_child(TreeNode("Football"))
child1.add_child(TreeNode("MMA"))
child2.add_child(TreeNode("Chess"))
child2.add_child(TreeNode("Writing"))
child2.add_child(TreeNode("Reading"))

print(root.children)

# IMPLEMENT DF Traversals in N-ary trees
# DF Traversal N-Ary tree
def preorder_df_traversal(root):
    if root:
        print(root.data)
        if root.children:
            for child in root.children:
                preorder_df_traversal(child)

print(preorder_df_traversal(root))

separator = '*' * 40

print(separator)

# DF Traversal N-Ary tree
def postorder_df_traversal(root):
    if root:
        if root.children:
            for child in root.children:
                postorder_df_traversal(child)
        print(root.data)

print(postorder_df_traversal(root))

