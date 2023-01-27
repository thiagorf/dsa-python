
"""
	Stack Data Structure:

    How it works: Stack uses the LIFO acronym last in first out, so
    the first element added to the stack is the last one to leave

    It has two methods:
        push: add an element in the last place in the stack
        pop: removes the last elements in the stack
"""


class Stack:

	def __init__(self):
		self.stack = list()
		

	def push(self, data):
		self.stack.append(data)
	def pop(self):
		if len(self.stack) - 1 == -1:
			print("Stack is already empty")
		else:
			self.stack.pop()

	def show(self):

		if not self.stack:
			print("| | <- stack is empty",end='\n\n')
			return

		for i, stackItem in enumerate(reversed(self.stack)):
			length = len(self.stack)

			if length == 1:
				print("|%i| <- unique element" % stackItem,end='\n')
				break

			if i != length - 1:
				if i == 0:
					print("|%i| <- last element" % stackItem,end='\n')
				else:	
					print("|%i|" % stackItem,end='\n')
			else:
				print("|%i| <- first element" % stackItem,end='\n\n')	
	def peek(self):
		if len(self.stack) != 0:
			print("%s  top of the stack" % self.stack[-1:])
		else:
			print("Stack is empty!")


stack = Stack()
print("Stack example: Last in First out(LIFO)")

stack.push(1)
stack.push(6)
stack.push(8)
stack.push(12)

stack.show()
stack.peek()

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.show()
stack.peek()