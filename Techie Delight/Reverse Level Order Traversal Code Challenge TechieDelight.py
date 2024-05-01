"""

Given the root of a binary tree, return the 
reverse level order traversal of its nodes' values. 
The solution should consider the binary tree nodes 
level by level in bottom-up order from left to right, 
i.e., process all nodes of the last level first, 
followed by all nodes of the second last level, and so on.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /		  / \
	 /	  	 /	 \
	4		5	  6
		   / \
		  /   \
		 7	   8

Output: [7, 8, 4, 5, 6, 2, 3, 1]

"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        if not isinstance(self.data, str):
            self.data = str(self.data)
        return self.data


def find_reverse_level_order(root: TreeNode) -> list[int]:
    from collections import deque

    result = deque()
    queue = deque([root])
    while queue:
        level_values = []
        for _ in range(len(queue)):
            node = queue.popleft()
            if node:
                level_values.append(node.data)
                queue.append(node.left)
                queue.append(node.right)
        if level_values:
            result.appendleft(level_values)
    return sum(result, [])


if __name__ == "__main__":
    r"""BINARY TREE
	          hobbies
	        /       \
	   physical   intelectual
	    /    \      /       \
	football mma  reading  coding 
	"""

    root = TreeNode("Hobbies")
    root.left = TreeNode("Physical")
    root.right = TreeNode("Intelectual")
    root.left.left = TreeNode("Football")
    root.left.right = TreeNode("MMA")
    root.right.left = TreeNode("Reading")
    root.right.right = TreeNode("Coding")
    r = find_reverse_level_order(root)
    print(r)
