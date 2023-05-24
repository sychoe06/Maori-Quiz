"""Component 4 - Run Quiz (version 1)
Sets min and max size for window, Adds all questions and options to their lists
Displays a "next" button at the bottom
"""
from tkinter import *

root = Tk()

# Setup lists to hold questions, answers and options
questions_list = [(1, "Q1: What is red in Maori?", "Whero"),
                  (2, "Q2: What is 3 in Maori?", "Toru"),
                  (3, "Q3: What is Sunday in Maori?", "Ratapu"),
                  (4, "Q4: What is 10 in Maori?", "Tekau"),
                  (5, "Q5: What is green in Maori?", "Kakariki"),
                  (6, "Q6: What is Thursday in Maori?", "Rapare")]
options_list = [(1, "Whero", "Kowhai", "Ma"), (2, "Tahi", "rima", "Toru"),
                (3, "Ratapu", "Ramere", "Rahori"), (4, "waru", "rua", "tekau"),
                (5, "Karaka", "Kakariki", "Kowhai"),
                (6, "Raapa", "Ratu", "Rapare")]

# Set up variables
WHITE = "white"
BLACK = "black"
RED = "red"
GREEN = "green"

QUIZ_NAME = "Maori Quiz"  # Name of Quiz
BTN_SIZE = 25  # Size for option buttons and start button
Q_FONT = "Calibri"  # Quiz Font
DIMENSIONS = "900x600"  # window dimensions
WIDTH = 900  # window height
HEIGHT = 600  # window height


# Intro window to start the quiz
def intro():
    root.title(f"{QUIZ_NAME} - Start")  # Sets title for window
    root.geometry(DIMENSIONS)  # Sets dimensions for window
    root.maxsize(WIDTH, HEIGHT)  # Sets maximum dimensions

    # Intro to welcome user
    welcome_lbl = Label(root, text="Welcome to the",
                        font=(Q_FONT, 20, "bold"), fg="black")
    maori_quiz_lbl = Label(root, text=QUIZ_NAME,
                           font=(Q_FONT, 50, "bold"), fg="red")

    # Start button - activates quiz when clicked
    start_btn = Button(root, text="START", font=(Q_FONT, BTN_SIZE, "bold"),
                       bg=BLACK, fg=WHITE, command=start_quiz)

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
    win.title(QUIZ_NAME)  # Sets title for new window
    win.geometry(DIMENSIONS)  # Sets dimensions
    win.maxsize(WIDTH, HEIGHT)  # Sets maximum dimensions
    win.minsize(850, 550)  # Sets minimum dimensions

    # Create a canvas object
    quiz_name = Canvas(win, width=WIDTH, height=100, bg=RED)

    # Add the name "Maori Quiz" in Canvas
    quiz_name.create_text(450, 50, text=QUIZ_NAME, fill=WHITE,
                          font=(Q_FONT, 30, "bold"))
    quiz_name.pack()

    # Sets up template for question label
    question_lbl = Label(win, text="", font=(Q_FONT, 25))
    question_lbl.place(relx=0.06, rely=0.25, anchor=NW)

    change_question(question_lbl, 1)  # Displays Question 1
    display_options(win, 1)  # Displays options for Question 1

    # Next question button
    next_btn = Button(win, text="Next", font=(Q_FONT, 20), fg=WHITE, bg=GREEN)
    next_btn.place(x=750, y=450)

    win.mainloop()


# Changes the text in the question label
def change_question(lbl, q_num):
    for qt in questions_list:
        if qt[0] == q_num:  # If it is question one
            # Changes the text in the question label
            lbl.config(text=qt[1])


# Displays options for each question
def display_options(master, q_num):
    for opts in options_list:
        # If the question number matches with the options for that question
        # Then display those options as buttons
        if opts[0] == q_num:
            opt1 = Button(master, text=opts[1], font=("Calibri", 25), width=10,
                          fg="white", bg="black", command=lambda:
                          check_answer(opts[1], 50))
            opt1.place(x=50, y=300)

            opt2 = Button(master, text=opts[2], font=("Calibri", 25), width=10,
                          fg="white", bg="black", command=lambda:
                          check_answer(opts[2], 350))
            opt2.place(x=350, y=300)

            opt3 = Button(master, text=opts[3], font=("Calibri", 25), width=10,
                          fg="white", bg="black", command=lambda:
                          check_answer(opts[3], 650))
            opt3.place(x=650, y=300)

    # Checks if selected option is correct answer
    def check_answer(selected_opt, opt_x):
        for answer in questions_list:
            if selected_opt == answer[2]:  # Correct option is selected
                correct_lbl = Label(master, text="Correct!",
                                    font=("Calibri", 20), fg="green")
                correct_lbl.place(x=opt_x, y=400)
            else:  # Incorrect option is selected
                incorrect_lbl = Label(master, text="Incorrect!",
                                      font=("Calibri", 20), fg="red")
                incorrect_lbl.place(x=opt_x, y=400)

            # Disables all option buttons
            opt1.config(state="disabled")
            opt2.config(state="disabled")
            opt3.config(state="disabled")


# Main Routine
intro()
