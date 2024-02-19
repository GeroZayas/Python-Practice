class Node:
	def __init__(self, data):
		self.prev = None
		self.next = None
		self.data = data

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def size(self):
		count = 0
		current = self.head
		while current:
			count += 1
			current = current.next
		return count

	def is_empty(self):
		return not self.head

	def push_back(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			self.tail = new_node
			return
		new_node.prev = self.tail
		self.tail.next = new_node
		self.tail = new_node

	def pop_back(self):
		if not self.head:
			return None
		data = self.tail.data
		if self.head == self.tail:
			self.head = None
			self.tail = None
			return data
		self.tail = self.tail.prev
		self.tail.next = None
		return data

	def push_front(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			self.tail = new_node
			return
		new_node.next = self.head
		self.head.prev = new_node
		self.head = new_node

	def pop_front(self):
		if not self.head:
			return None
		data = self.head.data
		if self.head == self.tail:
			self.head = None
			self.tail = None
			return data
		self.head = self.head.next
		self.head.prev = None
		return data

	def insert(self, index, value):
		if index < 0 or index > self.size():
			return IndexError("Index out of range")
		if index == 0:
			self.push_front(value)
			return
		if index == self.size():
			self.push_back(value)
			return
		new_node = Node(value)
		current = self.head
		for _ in range(index - 1):
			current = current.next
		new_node.prev = current
		new_node.next = current.next
		current.next.prev = new_node
		current.next = new_node

	def erase(self, index):
		if index < 0 or index > self.size():
			raise IndexError("Index out of range")
		if index == 0:
			self.pop_front()
			return
		if index == self.size() - 1:
			self.pop_back
			return
		current = self.head
		for _ in range(index):
			current = current.next
		current.prev.next = current.next
		current.next.prev = current.prev

	def display_forward(self):
		current = self.head
		while current:
			print(current.data, end=" -> ")
			current = current.next
		print()

	def display_backward(self):
		current = self.tail
		while current:
			print(current.data, end=" <- ")
			current = current.prev
		print()

	# Example usage:
linked_list = DoublyLinkedList()
linked_list.push_back(1)
linked_list.push_back(2)
linked_list.push_back(3)
print("Original linked list (forward):")
linked_list.display_forward()
print("Original linked list (backward):")
linked_list.display_backward()

print("Size of linked list:", linked_list.size())

linked_list.push_front(0)
print("Linked list after pushing front:")
linked_list.display_forward()

linked_list.insert(2, 1.5)
print("Linked list after inserting 1.5 at index 2:")
linked_list.display_forward()

print("Removing the first element:", linked_list.pop_front())
print("Linked list after popping the first element:")
linked_list.display_forward()

print("Removing the last element:", linked_list.pop_back())
print("Linked list after popping the last element:")
linked_list.display_forward()

linked_list.erase(1)
print("Linked list after erasing element at index 1:")
linked_list.display_forward()
