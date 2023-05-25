"""Component 7 - Button colour - Post usability testing 1
Change the colour of a button when the mouse hovers over it
"""

# import required module
from tkinter import *


# Changes colour of button on hover
def change_on_hover(button, colour_on_hover, colour_on_leave):
    # Colour of button changes when mouse hovers over it
    button.bind("<Enter>", func=lambda e: button.config(
        background=colour_on_hover))

    # Colour of button changes when mouse is not hovering over it
    button.bind("<Leave>", func=lambda e: button.config(
        background=colour_on_leave))


# Main routine
root = Tk()

# create test button
black_btn = Button(root, text="BLACK TEST", fg="white", bg="black")
black_btn.pack(pady=10)

green_btn = Button(root, text="GREEN TEST", fg="white", bg="green")
green_btn.pack(pady=10)

# Calls function to change colour of test buttons on hover
change_on_hover(black_btn, "grey", "black")
change_on_hover(green_btn, "light green", "green")

root.mainloop()
