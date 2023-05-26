"""Component 7 - Post Usability testing 1: Button colour (version 2)
Added this component for my different buttons my program
Shortened the amount of questions to save time
"""

# import required module
from tkinter import *
from tkinter import messagebox

# Setup lists to hold questions, answers and options (changed for testing)
questions_list = [(1, "Q1: What is red in Maori?", "Whero")]
options_list = [(1, "Whero", "Kowhai", "Ma")]

# Set up constants
WHITE = "white"
BLACK = "black"
RED = "red"
GREEN = "green"
LIGHT_GREEN = "#8AC847"
LIGHT_RED = "#ffcccb"
GREY = "grey"

QUIZ_NAME = "Maori Quiz"  # Name of Quiz
BTN_SIZE = 25  # Size for option buttons and start button
Q_FONT = "Calibri"  # Quiz Font
DIMENSIONS = "900x600"  # Dimensions of window
WIDTH = 900  # Height of window
HEIGHT = 600  # Width of window

# Set up variables
q_num = 0  # Sets question number
score = 0  # Sets user's score
total_num_qt = 2  # Total number of questions (changed for testing purposes)


# Intro window to start the quiz
def intro():
    root.deiconify()  # Redraws the intro window if it has been withdrawn

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
    change_on_hover(start_btn, GREY, BLACK)  # changes hover colour

    # Setting position - centering labels and button
    welcome_lbl.place(relx=0.5, rely=0.3, anchor=CENTER)
    maori_quiz_lbl.place(relx=0.5, rely=0.4, anchor=CENTER)
    start_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

    root.mainloop()


# Changes colour of button on hover
def change_on_hover(button, colour_on_hover, colour_on_leave):
    # Colour of button changes when mouse hovers over it
    button.bind("<Enter>", func=lambda e: button.config(
        background=colour_on_hover))

    # Colour of button changes when mouse is not hovering over it
    button.bind("<Leave>", func=lambda e: button.config(
        background=colour_on_leave))


# Starts Maori Quiz window
def start_quiz():
    global q_num
    q_num = 0  # Resets question number to 0 when quiz starts
    global score
    score = 0  # Resets score to 0 when quiz starts

    root.withdraw()  # Hides the intro window

    # New Window is created using Tk class
    win = Tk()
    win.deiconify()  # Redraws the start quiz window if it has been withdrawn

    win.title(QUIZ_NAME)  # Sets title for new window
    win.geometry(DIMENSIONS)  # Sets dimensions
    win.maxsize(WIDTH, HEIGHT)  # Sets maximum dimensions
    win.minsize(850, 550)  # Sets minimum dimensions

    # Create a canvas object
    quiz_name = Canvas(win, width=900, height=100, bg=RED)

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
def display_options(main, lbl):
    global q_num
    for opts in options_list:
        # If the question number matches with the options for that question
        # Then display those options as buttons
        if opts[0] == q_num:
            # Option 1 button
            opt1_txt = opts[1]  # Sets a variable for option 1
            opt1 = Button(main, text=opt1_txt, font=(Q_FONT, BTN_SIZE),
                          width=10, fg=WHITE, bg=BLACK, command=lambda:
                          check_opt(opt1, opt1_txt, 50))
            opt1.place(x=50, y=300)
            change_on_hover(opt1, GREY, BLACK)  # changes hover colour

            # Option 2 button
            opt2_txt = opts[2]  # Sets a variable for option 2
            opt2 = Button(main, text=opt2_txt, font=(Q_FONT, BTN_SIZE),
                          width=10, fg=WHITE, bg=BLACK, command=lambda:
                          check_opt(opt2, opt2_txt, 350))
            opt2.place(x=350, y=300)
            change_on_hover(opt2, GREY, BLACK)  # changes hover colour

            # Option 3 button
            opt3_txt = opts[3]  # Sets a variable for option 3
            opt3 = Button(main, text=opt3_txt, font=(Q_FONT, BTN_SIZE),
                          width=10, fg=WHITE, bg=BLACK, command=lambda:
                          check_opt(opt3, opt3_txt, 650))
            opt3.place(x=650, y=300)
            change_on_hover(opt3, GREY, BLACK)  # changes hover colour

    # Checks if selected option is correct answer
    def check_opt(opt_btn, selected_opt, opt_x):
        result_lbl = Label(main, text="", font=(Q_FONT, 20))
        result_lbl.place(x=opt_x, y=400)
        for answer in questions_list:
            if answer[0] == q_num:
                # If selected option is the answer, display "correct!"
                if selected_opt == answer[2]:
                    result_lbl.config(text="Correct!", fg=GREEN)
                    opt_btn.config(fg=BLACK, bg=LIGHT_GREEN)

                    add_score()  # Adds to score

                # If selected option is not the answer, display "incorrect!"
                else:
                    result_lbl.config(text="Incorrect!", fg=RED)
                    opt_btn.config(fg=BLACK, bg=LIGHT_RED)

                # Disables all buttons so only one option is selected at a time
                opt1.config(state="disabled")
                opt2.config(state="disabled")
                opt3.config(state="disabled")
                main.after(500, result_lbl.destroy)
        # Next button can be clicked now
        next_button(main, lbl, "answered")

    # Keeps record of user's score - number of questions correct
    def add_score():
        global score
        score += 1  # Increases score by one when this function is called


