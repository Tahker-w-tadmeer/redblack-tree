import tkinter as tk
import tkinter.messagebox as msgbox
import readFromDictionnnery as dic


def search_entered_word(tree):
    word = entry.get()
    word = word + "\n"
    return dic.look_up(tree, word)


def show_search_mssg(tree):
    if search_entered_word(tree) is None:
        msgbox.showinfo("search result", "word not found")
    else:
        msgbox.showinfo("search result", "the word is found")


def add_entered_word(tree):
    word = entry2.get()
    word = word + "\n"
    return dic.insert_word(tree, word)


def show_add_mssg(tree):
    if add_entered_word(tree) is False:
        msgbox.showinfo("add result", "word not added\n the word is already in the dictionary")

    else:
        msgbox.showinfo("add result", "the word is added\n the height of the tree is: " + str(
            tree.print_height()) + "\n the size of the tree is: " + str(tree.print_size()))


tree = dic.init_dic()
msgbox.showinfo("size and height of dictionary",
                "the height of the tree is: " + str(tree.print_height()) + "\n the size of the tree is: " + str(
                    tree.print_size()))
window = tk.Tk()
window.title("gramarly el ghalaba")
window.geometry("500x200")
label = tk.Label(window, text="search for a word:")
label.pack()
entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="search", command=lambda: show_search_mssg(tree))
button.pack()
label = tk.Label(window, text="add for a word:")
label.pack()

entry2 = tk.Entry(window)
entry2.pack()
button = tk.Button(window, text="insert", command=lambda: show_add_mssg(tree))
button.pack()

# Run the window
window.mainloop()
