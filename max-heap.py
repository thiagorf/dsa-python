"""
			 25
			/ \
		   16  24
		  /\   /\
         5 11 19 1
	    /\ /
	   2 3 5
		

	   index = [ 0,   1, 2, 3,  4,  5, 6, 7, 8, 9]	
	   value = [25, 16, 24, 5, 11, 19, 1, 2, 3, 5]

	   i = 3
	   parent(i) = (i - 1) /2 = 16
	   leftChild(i) = (i *2) + 1 = 2
	   rightChild(i) = (i *2) + 2 = 3
"""


class MaxHeap:
    def __init__(self, maxheap):
        self.maxheap = list(maxheap)

    """
		Add an element at the end of the list, and check if the parent is a greater
		if it is swapped and check the next parent
	"""

    def push(self, data):
        self.maxheap.append(data)
        self.__swapUp(len(self.maxheap) - 1)

    def __swapUp(self, lastElementIndex):
        parent = int((lastElementIndex - 1) / 2)

        if self.maxheap[parent] < self.maxheap[lastElementIndex]:

            self.__swap(parent, lastElementIndex)
            self.__swapUp(parent)

    def __swap(self, parent, children):
        self.maxheap[parent], self.maxheap[children] = (
            self.maxheap[children],
            self.maxheap[parent],
        )

    """
		Swap the first element with the last one in the list
		then remove the last element
	"""

    def pop(self):
        # swap the first and the last one
        self.__swap(0, -1)
        # remove the last one previously the greater number in the heap
        self.maxheap.pop()

        rightChild = int((0 * 2) + 2)

        if self.maxheap[rightChild] > self.maxheap[0]:
            self.__swapBottom(0)

    def __swapBottom(self, parent):
        # check left and right
        left = int((parent * 2) + 1)
        right = int((parent * 2) + 2)
        largest = parent
        # check len(self.maxheap) > left
        if len(self.maxheap) > left and self.maxheap[left] > self.maxheap[largest]:
            largest = left
        if len(self.maxheap) > right and self.maxheap[right] > self.maxheap[largest]:
            largest = right
        if largest != parent:
            self.__swap(parent, largest)
            self.__swapBottom(largest)

    def peek(self):
        if self.maxheap[0]:
            print(self.maxheap[0])
        else:
            print("Empty MaxHeap")

    def show(self):
        print(self.maxheap)


maxHeap = MaxHeap([25, 16, 24, 5, 11, 19, 1, 2, 3, 5])

maxHeap.push(12)
maxHeap.show()
maxHeap.pop()
maxHeap.show()
