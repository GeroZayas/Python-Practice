# binary search tree 
def  binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

arr = [1,2,3,4,5,6,7,8,9,10]

print(binary_search(arr,8))

# tree  traversal
def  in_order(tree):
    if tree:
        in_order(tree.left)
        print(tree.val)
        in_order(tree.right)
        
def pre_order(tree):
    if tree:
        print(tree.val)
        pre_order(tree.left)
        pre_order(tree.right)
        
def post_order(tree):
    if tree:
        post_order(tree.left)
        post_order(tree.right)
        print(tree.val)
        
# tree structure
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
# tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.left = Node(6)
root.right.right = Node(7)

# tree traversal   
in_order(root)

pre_order(root)
post_order(root)

