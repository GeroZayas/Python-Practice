from collections import deque


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None

    def __repr__(self):
        return str(self.data)

    def children(self):
        if not self.left and not self.right:
            return "No Children"
        if not self.left:
            return f"{self.data}'s ->", "[only right  child:]", self.right.data
        if not self.right:
            return f"{self.data}'s ->", "[only left  child:]", self.left.data
        else:
            return f"{self.data}'s children ->", self.left.data, self.right.data


root = Node("Hobbies")
root.left = Node("Physical")
root.right = Node("Intellectual")

root.left.left = Node("Boxing")
root.left.right = Node("Running")

root.right.right = Node("Chess")

print(root.children())

print(root.left.children())
print(root.right.children())


# =========================================
# Is In Tree? Function
# =========================================
def is_in_tree(root, key) -> bool:
    def bfs(root, key):
        if root:
            queue = deque([root])
            while queue:
                node = queue.popleft()
                if node.data == key:
                    return True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return False

    return bfs(root, key)


search_for = "Boxing"

print(f"Is in tree? -> {search_for}")
print(is_in_tree(root, search_for))
