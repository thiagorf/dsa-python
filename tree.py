class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data + " -> ", end="")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data + " -> ", end="")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data + " -> ", end="")


"""
    1
   /\
  12 9
 /\
5  6	
"""

root = Node("1")
root.left = Node("12")
root.right = Node("9")

root.left.left = Node("5")
root.left.right = Node("6")

print("Inorder sequence: ")
inorder(root)

print("\n\nPreorder sequence: ")
preorder(root)

print("\n\nPostorder sequence: ")
postorder(root)
print(" ")
