#####################################################
#
#
#
#
#####################################################
# Imports
from time import sleep
from Tkinter import *
import msvcrt
from sys import *
import os.path
from random import randint

#####################################################

#####################################################
# Variables
Timer = 0
SCORE = 0
TEMPQUESTION = []
EXIT = "Test_Room_7A"
DEFAULTSCORES = ["Score1\n", "Score2\n", "Score3\n", "Score4\n", "Score5\n"]
GAMEOVER = False
QUESTIONMODE = False
QUESTIONDICT = {}
QUESTIONBANK = []
DIRECTION = None


#####################################################
# Room Class

class Room(object):
    # Constructor for the Room Class
    def __init__(self, name, image=None):
        # information about constructor goes here
        self.name = name
        self.exits = {}
        self.image = image

    # Getters and setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    # Generates the exits pass to it by the addExits function
    def generateExit(self, Direction, Exists, Locked, exitLocation):
        if Exists == True:
            self.exits[Direction] = [Locked, exitLocation]

    # Assumes that rooms exist in all 4 directions and they are unlocked, arguments can be provided to remove exits
    # and lock exits
    def addExits(self, North=True, South=True, East=True, West=True, northLocked=False, southLocked=False,
                 eastLocked=False, westLocked=False, nExit=None, sExit=None, eExit=None, wExit=None):
        self.generateExit("north", North, northLocked, nExit)
        self.generateExit("south", South, southLocked, sExit)
        self.generateExit("east", East, eastLocked, eExit)
        self.generateExit("west", West, westLocked, wExit)

    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits.keys():
            s += exit + " "

        return s


#####################################################
# Game Class

class Game(Frame):
    def __init(self, parent):
        Frame.__init__(self, parent)

    def createRooms(self):
        Room1A = Room("Test_Room_1A", "skull.gif")
        Room2A = Room("Test_Room_2A", "skull.gif")
        Room3A = Room("Test_Room_3A", "skull.gif")
        Room4A = Room("Test_Room_4A", "skull.gif")
        Room5A = Room("Test_Room_5A", "skull.gif")
        Room6A = Room("Test_Room_6A", "skull.gif")
        Room7A = Room("Test_Room_7A", "skull.gif")
        Room8A = Room("Test_Room_8A", "skull.gif")
        Room9A = Room("Test_Room_9A", "skull.gif")
        Room1A.addExits(South=False, nExit=Room5A, eExit=Room2A, wExit=Room4A, northLocked=True)
        Room2A.addExits(East=False, sExit=Room7A, nExit=Room6A, wExit=Room1A)
        Room3A.addExits(North=False, South=False, eExit=Room7A, wExit=Room8A)
        Room4A.addExits(West=False, eExit=Room1A, nExit=Room9A, sExit=Room8A)
        Room5A.addExits(North=False, sExit=Room1A, eExit=Room6A, wExit=Room9A)
        Room6A.addExits(North=False, East=False, wExit=Room5A, sExit=Room2A)
        Room7A.addExits(South=False, East=False, nExit=Room2A, wExit=Room3A)
        Room8A.addExits(South=False, West=False, eExit=Room3A, nExit=Room4A)
        Room9A.addExits(West=False, North=False, sExit=Room4A, eExit=Room5A)

        Game.currentRoom = Room1A
        Game.Score = 0

    def setupGUI(self):
        # Organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the image to the left of the GUI
        # the widget is a TKinter label
        # don't let the image control the widget size
        img = None

        Game.image = Label(self, width=WIDTH / 2, image=img)
        Game.image.image = img
        Game.image.grid(row=0, column=0)
        Game.image.pack_propagate(False)

        Game.img = PhotoImage(file="skull.gif")
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

        # setup the text to the right of the GUI
        # first the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH / 4)
        # widget is a TKINTER Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.grid(row=0, column=2)
        text_frame.grid(row=0, column=2)
        text_frame.pack_propagate(False)

        # menu bar at bottom
        var = StringVar()
        panel3 = Label(self, textvariable=var).grid(row=2, column=0, columnspan=1)

        var2 = StringVar()
        panel4 = Label(self, textvariable=var2).grid(row=2, column=1, columnspan=1)

        var3 = StringVar()
        panel5 = Label(self, textvariable=var3).grid(row=2, column=2, columnspan=1)

        Button(self, text="Quit").grid(row=2, column=4, columnspan=1)
        Button(self, text="Quit").grid(row=2, column=5, columnspan=1)

        var.set("Score:0000(1)")
        var2.set("Score:0000(2)")
        var3.set("Score:0000(3)")

    def status(self, response=None):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if response == None:
            response = "Welcome to the Labyrinth."
        if (Game.currentRoom.name == "Test_Room_7A"):
            # if dead, let the player know
            response = "Congratulations you have found the exit"

        # otherwise, display the appropriate status
        Game.text.insert(END, str(Game.currentRoom) + "\n\n" + response)
        Game.text.config(state=DISABLED)

    def questionStatus(self, response):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)

        response = "To get through the door answer the question\n" + response

        # otherwise, display the appropriate status
        Game.text.insert(END, response)
        Game.text.config(state=DISABLED)



    def play(self):
        self.createRooms()
        self.setupGUI()
        self.status()


    def moveRoom(self, direction):
        global DIRECTION
        # needs to check if door is locked and find question if it is
        if direction in Game.currentRoom.exits:
            if Game.currentRoom.exits[direction][0] == False:
                response = "Room Changed"
                Game.currentRoom = Game.currentRoom.exits[direction][1]
                self.Score += 1
                self.status(response)
            elif Game.currentRoom.exits[direction][0] == True:
                self.askQuestion()
                question()
                DIRECTION = direction

    def askQuestion(self):
        global TEMPQUESTION
        QNAME = selectQuestion()
        TEMPQUESTION = QUESTIONDICT[QNAME]
        response = "{}\n{}\n{}\n{}".format(QNAME, TEMPQUESTION[0][0], TEMPQUESTION[1][0], TEMPQUESTION[2][0], TEMPQUESTION[3][0])
        self.questionStatus(response)

    def unlockExit(self, direction):
        Game.currentRoom.exits[direction][0] = False




