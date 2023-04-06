import redblack_tree


def read_dic(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    root = None
    for line in lines:
        root = redblack_tree.insert_into_RBT(root, line)
