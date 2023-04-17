import new_rbt as redblack_tree


def init_dic():
    file = open("EN-US-Dictionary.txt", 'r')
    lines = file.readlines()
    file.close()
    tree = redblack_tree.Red_BLack_Tree()
    for line in lines:
        tree.insert(line)
    return tree


def look_up(rbt, value):
    if rbt.search(value) is None:
        return None
    else:
        return value


def insert_word(rbt, word):
    if rbt.search(word) is None:
        rbt.insert(word)
        return rbt
    else:
        return False


def print_dict_size(dict):
    dict.print_size()


def print_height(dict):
    dict.print_height()
