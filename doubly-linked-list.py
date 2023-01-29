"""
	Doubly Linked List

	has the same concepts as the singly linked list but  with the addition of the previous cursor

	LinkedList:
		head

	Node:
		prev
		data
		next

	Example:
		NodeA:
			prev: None
			data: a
			next NodeB
		NodeB:
			prev: NodeA
			data: b
			next: None
	
	None <- a <-> b -> None
"""

class DoublyLinkedList:
	def __init__(self, head = None):
		self.head = head

	def add_beginning(self, node):
		
		node.next = self.head
		self.head.prev = node
		self.head = node
		
	def add_after(self, targetNode, newNode):
		# None <- b <-> a -> None
		node = self.head
		while node is not None:
			if node.data == targetNode.data:
				nextNode = node.next
				newNode.prev, newNode.next = node, nextNode
				node.next = newNode
				nextNode.prev = newNode
				node = None
			else:
				node = node.next

	def remove_beginning(self):
		pass
	def	remove_after(self):
		pass
	def	find(self):
		pass
	def	show(self):
		node = self.head
		nodes = list()

		# None <- a <-> b -> None

		while node is not None:
			nodes.append(node.data)
			node = node.next
		nodes.insert(0, "None")
		nodes.append("None")

		stringRepr = " <-> ".join(nodes)

		listString = stringRepr.split()

		listString[1] = " <- "
		listString[-2] = " -> "

		
		return " ".join(listString)

class Node:
	def __init__(self, data):
		self.prev = None
		self.data = data
		self.next = None


linkedList = DoublyLinkedList(Node("a"))
nodeB = Node("b")
linkedList.add_beginning(nodeB)
linkedList.add_after(nodeB, Node("c"))
print(linkedList.show())
