"""
	Each record in the linked list is called an element or Node
	A node contains the address for the next node and a field with data
	The head is the first node in a linked list, and the tail can be the rest of the list or the last node

	LinkedList:
		head: null
	Node
		data: data
		pointer: Node or None

	Operations
		insert_beginning
		insert_after
		remove_veginning
		remove_after
		find
		show
"""


class LinkedList:
	def __init__(self, head = None):
		self.head = head

	def add_beginning(self, node):
		node.pointer, self.head = self.head, node
		
	def add_after(self):
		pass

	def remove_beginning(self):
		new_head = self.head.pointer

		self.head.pointer = None
		self.head = new_head	
		
	def remove_after(self):
		pass
	
	def find(self, node):
		pass

	def show(self):
		node = self.head
		nodes = list()

		while node is not None:
			nodes.append(node.data)
			node = node.pointer
		nodes.append("None")

		return " -> ".join(nodes)

	

class Node:
	def __init__(self, data):
		self.data = data
		self.pointer = None

	def __repr__(self):
		return self.data


node1 = Node("a")

linkedList = LinkedList(node1)

linkedList.add_beginning(Node("b"))


print(linkedList.show())
linkedList.remove_beginning()
print(linkedList.show())
