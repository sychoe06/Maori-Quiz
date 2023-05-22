"""Component 2 - Questions (version 2)

"""
from tkinter import *

root = Tk()


# Intro window to start the quiz
def intro():
    root.title("Maori Quiz")  # Sets title for window
    root.geometry("900x600")  # Sets dimensions for window

    # Intro to welcome user
    welcome_lbl = Label(root, text="Welcome to the",
                        font=("Calibri", 20, "bold"), fg="black")
    maori_quiz_lbl = Label(root, text="Maori Quiz",
                           font=("Calibri", 50, "bold"), fg="red")

    # Start button - activates quiz when clicked
    start_btn = Button(root, text="START", command=start_quiz,
                       font=("Calibri", 20, "bold"), fg="white", bg="black")

    # Setting position - centering labels and button
    welcome_lbl.place(relx=0.5, rely=0.3, anchor=CENTER)
    maori_quiz_lbl.place(relx=0.5, rely=0.4, anchor=CENTER)
    start_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

    root.mainloop()


# Launches Maori Quiz
def start_quiz():
    root.destroy()  # Deletes the starting window

    # New Window is created using Tk class
    win = Tk()
    win.title("Maori Quiz")  # Sets title for new window
    win.geometry("900x600")  # Sets dimensions

    # Create a canvas object
    #quiz_name = Canvas(win, width=900, height=100, bg="red")

    # Add the name "Maori Quiz" in Canvas
    #quiz_name.create_text(450, 50, text="Maori Quiz", fill="white",
                        #  font=("Calibri", 30, "bold"))
    #quiz_name.pack()

    # Quiz questions
    #Question(win, "What is the colour red?")
    Question(win)

    win.mainloop()


class Question:
    print("label")
    #def __init__(self, parent, qt):
        #self.parent = parent
        #self.colour = "black"
        #self.font = "Calibri"
        #self.size = 25
        #self.qt = qt

    #def question_lbl(self):
        #q = Label(self.parent, text=self.qt, font=(self.font, self.size),
         #         fg=self.colour)
        #q.place(relx=0.06, rely=0.25, anchor=NW)  # sets position

    def __init__(self, parent):
        self.parent = parent

    def question_lbl(self):
        Label(self.parent, text="hello").pack()


# Main routine
intro()
