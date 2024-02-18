# Implement a Singly LinkedList
# We have nodes and each node has a pointer to the next one

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __repr__(self):
		return f"{self.data}"


class SinglyLinkedList:
	def __init__(self):
		self.head = None

	def display(self):
		current = self.head
		while current:
			print(current.data, end=" -> ")
			current = current.next
		print()	

	def size(self):
		count = 0
		current = self.head
		while current:
			count += 1
			current = current.next

		return count

	def is_empty(self):
		return self.head is None

	def push_back(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next

		last_node.next = new_node

	def pop_back(self):
		if not self.head:
			return None
		elif not self.head.next:
			data = self.head.data
			self.head = None
			return data
		current = self.head

		# we want to stop when current.next is the last node, 
		# so we stop when current.next.next is None
		while current.next.next:
			current = current.next
		data = current.next.data
		current.next = None
		return data

	def insert(self, index, value):
		if index < 0 or index > self.size():
			raise IndexError("Index out of range")
		new_node = Node(value)
		if index == 0:
			new_node.next = self.head
			self.head = new_node
			return
		current = self.head
		for _ in range(index - 1):
			current = current.next

		new_node.next = current.next
		current.next = new_node

	def reverse_list(self):
		prev = None
		current = self.head
		while current:
			next_node = current.next
			current.next = prev
			prev = current
			current = next_node

		self.head = prev

	def push_front(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def pop_front(self):
		if not self.head:
			return None
		data = self.head.data
		self.head = self.head.next
		return data

	def head(self):
		if not self.head:
			return None
		return self.head.data

	def tail(self):
		if not self.head:
			return None
		current = self.head
		while current:
			current = current.next
		return current.data

	def erase(self, index):
		if index < 0 or index >= self.size():
			raise IndexError("Index out of range")
		if index == 0:
			self.head = self.head.next
			return
		current = self.head
		for _ in range(index-1):
			current = current.next
		current.next = current.next.next

	def remove_value(self, value):
		current = self.head
		if current is None:
			return
		if current.data == value:
			self.head = current.next
			return
		while current.next:
			if current.next.data == value:
				current.next = current.next.next
				return
			current = current.next

# Example usage:
linked_list = SinglyLinkedList()
linked_list.push_back(1)
linked_list.push_back(2)
linked_list.push_back(3)
linked_list.push_back(4)
print("Original linked list:")
linked_list.display()

print("Size of linked list:", linked_list.size())

linked_list.reverse_list()
print("Reversed linked list:")
linked_list.display()

print("Removing the first element:", linked_list.pop_front())
print("Linked list after popping the first element:")
linked_list.display()

print("Removing the last element:", linked_list.pop_back())
print("Linked list after popping the last element:")
linked_list.display()

linked_list.insert(1, 5)
print("Linked list after inserting 5 at index 1:")
linked_list.display()

print("Head of linked list:", linked_list.head)
print("Tail of linked list:", linked_list.tail)

linked_list.erase(1)
print("Linked list after erasing element at index 1:")
linked_list.display()

linked_list.remove_value(2)
print("Linked list after removing value 2:")
linked_list.display()

