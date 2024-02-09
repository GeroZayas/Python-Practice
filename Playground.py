class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

    def __repr__(self):
        return f"{self.data}"


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def find_node(self, root, key):
        while root is not None:
            if key < root.data:
                root = root.left
            elif key > root.data:
                root = root.right
            else:
                return root
        return None

    def get_min(self, root):
        while root.left is not None:
            root = root.left
        return root

    def get_successor(self, root, key):
        # find the node with the value key in the tree
        # save that node on a variable named 'current'
        current = self.find_node(root, key)

        # if current is None, does not exist
        # return None -> no successor here
        if not current:
            return None

        # if current has a right child , then
        # use the get_min() function to find
        # the minimum value in that right subtree
        if current.right:
            return self.get_min(current.right)

        # if current didn't have a right child
        # then we need create a new var to get hold of
        # a possible successor value
        successor = None

        # while we keep having a node
        # we check if our key value is less
        # of the node's data value
        while root is not None:
            if key < root.data:
                # if it is less, then, as we will go to
                # the left child, and turn it into the new root
                # we save our root bode as the successor
                # if case we find a value less than our key value
                # there in the left child node
                successor = root
                # this is how we turn the left child node into
                # the new root so as to keep traversing the tree
                root = root.left
            elif key > root.data:
                # if our key value is more than the value in our root
                # we go to the right child node
                # so root now because that
                root = root.right
            # or now, we have found a node whose value
            # is equal to our key value and, as we had
            # save the value of its parent in ur successor var
            # we can break the while loop and return our
            # sucessor
            else:
                break
        return successor


# Ejemplo de uso:
bst = BST()
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    bst.root = bst.insert(bst.root, key)

successor_key = 30
successor_node = bst.get_successor(bst.root, successor_key)

# if successor_node is not None:
#   print(f"El sucesor de {successor_key} es {successor_node.data}")
# else:
#   print(f"No se encontró sucesor para {successor_key}")
