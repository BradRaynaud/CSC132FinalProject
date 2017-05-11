######################################################
# This program is to provide the player with a title screen
# The Start game button starts the Main_Game program
# The Go to Scoreboard button starts the Score_Board program
######################################################

from Tkinter import *

TITLE_FONT = ("Helvetica", 18, "bold")
LARGE_FONT = ("Verdana", 12)

window = Tk()

label = Label(text="This is the start page", font=TITLE_FONT)
label.pack(side="top", fill="x", pady=10)

button1 = Button(text="Start Game")

button2 = Button(text="Go to Scoreboard")

button1.pack()
button2.pack()

window.mainloop()