# Displays Next button to go to next question
def next_button(main, qt_lbl, qt_status):
    global q_num
    next_btn = Button(main, text="Next", font=(Q_FONT, 20), fg=WHITE, bg=GREEN)
    next_btn.place(x=750, y=450)
    change_on_hover(next_btn, LIGHT_GREEN, GREEN)  # changes hover colour
    # If the question has been answered - option is selected
    if q_num >= total_num_qt:
        next_btn.config(command=lambda: end_quiz(main))
    elif qt_status == "answered":
        # Then allow user to click "next" to go to next question
        next_btn.config(command=lambda: change_question(main, qt_lbl))
    else:
        # If not then display error message
        next_btn.config(command=msg_error)


# Error message for "next" button
def msg_error():
    messagebox.showerror("Error", "Please select your answer before going to "
                                  "the next question")


# Changes the text in the question label
def change_question(main, lbl):
    global q_num
    q_num += 1  # Question number increases every time "next" button is clicked
    next_button(main, lbl, "not answered")
    # Searches question in question list
    for qt in questions_list:
        if qt[0] == q_num:  # If it is question one
            # Changes the text in the question label
            lbl.config(text=qt[1])

    display_options(main, lbl)  # Calls function to display options


# End Maori Quiz window
def end_quiz(quiz_window):
    global score
    quiz_window.withdraw()  # Hides the start quiz window

    end = Tk()
    end.deiconify()  # Redraws the end window if it has been withdrawn
    # New Window is created using Tk class for the end of the quiz
    end.title(f"{QUIZ_NAME} - End")  # Sets title for new window
    end.geometry(DIMENSIONS)  # Sets dimensions
    end.maxsize(WIDTH, HEIGHT)  # Sets maxsize for window

    # Create a canvas object
    finished_quiz = Canvas(end, width=WIDTH, height=100, bg=RED)

    # Add the name "Maori Quiz" in Canvas
    finished_quiz.create_text(450, 50, fill=WHITE, font=(Q_FONT, 30, "bold"),
                              text="Congrats! You have finished the quiz!")
    finished_quiz.pack()

    # Score labels created
    score_lbl = Label(end, text="Your score is...", font=(Q_FONT, 20))
    score_lbl.place(relx=0.5, rely=0.3, anchor=CENTER)
    user_score_lbl = Label(end, text=f"{score}/{total_num_qt}",
                           font=(Q_FONT, 80, "bold"), fg=GREEN)
    user_score_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Buttons
    play_again_btn = Button(end, text="PLAY AGAIN", font=(Q_FONT, BTN_SIZE),
                            fg=WHITE, bg=BLACK, width=15, command=intro)
    play_again_btn.place(relx=0.5, rely=0.8, anchor=CENTER)
    change_on_hover(play_again_btn, GREY, BLACK)  # changes hover colour

    end.mainloop()


# Main routine
root = Tk()

intro()
