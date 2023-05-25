# import required module
from tkinter import *


# function to change properties of button on hover
def change_on_hover(button, colour_on_hover, colour_on_leave):

    # adjusting background of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colour_on_hover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colour_on_leave))


# Driver Code
root = Tk()

# create button
# assign button text along
# with background color
myButton = Button(root,
                  text="On Hover - Background Change",
                  bg="yellow")
myButton.pack()

# call function with background
# colors as argument
change_on_hover(myButton, "red", "yellow")

root.mainloop()
