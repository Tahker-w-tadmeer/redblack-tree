import new_rbt


class Printable:
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % (self.key + " " + ("B" if self.color == "black" else "R"))
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % (self.key + " " + ("B" if self.color == "black" else "R"))
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % (self.key + " " + ("B" if self.color == "black" else "R"))
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % (self.key + " " + ("B" if self.color == "black" else "R"))
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
        self.color = 'red'
        self.parent = None
        self.left = None
        self.right = None
        self.key = value


class Red_BLack_Tree:

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.root.color = 'black'
            return
        node = Node(key)
        self.insert_into_RBT(node, self.root)
        self.fix_insertion(node)

    def insert_into_RBT(self, node, parent: Node) -> Node:

        while parent is not None:
            node.parent = parent
            if node.key < parent.key:
                if parent.left is None:
                    parent.left = node
                    return node
                parent = parent.left
            else:
                if parent.right is None:
                    parent.right = node
                    return node
                parent = parent.right

    def display(self):
        if self.root is not None:
            print(self.root.display())

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def change_color_up(self, node, uncle):
        node.parent.color = 'black'
        uncle.color = 'black'
        node.parent.parent.color = 'red'
        return node.parent.parent

    def fix_insertion(self, n):
        while n.parent is not None and n.parent.color == 'red':
            uncle = self.get_uncle(n)
            if uncle is not None and uncle.color == 'red':
                n = self.change_color_up(n, uncle)
            else:
                grandparent = n.parent.parent
                parent = n.parent
                if n is parent.right and parent is grandparent.left:
                    n = n.parent
                    self._left_rotate(n)
                if n is parent.left and parent is grandparent.left:
                    n.parent.color = 'black'
                    n.parent.parent.color = 'red'
                    self._right_rotate(n.parent.parent)
                if n is parent.left and parent is grandparent.right:
                    n = n.parent
                    self._right_rotate(n)
                if n is parent.right and parent is grandparent.right:
                    n.parent.color = 'black'
                    n.parent.parent.color = 'red'
                    self._left_rotate(n.parent.parent)
        self.root.color = 'black'

    def get_uncle(self, n: Node) -> Node:
        x = n.parent
        if x is None:
            return None
        if x is x.parent.left:
            return x.parent.right
        if x is x.parent.right:
            return x.parent.left

    def height(self, node):
        if node is None:
            return 0
        else:
            max_left = self.height(node.left)
            max_right = self.height(node.right)
            return max(max_left, max_right) + 1

    def size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.size(node.left) + self.size(node.right)

    def print_height(self):
        size = self.height(self.root)
        print(size)

    def print_size(self):
        size = self.size(self.root)
        print(size)

    def search(self, value):
        n = self.root
        while n is not None:
            if n.key == value:
                return n.key
            if n.key > value:
                n = n.left
                continue
            if n.key < value:
                n = n.right
                continue
        return None

