class LinkedList:
    def __init__(self, keys: list = None):
        self._head = None
        if keys is not None:
            for i in reversed(range(len(keys))):
                self._head = Node(data=keys[i], next=self._head)

    def __repr__(self) -> str:
        if self._head:
            while self._head:
                print(self._head.data, end=" -> ")
                self._head = self._head.next
            print("None")
        elif not self._head:
            return "Empty List"
        return ""


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


llist = LinkedList()
print("This is llist 1 that is empty:\n")
print(llist)

print()

print("This is llist 2 that is full:\n")
llist2 = LinkedList(["Gero", "Mar", "Sonia"])
print(llist2)
