class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(20)

root.left.left = Node(3)
root.left.right = Node (7)

root.right.left = Node(15)
root.right.left.right = Node(18)

#calculating height of the above tree //3
def height(node):
    if node is None:
        return -1

    left = height(node.left)
    right = height(node.right)

    return max(left, right) +1

print("height: ", height(root))