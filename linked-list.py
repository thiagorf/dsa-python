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
		remove_beginning
		remove_after
		find
		show
"""


class LinkedList:
	def __init__(self, head = None):
		self.head = head

	def add_beginning(self, node):
		node.pointer, self.head = self.head, node
		
	def add_after(self, targetNode, newNode):
		node = self.head

		while node is not None:
			if targetNode.data == node.data:
				attachedNode = targetNode.pointer
				targetNode.pointer = newNode
				newNode.pointer = attachedNode
				node = None
			else:
				node = node.pointer
		

	def remove_beginning(self):
		new_head = self.head.pointer

		self.head.pointer = None
		self.head = new_head	
		
	def remove_after(self):
		pass
	
	def find(self, targetNode):
		node = self.head
		requiredNode = None


		while node is not None:
			if node.data == targetNode.data:
				requiredNode = node
				node = None
			else:
				node = node.pointer

		if requiredNode is None:
			return "Invalid node"
		else:
			return requiredNode

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

nodeC = Node("c")

linkedList.add_beginning(nodeC)
linkedList.add_after(nodeC, Node("d"))
print(linkedList.show())

print(linkedList.find(node1))
