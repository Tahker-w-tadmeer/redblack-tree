class Printable:
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % (self.value + " " + ("B" if self.color == "black" else "R"))
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % (self.value + " " + ("B" if self.color == "black" else "R"))
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % (self.value + " " + ("B" if self.color == "black" else "R"))
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % (self.value + " " + ("B" if self.color == "black" else "R"))
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Node(Printable):
    def __init__(self, value):
        self.color = None
        self.right = None
        self.left = None
        self.value = value
        self.parent = None


def height(node):
    if node is None:
        return 0
    else:
        max_left = height(node.left)
        max_right = height(node.right)
        return max(max_left, max_right) + 1


def size(self, node):
    if node is None:
        return 0
    else:
        return 1 + self.size(node.left) + self.size(node.right)


def print_size(self):
    size = self.size(self.root)
    print(size)


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
    parent = None
    x = r

    while x is not None:
        parent = x
        if new_node.value < x.value:
            x = x.left
        else:
            x = x.right

    new_node.parent = parent

    if parent is None:
        r = new_node
    elif parent.value < new_node.value:
        parent.right = new_node
    else:
        parent.left = new_node
    fix_insert(new_node)
    return r


r = None
r = insert_into_RBT(r, "2")
r = insert_into_RBT(r, "1")
r = insert_into_RBT(r, "4")
r = insert_into_RBT(r, "5")
r = insert_into_RBT(r, "9")
r = insert_into_RBT(r, "3")
r = insert_into_RBT(r, "6")
r = insert_into_RBT(r, "7")
r.display()
