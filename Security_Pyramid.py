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

#####################################################
# Variables
Timer = 0
TEMPQUESTION = {"Test":[["IncorrectA", False], ["IncorrectB", False], ["CorrectC", True], ["IncorrectD", False]]}
EXIT = "Test_Room_7A"

#####################################################
# Room Class

class Room(object):
    # Constructor for the Room Class
    def __init__(self, name):
        # information about constructor goes here
        self.name = name
        self.exits = {}

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
        s = "{} ".format(self.name)
        s += str(self.exits)
        return s


#####################################################
# Game Class

class Game(Frame):
    def __init(self, parent):
        Frame.__init__(self, parent)

    def createRooms(self):
        Room1A = Room("Test_Room_1A")
        Room2A = Room("Test_Room_2A")
        Room3A = Room("Test_Room_3A")
        Room4A = Room("Test_Room_4A")
        Room5A = Room("Test_Room_5A")
        Room6A = Room("Test_Room_6A")
        Room7A = Room("Test_Room_7A")
        Room8A = Room("Test_Room_8A")
        Room9A = Room("Test_Room_9A")
        Room1A.addExits(South= False,nExit=Room5A, eExit=Room2A, wExit=Room4A, northLocked= True)
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
        self.pack(fill=BOTH, expand=1)
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

    def status(self, response=None):
        c = "you are in room {} and possible exits include {}, and {}, Score is {}".format(
            Game.currentRoom.name, Game.currentRoom.exits.keys(), response, Game.Score)
        print c

    def play(self):
        self.createRooms()
        self.setupGUI()
        self.status()

    def process(self, event):
        action = Game.player_input.get()
        action = action.lower()

        if action == "quit" or action == "exit" or action == "bye":
            quit()
            response = "you tried to quit"

        words = action.split()

        response = "Try Again"

        if len(words) == 2:
            verb = words[0]
            noun = words[1]

            # the verb is go
            if verb == "go":
                # sets a default response
                response = "Invalid Exit"
                self.moveRoom(noun)

        Game.player_input.delete(0, END)  # clears the player input

    def moveRoom(self, direction):
        # needs to check if door is locked and find question if it is
        if direction in Game.currentRoom.exits:
            if Game.currentRoom.exits[direction][0] == False:
                response = "Room Changed"
                Game.currentRoom = Game.currentRoom.exits[direction][1]
                self.Score += 1
                self.status(response)
            elif Game.currentRoom.exits[direction][0] == True:
                response = "This exit is locked answer the question to continue or press 5 to give up"
                self.status(response)
                print "{}\nA):{}\nB):{}\nC):{}\nD):{}".format \
                    (TEMPQUESTION.keys(), TEMPQUESTION["Test"][0][0], TEMPQUESTION["Test"][1][0],
                     TEMPQUESTION["Test"][2][0], TEMPQUESTION["Test"][3][0])
                question()

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
    quit()
    # function switches to the scoreboard and Saves the score onto the save file
    # also references the score file to pull up the top 5

def question():
    global QUESTIONMODE
    QUESTIONMODE = True

def answerQuestion(choice):
    global QUESTIONMODE
    for answer in TEMPQUESTION:
        if TEMPQUESTION[answer][choice][1] == True:
            print "correct"
            QUESTIONMODE = False
        else:
            print "incorrect"

def generateSave():
    pass
    # This function Generates a save if a save file is not found


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


GAMEOVER = False
QUESTIONMODE = False

# wait for the window to close
# substitutes mainloop due to window.mainloop being an Infinite While true loop
generateSave()
while True:
    window.update()
    detectKeyboardInputM()
    while QUESTIONMODE == True:
        detectKeyboardInputQ()
        Timer += 1
        sleep(.1)
    if g.currentRoom.name == EXIT:
        saveScore()


    Timer += 1
    sleep(.1)
    if Timer == 60: # when the timer reaches the limit the game will switch to the score board and player score will be saved
        # change to Scoreboard and save score
        pass
