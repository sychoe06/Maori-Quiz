from tkinter import *


class Window(Frame, message):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        text = Label(self, text=message)
        text.place(x=70, y=90)


root = Tk()
message = ""
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("200x200")
root.mainloop()
