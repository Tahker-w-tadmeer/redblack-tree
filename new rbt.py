class node:
    def __init__(self, value):
        self.color = "red"
        self.parent = None
        self.left = None
        self.right = None
        self.key = value


class Red_BLack_Tree:
    def __int__(self, value):
        self.root = None

    def insert_into_RBT(self, key):
        new_node = Node(key)
        parent = None
        x = self.root

        while x is not None:
            parent = x
            if new_node.value < x.value:
                x = x.left
            else:
                x = x.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif parent.value < new_node.value:
            parent.right = new_node
        else:
            parent.left = new_node
        fix_insert(new_node)

    def change_color_up(node, uncle):
        node.parent.color = "black"
        uncle.color = "black"
        node.parent.parent.color = "red"
        return node.parent.parent

    def fix_insertion(self, node):
        while n.parent is not None and n.parent.color == "red":
            uncle = get_uncle(node)
            if uncle is not None and uncle.color == "red":
                n = change_color_up(n, uncle)
            else:

                granparent=n.parent.parent
                parent = n.parent
                if n is parent.right and parent is granparent.left:
                    n = n.parent
                    left_rotate(n)
                elif n is parent.left and parent is granparent.left:
                  n.parent.color = "black"
                  n.parent.parent.color = "black"
                  right_rotate(n.parent.parent)
                if n is parent.left and parent is grandparent.right:
                    n=n.parent
                    right_rotate(n)
                elif n is parent.right and parent is grandparent.right:
                  n.parent.color= "black"
                  n.parent.color="black"
                  left_rotate()


    def rotation(x, y):  # x is the older .if sending child and parent .then x is the parent and y is the child
        z = x.get_parent
        if z.value > y:
            z.left = y
            y.parent = z
        else:
            z.right = y
            y.parent = z
        if y.value > x.value:
            y.left = x
            x.parent = y
        if y.value < x.value:
            y.right = x
            x.parent = y

    def get_uncle(node):
        x = node.parent
        if (x is None):
            return None
        if (x is x.parent.left):
            return x.parent.right
        if (x is x.parent.right):
            return x.parent.left

    def fix_insertion11(self, node):
        while n.parent is not None and n.parent.color == "red":
            uncle = get_uncle(node)
            if uncle is not None and uncle.color == "red":
                n = change_color_up(n, uncle)
            if uncle is None or uncle.color == "black":
                parent = n.parent
                if (n is parent.right and parent is parent.parent.right) or ( n is parent.left and parent is parent.parent.left):
                    parent.color="black"
                    parent.parent.color="red"
                    rotate(parent.parent,parent)
                if (n is parent.right and parent is parent.parent.left) or ( n is parent.left and parent is parent.parent.right):
                    parent.color="black"
                    parent.parent.color="red"
                    rotate(parent.parent,parent)



