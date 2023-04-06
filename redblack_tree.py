def get_parent(root, node):
    if root is None or root == node:
        return None
    if node.value < root.value:
        if root.left == node:
            return root
        else:
            return get_parent(root.left, node)

    if node.value > root.value:
        if root.right == node:
            return node
        else:
            return get_parent(root.right, node)
    else:
        return None


def insert_into_RBT(root, key):
    class Node:
        def __init__(self, value):
            self.color = None
            self.right = None
            self.left = None
            self.value = value
            self.parent = None

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
        root.color = "black"

    new_node = Node(key)
    new_node.parent = get_parent(root, new_node)
    parent = get_parent(root, new_node)
    if parent is None:
        root = new_node
    elif parent.value < new_node:
        parent.right = new_node
    else:
        parent.left = new_node
    fix_insert(new_node)
    return root
