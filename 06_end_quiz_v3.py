"""Component 6 - End Quiz (version 3)
Shows play again button below the score and changed fg and bg of user's score
"""
from tkinter import *

# Set up constants
WHITE = "white"
BLACK = "black"
RED = "red"
GREEN = "green"
LIGHT_GREEN = "#8AC847"
LIGHT_RED = "#ffcccb"

QUIZ_NAME = "Maori Quiz"  # Name of Quiz
BTN_SIZE = 25  # Size for option buttons and start button
Q_FONT = "Calibri"  # Quiz Font
DIMENSIONS = "900x600"  # Dimensions of window
WIDTH = 900  # Height of window
HEIGHT = 600  # Width of window

# Set up variables
q_num = 0  # Sets question number
score = 6  # Set score to 6 for testing purposes
total_num_qt = 6  # Total number of questions


# End Maori Quiz window
def end_quiz():
    end = Tk()
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
                            fg=WHITE, bg=BLACK, width=15)
    play_again_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    end.mainloop()


# Main routine
end_quiz()
