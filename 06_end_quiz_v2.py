"""Component 6 - End Quiz (version 2)
Only using the code needed for the End Quiz component - to save time
Shows the user their score out of 6 in the end window
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
score = 6  # Set score to 10 for testing purposes
total_num_qt = 6  # Total number of questions


# End Maori Quiz window
def end_quiz():
    # New Window is created using Tk class for the end of the quiz
    end = Tk()
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
    score_lbl.place(x=380, y=150)
    user_score_lbl = Label(end, text=f"{score}/{total_num_qt}",
                           font=(Q_FONT, 70), fg=WHITE, bg=GREEN)
    user_score_lbl.place(x=400, y=200)

    end.mainloop()


# Main Routine
end_quiz()
