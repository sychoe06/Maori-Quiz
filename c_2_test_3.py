"""Component 2 - Questions (version 1)
Used a constant variable to store question one - saves up space
"""
from tkinter import *

root = Tk()
root.title("Maori Quiz")  # Sets title for window
root.geometry("900x600")  # Sets dimensions for window


class Quiz:
    def __init__(self, main, question):
        quiz_frame = Frame(main)
        quiz_frame.pack()
        self.quiz_name = "Maori Quiz"
        self.question = Label(main, text=question, font=("Calibri", 25)

    def start_quiz(self):  # Launches Maori Quiz
        root.destroy()  # Deletes the starting window

        # New Window is created using Tk class
        new_root = Tk()
        new_root.title("Maori Quiz")  # Sets title for new window
        new_root.geometry("900x600")  # Sets dimensions

        # Create a canvas object
        quiz_title = Canvas(new_root, width=900, height=100, bg="red")

        # Add the title "Maori Quiz" in Canvas
        quiz_title.create_text(450, 50, text="Maori Quiz", fill="white",
                              font=("Calibri", 30, "bold"))
        quiz_title.pack()

        # Quiz questions
        question_one = "Q1: What is the colour red in Maori?"

        new_root.mainloop()


# Contains all the questions for this quiz
questions_list = ["What is the colour red in Maori?",
                  "What is monday in Maori?"]

# Labels to welcome user
welcome_lbl = Label(root, text="Welcome to the",
                    font=("Calibri", 20, "bold"), fg="black")

Maori_Quiz_lbl = Label(root, text="Maori Quiz",
                       font=("Calibri", 50, "bold"), fg="red")

# Start button - activates quiz when clicked
start_btn = Button(root, text="START", command=start_quiz,
                   font=("Calibri", 20, "bold"), fg="white", bg="black")

# Setting position - centering labels and button
welcome_lbl.place(relx=0.5, rely=0.3, anchor=CENTER)
Maori_Quiz_lbl.place(relx=0.5, rely=0.4, anchor=CENTER)
start_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
