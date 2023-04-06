import tkinter as tk
import tkinter.messagebox as msgbox
import readFromDictionnnery as dic


def search_entered_word():
    word = entry.get()
    tree = dic.init_dic()
    return dic.look_up(tree, word)


def show_search_mssg():
    if search_entered_word() is None:
        msgbox.showinfo("search result", "word not found")
    else:
        msgbox.showinfo("search result", "the word is found")
def add_entered_word():
    word = entry2.get()
    tree = dic.init_dic()
    return dic.insert_word(tree, word)
def show_add_mssg():
    if add_entered_word() is False:
        msgbox.showinfo("add result", "word not added\n the word is already in the dictionary")

    else:
        msgbox.showinfo("add result", "the word is added\n the height of the tree is: "+str(dic.print_height(add_entered_word()))+"\n the size of the tree is: "+str(dic.print_size(add_entered_word())))

window = tk.Tk()
window.title("gramarly el ghalaba")

window.geometry("500x200")

label = tk.Label(window, text="search for a word:")
label.pack()

entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="search", command=show_search_mssg)
button.pack()
label = tk.Label(window, text="add for a word:")
label.pack()

entry2 = tk.Entry(window)
entry2.pack()
button = tk.Button(window, text="insert", command=show_add_mssg)
button.pack()

# Run the window
window.mainloop()
