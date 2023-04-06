class Node:
    def __init__(self, value):
        self.color = None
        self.right = None
        self.left = None
        self.value = value
        self.parent = None


def get_parent(r, node):
    parent = None
    x = r

    while x is not None:
        parent = x
        if node.value < x.value:
            x = x.left
        else:
            x = x.right
    return parent


def insert_into_RBT(r, key):
    def rotation(x, y):  # x is the older .if sending child and parent .then x is the parent and y is the child
        z = x.get_parent
        if z.value > y:
            z.left = y
        else:
            z.right = y
        if y.value > x.value:
            y.left = x
        if y.value < x.value:
            y.right = x

    # function for case 1
    def change_color_up(node, uncle):
        node.parent.color = "black"
        uncle.color = "black"
        node.parent.parent.color = "red"
        return node.parent.parent

    def fix_insert(n):
        while n.parent is not None and n.parent.color == "red":
            if n.parent is n.parent.parent.left:
                uncle = n.parent.parent.right
                if uncle.color == "red" and uncle is not None:
                    n = change_color_up(n, uncle)
                if uncle.color == "black" and uncle is not None:
                    # case 3(left-right)
                    if n is n.parent.right:
                        n = n.parent
                        rotation(n.parent.parent, n.parent)
                    n.parent = "black"
                    n.parent.parent = "black"
                    rotation(n.parent.parent, n.parent)
            else:
                uncle = n.parent.parent.left
                if uncle.color == "red" and uncle is not None:
                    n = change_color_up(n, uncle)
                if uncle.color == "black" and uncle is not None:
                    # case 3 (right-left)
                    if n is n.parent.left:
                        n = n.parent
                        rotation(n.parent.parent, n.parent)
                    n.parent = "black"
                    n.parent.parent = "red"
                    rotation(n.parent.parent, n.parent)
        r.color = "black"

    new_node = Node(key)
    new_node.parent = get_parent(r, new_node)
    parent = get_parent(r, new_node)
    if parent is None:
        r = new_node
    elif parent.value < new_node.value:
        parent.right = new_node
    else:
        parent.left = new_node
    fix_insert(new_node)
    return r


from collections import deque


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
        print(node.value, node.color)

        # Add the node's children to the queue
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


r = None
r = insert_into_RBT(r, 2)
r = insert_into_RBT(r, 1)
r = insert_into_RBT(r, 4)
r = insert_into_RBT(r, 5)
r = insert_into_RBT(r, 9)
r = insert_into_RBT(r, 3)
r = insert_into_RBT(r, 6)
r = insert_into_RBT(r, 7)
print_red_black_tree(r)
