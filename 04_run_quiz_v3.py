"""Component 4 - Run Quiz (version 3)
"Next" button can only be clicked once option has been selected.
Displays an error message if "next" button is clicked before option
"""
from tkinter import *
from tkinter import messagebox

# Setup lists to hold questions, answers and options
questions_list = [(1, "Q1: What is red in Maori?", "Whero"),
                  (2, "Q2: What is 3 in Maori?", "Toru"),
                  (3, "Q3: What is Sunday in Maori?", "Ratapu"),
                  (4, "Q4: What is 10 in Maori?", "Tekau"),
                  (5, "Q5: What is green in Maori?", "Kakariki"),
                  (6, "Q6: What is Thursday in Maori?", "Rapare")]
options_list = [(1, "Whero", "Kowhai", "Ma"), (2, "Tahi", "rima", "Toru"),
                (3, "Ratapu", "Ramere", "Rahori"), (4, "Waru", "Rua", "Tekau"),
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
DIMENSIONS = "900x600"
WIDTH = 900
HEIGHT = 600
q_num = 0  # Sets question number


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

    # Calls function to change text in question
    change_question(win, question_lbl)

    q_status = "not answered"  # Option hasn't been selected yet
    next_button(win, question_lbl, q_status)  # Calls next button function

    win.mainloop()


# Displays options for each question
def display_options(master, lbl):
    global q_num
    for opts in options_list:
        # If the question number matches with the options for that question
        # Then display those options as buttons
        if opts[0] == q_num:
            # Option 1 button
            opt1_txt = opts[1]  # Sets a variable for option 1
            opt1 = Button(master, text=opt1_txt, font=(Q_FONT, BTN_SIZE),
                          width=10, fg=WHITE, bg=BLACK, command=lambda:
                          check_opt(opt1_txt, 50))
            opt1.place(x=50, y=300)

            # Option 2 button
            opt2_txt = opts[2]  # Sets a variable for option 2
            opt2 = Button(master, text=opt2_txt, font=(Q_FONT, BTN_SIZE),
                          width=10, fg=WHITE, bg=BLACK, command=lambda:
                          check_opt(opt2_txt, 350))
            opt2.place(x=350, y=300)

            # Option 3 button
            opt3_txt = opts[3]  # Sets a variable for option 3
            opt3 = Button(master, text=opt3_txt, font=(Q_FONT, BTN_SIZE),
                          width=10, fg=WHITE, bg=BLACK, command=lambda:
                          check_opt(opt3_txt, 650))
            opt3.place(x=650, y=300)

    # Checks if selected option is correct answer
    def check_opt(selected_opt, opt_x):
        global q_num
        for answer in questions_list:
            if answer[0] == q_num:
                # If selected option is the answer then display "correct!"
                if selected_opt == answer[2]:
                    correct_lbl = Label(master, text="Correct!",
                                        font=(Q_FONT, 20), fg=GREEN)
                    correct_lbl.place(x=opt_x, y=400)
                # If selected option is not the answer then display "incorrect!"
                else:
                    incorrect_lbl = Label(master, text="Incorrect!",
                                          font=(Q_FONT, 20), fg=RED)
                    incorrect_lbl.place(x=opt_x, y=400)

                # Disables all buttons so only one option is selected at a time
                opt1.config(state="disabled")
                opt2.config(state="disabled")
                opt3.config(state="disabled")

        next_button(master, lbl, "answered")  # Next button can be clicked now


# Displays Next button to go to next question
def next_button(master, qt_lbl, qt_status):
    next_btn = Button(master, text="Next", font=(Q_FONT, 20), fg=WHITE, bg=GREEN)
    next_btn.place(x=750, y=450)
    # If the question has been answered - option is selected
    if qt_status == "answered":
        # Then allow user to click "next" to go to next question
        next_btn.config(command=lambda: change_question(master, qt_lbl))
    else:
        # If not then display error message
        next_btn.config(command=msg_error)


# Error message for "next" button
def msg_error():
    messagebox.showerror("Error", "Please select your answer before going to "
                                  "the next question")


# Changes the text in the question label
def change_question(master, lbl):
    global q_num
    q_num += 1  # Question number increases every time "next" button is clicked
    next_button(master, lbl, "not answered")
    # Searches question in question list
    for qt in questions_list:
        if qt[0] == q_num:  # If it is question one
            # Changes the text in the question label
            lbl.config(text=qt[1])

    display_options(master, lbl)  # Calls function to display options


# Main Routine
root = Tk()

intro()
