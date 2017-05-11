######################################################
# This program is to provide the player with a title screen
# The Start game button starts the Main_Game program
# The Go to Scoreboard button starts the Score_Board program
######################################################

from Tkinter import *

class StartPage(Frame):
    def __init(self, parent):
        Frame.__init__(self, parent)
        self.test = True


    def startMain_Game(self):
        self.test = False

    def startScore_Board(self):
        pass

    test = True

    def setup(self):
        TITLE_FONT = ("Helvetica", 18, "bold")
        LARGE_FONT = ("Verdana", 12)

        label = Label(text="This is the start page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(text="Start Game", command = self.startMain_Game)

        button2 = Button(text="Go to Scoreboard")

        button1.pack()
        button2.pack()

    def start(self):
        self.setup()

window = Toplevel

# create the GUI as a Tkinter canvas inside the window
g = StartPage(window)
# play the game
g.start()

while g.test:
    window.update()


execfile("test.py")