####################################################
# Functions
def detectKeyboardInputM():
    # if you detect keyboard input call the function Game.moveRoom(direction)
    if msvcrt.kbhit():
        key = msvcrt.getch()

        # WSAD will be used to move from room to room
        if key == "w":
            g.moveRoom("north")
        if key == "s":
            g.moveRoom("south")
        if key == "a":
            g.moveRoom("west")
        if key == "d":
            g.moveRoom("east")


def detectKeyboardInputQ():
    # if you detect keyboard input call the function Game.moveRoom(direction)
    if msvcrt.kbhit():
        key = msvcrt.getch()
        temp = None
        # 1,2,3,4 will be placeholders for A,B,C,D
        if key == "1":
            answerQuestion(0)
        if key == "2":
            answerQuestion(1)
        if key == "3":
            answerQuestion(2)
        if key == "4":
            answerQuestion(3)


def saveScore():
    readSave()
    # function switches to the scoreboard and Saves the score onto the save file
    # also references the score file to pull up the top 5


def question():
    global QUESTIONMODE
    QUESTIONMODE = True


def answerQuestion(choice):
    global QUESTIONMODE
    global SCORE
    if TEMPQUESTION[choice][1] == "T":
        print "correct"
        SCORE += 100
        QUESTIONMODE = False
        g.status()
        g.unlockExit(DIRECTION)
    else:
        print "incorrect"



def generateSave():
    if os.path.isfile("save.txt") == False:
        text_file = open("save.txt", "w")
        text_file.writelines(DEFAULTSCORES)
        text_file.close()
        # This function Generates a save if a save file is not found


def readSave():
    with open('save.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    return data


def formatData():
    rawData = []
    # with is like your try .. finally block in this case
    with open("Questions.txt", 'r') as file:
        # reads the text file and turns each line into a string
        data = file.readlines()

    # splits each entry of the data list
    for i in range(len(data)):
        rawData.append(data[i].split("|"))

    for i in range(len(rawData)):
        QUESTIONDICT[rawData[i][0]] = [[rawData[i][1], rawData[i][2]],
                                       [rawData[i][3], rawData[i][4]],
                                       [rawData[i][5], rawData[i][6]],
                                       [rawData[i][7], rawData[i][8]]]

        QUESTIONBANK.append(rawData[i][0])
        QUESTIONDICT[rawData[i][0]][3][1] = QUESTIONDICT[rawData[i][0]][3][1][0]


def selectQuestion():
    temp = randint(0, len(QUESTIONBANK) - 1)
    return QUESTIONBANK[temp]


####################################################
# Main Program
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# Checks to see if a save file exists and if one is not found it creates a savefile
generateSave()
formatData()

# wait for the window to close
# substitutes mainloop due to window.mainloop being an Infinite While true loop
while True:
    window.update()
    detectKeyboardInputM()
    while QUESTIONMODE == True:
        window.update()
        detectKeyboardInputQ()
        Timer += 1
        sleep(.1)
    if g.currentRoom.name == EXIT:
        saveScore()

    Timer += 1
    sleep(.1)
    if Timer == 60:  # when the timer reaches the limit the game will switch to the score board and player score will be saved
        # change to Scoreboard and save score
        pass
