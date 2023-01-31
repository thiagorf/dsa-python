class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return str(self.data)


def find(root, value):
    if root == None:
        return False

    if value == root.data:
        return True

    if value > root.data:
        return find(root.right, value)
    else:
        return find(root.left, value)


def addNode(root, value):
    if root == None:
        return Node(value)

    if value > root.data:
        root.right = addNode(root.right, value)
    else:
        root.left = addNode(root.left, value)
    return root


# 9 == root.right = addNode(9, 10), addNode(None, 10)


def removeNode(root, value):
    if root == None:
        return root

    if value > root.data:
        root.right = removeNode(root.right, value)
    else:
        root.left = removeNode(root.left, value)


root = Node(5)
root.left = Node(3)
root.right = Node(9)

root.left.left = Node(1)
root.left.right = Node(4)

root.right.left = Node(6)


print("6 is a valid node? %s" % find(root, 6))
print("8 is a valid node? %s" % find(root, 8))

print("add Node(%s)" % addNode(root, 10))
print("10 is a valid node? %s" % find(root, 10))
