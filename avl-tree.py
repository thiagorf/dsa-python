"""
    Height of a node: the number of edges a node has based on the deepest leaf
    Balance fator: height of the left subtree - height of the right subtree
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        # why there so many articles out there with the height of 1?
        self.height = 0


"""
        33
       / \
      9  53
     /\   \
    8 21  61
      /
     11 
"""


class AvlTree:
    def add_node(self, root, value):
        if root == None:
            return Node(value)

        if value > root.data:
            root.right = self.add_node(root.right, value)
        else:
            root.left = self.add_node(root.left, value)

        root.height = 1 + max(self.findHeight(root.left), self.findHeight(root.right))

        return root

    def findHeight(self, node):
        if node == None:
            return -1
        return node.height


sequenceAfterRoot = [9, 53, 8, 21, 61, 11]

root = Node(33)
avlTree = AvlTree()

for node in sequenceAfterRoot:
    avlTree.add_node(root, node)


print("Node 61 height:  %i" % avlTree.findHeight(root.right.right))
print("Node 9 height:  %i" % avlTree.findHeight(root.left))
print("Root node (33) height: %i" % avlTree.findHeight(root))
