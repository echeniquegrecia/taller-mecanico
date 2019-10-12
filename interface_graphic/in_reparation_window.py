from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry


class InReparationWindow:
    """Class for window to repair"""

    def __init__(self):
        master = Tk()
        listbox = Listbox(master, width=100, height=20)

        listbox.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        #listbox.pack(side="left", fill="y")
        # scrollbar = Scrollbar(master, orient="vertical")
        # scrollbar.config(command=listbox.yview)
        # scrollbar.pack(side="right", fill="y")
        # listbox.config(yscrollcommand=scrollbar.set)
        #
        #
        list_values = ["one", "two", "three", "four", "hhh", "uuuu", "jjjj", "oooo", "mmmm", "tttt",
                       "iii", "ggg", "ddd", "zzz", "aaaa"]
        #
        for item in list_values:
            listbox.insert(END, item)
        #
        def testing():
            value = listbox.curselection()
            print(list_values[value[0]])
            listbox.delete(ANCHOR)
        #
        #
        #
        btn = Button(master, text="Finalizar", command=testing)
        btn.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        mainloop()


InReparationWindow()