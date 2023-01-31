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


root = Node("1")
root.left = Node("12")
root.right = Node("9")

root.left.left = Node("5")
root.left.right = Node("6")

print("Inorder sequence: ")
inorder(root)
