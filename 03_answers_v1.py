"""Component 3 - Answers (version 1) - Trial one
Displaying options to answer question as buttons
"""
from tkinter import *

root = Tk()
questions_list = [(1, "Q1: What is red in Maori?", "Whero")]
options_list = [(1, "Whero", "Kowhai", "Ma")]


# Intro window to start the quiz
def intro():
    root.title("Maori Quiz - Start")  # Sets title for window
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


# Starts Maori Quiz
def start_quiz():
    root.destroy()  # Deletes the starting window

    # New Window is created using Tk class
    win = Tk()
    win.title("Maori Quiz")  # Sets title for new window
    win.geometry("900x600")  # Sets dimensions

    # Create a canvas object
    quiz_name = Canvas(win, width=900, height=100, bg="red")

    # Add the name "Maori Quiz" in Canvas
    quiz_name.create_text(450, 50, text="Maori Quiz", fill="white",
                          font=("Calibri", 30, "bold"))
    quiz_name.pack()

    # Sets up template for question label
    question_lbl = Label(win, text="", font=("Calibri", 25))
    question_lbl.place(relx=0.06, rely=0.25, anchor=NW)

    change_question(question_lbl, 1)  # Displays Question 1
    display_options(win, 1)  # Display options for Q1

    # Sets up options for question

    win.mainloop()


# Changes the text in the question label
def change_question(lbl, q_num):
    for qt in questions_list:
        if qt[0] == q_num:  # If it is question one
            question = f"{qt[1]}"
            # Changes the text in the question label
            lbl.config(text=question)


# Displays options for each question
def display_options(parent, q_num):
    for opts in options_list:
        # If the question number matches with the options for that question
        # Then display those options as buttons
        if opts[0] == q_num:
            opt1 = Button(parent, text=opts[1], font=("Calibri", 25),
                          width=10, fg="white", bg="black")
            opt1.place(x=50, y=300)

            opt2 = Button(parent, text=opts[2], font=("Calibri", 25),
                          width=10, fg="white", bg="black")
            opt2.place(x=350, y=300)

            opt2 = Button(parent, text=opts[3], font=("Calibri", 25),
                          width=10, fg="white", bg="black")
            opt2.place(x=650, y=300)


# Main Routine
intro()
