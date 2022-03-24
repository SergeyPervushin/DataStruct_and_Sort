from tkinter import *


class Main_Window:
    def __init__(self, master):
        self.master = master
        self.master.title('Data struct Creator')
        self.master.geometry('1000x500')
        self.canvas = Canvas(master, width=1000, height=500, bg='white')
        self.canvas.pack()
        self.master.mainloop()

    def quit(self):
        self.quit()


class Main_menu:
    def __init__(self, root):
        self.menu = Menu(root, tearoff=0)
        root.config(menu=self.menu)

        self.file_menu = Menu(self.menu, tearoff=0)
        self.new_file_menu = Menu(self.file_menu, tearoff=0)
        self.linked_list_menu = Menu(self.new_file_menu, tearoff=0)

        self.menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_cascade(label='New', menu=self.new_file_menu)
        self.new_file_menu.add_cascade(label='Linked List', menu=self.linked_list_menu)

        self.new_file_menu.add_command(label='Binary Tree', command=Binary_tree)

        self.linked_list_menu.add_command(label='Single linked list', command=Single_linked_list_window)
        self.linked_list_menu.add_command(label='Doubly linked list', command=Doubly_linked_list_window)

        self.file_menu.add_command(label='Save')
        self.file_menu.add_command(label='Load')
        self.file_menu.add_command(label='Exit', command=root.quit)

        self.tools_menu = Menu(self.menu, tearoff=0)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Tools', menu=self.tools_menu)
        self.menu.add_cascade(label='Help', menu=self.help_menu)


class Single_linked_list_window:
    def __init__(self):
        self.window = Toplevel()
        self.window.title('Single Linked list')
        self.window.geometry('300x300')


class Doubly_linked_list_window:
    def __init__(self):
        self.window = Toplevel()
        self.window.title('Doubly Linked list')
        self.window.geometry('300x300')


class Binary_tree:
    def __init__(self):
        self.window = Toplevel()
        self.window.title('Binary tree')
        self.window.geometry('300x300')


# root = Tk()
# root.geometry('1000x500')
# root.title('Data struct Creator')
#
#
# main_menu = Menu(root)
# root.config(menu=main_menu)
#
# file_menu = Menu(main_menu, tearoff=0)
#
# new_file_menu = Menu(file_menu, tearoff=0)
#
# new_file_menu.add_command(label='Linked List')
# new_file_menu.add_command(label='Binary Tree')
# file_menu.add_cascade(label='New', menu=new_file_menu)
#
# file_menu.add_command(label='Save')
# file_menu.add_command(label='Load')
#
# tools_menu = Menu(main_menu, tearoff=0)
#
# help_menu = Menu(main_menu, tearoff=0)
# help_menu.add_command(label='Description')
# help_menu.add_command(label='Licence')
#
# main_menu.add_cascade(label='File', menu=file_menu)
# main_menu.add_cascade(label='Tools', menu=tools_menu)
# main_menu.add_cascade(label='Help', menu=help_menu)
# root.mainloop()