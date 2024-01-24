# BINARY TREE IMPLEMENTATION
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        if not isinstance(self.data, str):
            self.data = str(self.data)
        return f"{self.data}"


# Initialize the Tree
root = TreeNode('Hobbies')
child1 = TreeNode('Physical')
child2 = TreeNode('Intellectual')
root.left = child1
root.right = child2 

child1.left = TreeNode("Football")
child1.right = TreeNode("MMA")
child2.left = TreeNode("Chess")
child2.right = TreeNode("Writing")

separator = lambda: print("-" * 45)


separator()
print("Inorder Traversal:") 
separator()

# IMPLEMENT DFS Traversals
# in order
def inorder_dfs(root):
    if root:
        inorder_dfs(root.left)
        print(root.data)
        inorder_dfs(root.right)


print(inorder_dfs(root))

separator()

print("Preorder Traversal:") 
separator()
# IMPLEMENT DFS Traversals
# preorder
def preorder_dfs(root):
    if root:
        print(root.data)
        preorder_dfs(root.left)
        preorder_dfs(root.right)

print(preorder_dfs(root))

