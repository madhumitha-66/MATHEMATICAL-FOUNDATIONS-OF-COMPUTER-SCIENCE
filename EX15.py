class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)

    elif value > root.data:
        root.right = insert(root.right, value)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)


root = None

records = [50, 30, 70, 20, 40, 60, 80]

for value in records:
    root = insert(root, value)

print("Inorder Traversal:")
inorder(root)

key = int(input("\nEnter register number to search: "))

if search(root, key):
    print("Student Record Found")
else:
    print("Student Record Not Found")
