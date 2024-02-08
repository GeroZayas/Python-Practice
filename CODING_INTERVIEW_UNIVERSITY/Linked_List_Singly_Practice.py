class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    # =============ITERATOR=================
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # =============INSERT NODE BEGINNING=================
    def add_first(self, node):
        # the new node points to the old self.head
        node.next = self.head
        # the inserted node is the new head now
        self.head = node

    # =============INSERT NODE END=================
    # inserting nodes at the end
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        # traverse the whole list until reaching the end
        for current_node in self:
            pass
        # set the current_node as the last node
        # add the new node as the next value of that current_node
        current_node.next = node

    # =============INSERT NODE AFTER ANOTHER NODE=================
    # add after a particular node
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception(f"Node with data {target_node_data} not found")

    # =============INSERT NODE BEFORE ANOTHER NODE=================
    # add before a particular node
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        # Adding node before the head of the list
        # We can reuse add_first() because new node will be head now
        if self.head.data == target_node_data:
            return self.add_first(new_node)

        # keep track of the last-checked node using prev_node
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                # when target node found
                # use prev_node to rewire the next values
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    # =============REMOVE NODE=================
    # remove node
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    # =============REPR LIST=================
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


# ========================================================#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data


# ========================================================#
