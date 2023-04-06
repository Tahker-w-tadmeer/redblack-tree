import new_rbt as redblack_tree


def init_dic():
    file = open("dictionary.txt", 'r')
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

#####################################################################

# y = input("enter Dictionary name: ")
# Dictionary = read_dic(y)
# print("Dictionary loaded successfully!")
# print("size of dictionary before loaded: ")
# print_dict_size(Dictionary)
# print("height of dictionary before loaded: ")
# print_height(Dictionary)
#
# print("enter a word to look up: ")
# x = input()
# look_up(Dictionary, x)
# print("enter a word to insert: ")
# z = input()
# insert_word(Dictionary, z)
# print("size of dictionary after loaded: ")
# print_dict_size(Dictionary)
# print("height of dictionary after loaded: ")
# print_height(Dictionary)
