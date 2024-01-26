class TreeNode:
	def __init__(self, data = None):
		self.data = data
		self.left = self.right = None 

def bfs_traversal(root):
	if root:
		queue = [root]
		while queue:
			node = queue.pop(0)
			print(node.data, end=' ')
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

tree = [3,9,20,None, None,15,7]

"""
			3
		   /  \
		  9    20
		      /   \
		     15    7
"""

root = TreeNode(tree[0])
root.left = TreeNode(tree[1])
root.right = TreeNode(tree[2])
root.right.left = TreeNode(tree[5])
root.right.right = TreeNode(tree[6])

print(bfs_traversal(root))

def is_balanced(root) -> bool:
	def dfs(root):
		if not root:
			# True for balanced and 0 for distance
			return [True, 0]

		left, right = dfs(root.left), dfs(root.right)
		# to be balanced left must be true, right must be true
		# and the absolute value of distance must be <= 1
		balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
		return [balanced, 1 + max(left[1], right[1])]

	return dfs(root)[0] 

print(is_balanced(root))
