"""
	Queue Data Structure

    How it works: Queue uses the FIFO acronym, first in last out, so
    the first element added to the queue is the first one to leave

    methods:
        enqueue: add an element in the last position of the queue
        dequeue: removes the first element in the queue
"""

class Queue:

	def __init__(self):
		self.queue = list()

	def enqueue(self, data):
		self.queue.append(data)
		
	def dequeue(self):
		if len(self.queue) - 1 == -1:
			print("Queue is empty")
			return
		else:
			# first element
			self.queue.pop(0)

	def peek(self):
		if len(self.queue) == 0:
			print("Queue is empty")
		else:
			print("|%i| <- Next element to be dequeue" % self.queue[0])
	def show(self):
		print(self.queue)

	

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.show()

queue.dequeue()
queue.show()
queue.peek()
queue.dequeue()
queue.peek()