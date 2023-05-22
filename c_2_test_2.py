"""Component 2 - Questions (version 2)

"""
from tkinter import *

root = Tk()


class Questions:
    def __init__(self, parent, text):
        self.my_frame = Frame(parent)
        self.my_frame.pack()
        self.text = text
        #self.question = Label(my_frame, text=text).pack(padx=20, pady=20)

    def set_label(self):
        Label(self.my_frame, text=self.text).pack(padx=20, pady=20)


def next_q(parent):
    var_a = Questions(parent, "Yellow?")

    #Questions.set_label()


def display():
    root.destroy()
    win = Tk()
    Questions(win, "What is red in Maori?")
    next_btn = Button(win, text="Next", command=lambda: next_q(win))
    next_btn.pack(padx=20, pady=20)

    win.mainloop()


btn = Button(root, text="click me", command=display)
btn.pack()
root.mainloop()
