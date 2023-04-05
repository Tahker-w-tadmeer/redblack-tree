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


def insert_into_RBT(root, node):
    class node:
        def __init__(self, value):
            self.color = None
            self.right = None
            self.left = None
            self.value = value
            self.parent=None


