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
    def __init__(self, head=None):
        self.head = head
        self.size = 0 if head == None else 1

    def add_beginning(self, node):
        if self.size == 0:
            self.head = node
            self.size += 1
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.size += 1

    def add_after(self, targetNode, newNode):
        # None <- b <-> a -> None
        node = self.head
        initialSize = self.size
        while node is not None:
            if node.data == targetNode.data:
                nextNode = node.next
                newNode.prev, newNode.next = node, nextNode
                node.next = newNode
                nextNode.prev = newNode
                node = None
                self.size += 1
            else:
                node = node.next
        if initialSize == self.size:
            # If the size doesn't change, it means that the target node doesn't exist
            print("Invalid target node")

    def remove_beginning(self):
        # chnage the next and prev cursor
        head = self.head
        self.head = head.next
        self.head.prev = head.prev

    def remove_after(self, target):
        current = self.head

        while current is not None:
            if current.data == target.data:
                # c
                nextNode = current.next
                current.prev.next = nextNode
                current = None
            else:
                current = current.next

    def find(self, target):
        current = self.head
        node = None

        while current is not None:
            if current.data == target.data:
                node = current.data
                current = None
            else:
                current = current.next
        return node

    def show(self):
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
nodeC = Node("c")
linkedList.add_after(nodeB, nodeC)
linkedList.add_after(Node("sdsa"), Node("sdasdf"))
print(linkedList.show())
print("list size: %i" % linkedList.size)
linkedList.remove_beginning()
linkedList.add_beginning(nodeB)
linkedList.remove_after(nodeC)
print(linkedList.show())

print("Node c exist? %s" % linkedList.find(nodeC))

emptyList = DoublyLinkedList()
emptyList.add_beginning(Node("h"))
print(emptyList.show())
print(emptyList.size)
