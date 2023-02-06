"""
    Height of a node: the number of edges a node has based on the deepest leaf
    Balance fator: height of the left subtree - height of the right subtree
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        # why are there so many articles out there with the height of 1?
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
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(str(root.data) + " -> ", end="")
            self.inorder(root.right)

    def add_node(self, root, value):
        if root == None:
            return Node(value)

        if value > root.data:
            root.right = self.add_node(root.right, value)
        else:
            root.left = self.add_node(root.left, value)

        root.height = max(self.findHeight(root.left), self.findHeight(root.right))
        # {-1, 0, 1}
        balance = self.findBalance(root)

        # balance factor > 1
        # tree is left heavy
        if balance > 1:
            if value < root.left.data:
                return self.rightRotate(root.right)
            else:
                # left-right rotate is only possible
                # when the left child of a node is less than the new node
                """
                       21  <- root in this subtree
                      /
                     11	<- left child of root
                      \
                         12 < - new Node
                """
                root.left = self.leftRotate(root.left)

                return self.rightRotate(root.right)

        # balance factor < -1
        # tree is right heavy
        if balance < -1:
            if value > root.right.data:
                return self.leftRotate(root.left)
            else:
                # right-left rotate is only possible
                # when the right child of a node is greater than the new node
                """
                       21  <- root in this subtree
                        \
                        36	<- right child of root
                        /
                         28 < - new Node
                """
                root.right = self.rightRotate(root.right)

                return self.leftRotate(root.left)
        return root

    def removeNode(self, root, value):
        if not root:
            return None

        if value > root.data:
            root.right = self.removeNode(root.right, value)
        elif value < root.data:
            root.left = self.removeNode(root.left, value)
        else:
            if not root.right and not root.left:
                return None
            if not root.left and root.right:
                return root.right
            if not root.right and root.left:
                return root.left
            if root.left and root.right:
                temp = root.right

                while temp.left:
                    temp = temp.left

                root.data = temp.data
                root.right = self.removeNode(root.right, root.data)

        root.height = max(self.findHeight(root.left), self.findHeight(root.right))

        balance = self.findBalance(root)

        if balance > 1:
            if self.findBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balance < -1:
            if self.findBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)

                return self.leftRotate(root)
        return root

    def leftRotate(self, x):
        y = x.right
        b = y.left

        y.left = x
        x.right = b

        x.height = 1 + max(self.findHeight(x.left), self.findHeight(x.right))
        y.height = 1 + max(self.findHeight(y.left), self.findHeight(y.right))

        return y

    def rightRotate(self, x):
        y = x.left
        b = y.right

        y.right = x
        x.left = b

        x.height = 1 + max(self.findHeight(x.left), self.findHeight(x.right))
        y.height = 1 + max(self.findHeight(y.left), self.findHeight(y.right))

        return y

    def findHeight(self, node):
        if node == None:
            return 0
        return node.height

    def findBalance(self, node):
        if node == None:
            return 0
        balance = self.findHeight(node.left) - self.findHeight(node.right)

        return balance


sequenceAfterRoot = [9, 53, 8, 21, 61, 11]

root = Node(33)
avlTree = AvlTree()

for node in sequenceAfterRoot:
    avlTree.add_node(root, node)

"""
print("Node 61 height:  %i" % avlTree.findHeight(root.right.right))
print("Node 9 height:  %i" % avlTree.findHeight(root.left))
print("Root node (33) height: %i" % avlTree.findHeight(root))
print("Node 61 balance: %i" % avlTree.findBalance(root.right.right))
print("Node 9 balance: %i" % avlTree.findBalance(root.left))
print("Root node (33) balance: %i" % avlTree.findBalance(root))
"""
print("Next")
avlTree.add_node(root, 12)
print("Node 9 balance: %i" % avlTree.findBalance(root.left))
avlTree.inorder(root)
print("\nRemove node 9")
avlTree.removeNode(root, 9)
avlTree.inorder(root)
print("\n")
print(avlTree.findHeight(root.left.left.right))
