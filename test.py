from collections import deque


def insert_into_red_black_tree(root, key):
    class Node:
        def __init__(self, key):
            self.color = "red"
            self.key = key
            self.left = None
            self.right = None
            self.parent = None

    def left_rotate(x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insertion(node):
        while node.parent is not None and node.parent.color == "red":
            if node.parent is node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node is node.parent.right:
                        node = node.parent
                        left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node is node.parent.left:
                        node = node.parent
                        right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    left_rotate(node.parent.parent)
        root.color = "black"

    new_node = Node(key)
    parent = None
    x = root

    while x is not None:
        parent = x
        if new_node.key < x.key:
            x = x.left
        else:
            x = x.right

    new_node.parent = parent
    if parent is None:
        root = new_node
    elif new_node.key < parent.key:
        parent.left = new_node
    else:
        parent.right = new_node

    fix_insertion(new_node)

    return root


def print_red_black_tree(r):
    if r is None:
        return

    # Create a queue to store nodes in level order
    queue = deque()
    queue.append(r)

    while len(queue) > 0:
        # Get the next node in the queue
        node = queue.popleft()

        # Print the node's key and color
        print(node.key, node.color)

        # Add the node's children to the queue
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


root = None
root = insert_into_red_black_tree(root, 10)
root = insert_into_red_black_tree(root, 20)
root = insert_into_red_black_tree(root, 30)
root = insert_into_red_black_tree(root, 15)
root = insert_into_red_black_tree(root, 18)

print_red_black_tree(root)
