from dataclasses import dataclass


class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer


@dataclass
class LinkedList:
    def __init__(self):
        self.head = None

    def add_node_front(self, data):
        self.head = Node(data, self.head)

    def add_node_end(self, data):
        if not self.head:
            self.head = Node(data, None)
        current_node = self.head
        while current_node.pointer:
            current_node = current_node.pointer
        current_node.pointer = Node(data, None)

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end=" => ")
            n = n.pointer
        print()


my_linked_list = LinkedList()

my_linked_list.add_node_front("Abraham")
my_linked_list.add_node_end("Bella")
my_linked_list.add_node_end("Charlie")

print(my_linked_list.print_list())
