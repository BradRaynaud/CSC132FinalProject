#####################################################
#
#
#
#
#####################################################
# Imports
from time import sleep
from Tkinter import *


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
        Room1A.addExits(nSouth=False, nExit=Room5A, eExit=Room2A, wExit=Room4A)
        Room2A.addExits(East=False, sExit=Room7A, nExit=Room6A, wExit=Room1A)
        Room3A.addExits(North=False, South=False, eExit=Room7A, wExit=Room8A)
        Room4A.addExits(West=False, eExit=Room1A, nExit=Room9A, sExit=Room8A)
        Room5A.addExits(North=False, sExit=Room1A, eExit=Room6A, wExit=Room9A)
        Room6A.addExits(North=False, East=False, wExit=Room5A, sExit=Room2A)
        Room7A.addExits(South=False, East=False, nExit=Room2A, wExit=Room3A)
        Room8A.addExits(South=False, West=False, eExit=Room3A, nExit=Room4A)
        Room9A.addExits(West=False, North=False, sExit=Room4A, eExit=Room5A)

        Game.currentRoom = Room1A

    def setupGUI(self):
        self.pack(fill=BOTH, expand=1)
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

    def status(self, response=None):
        c = "you are in room {} and possible exits include {}, and {}".format(Game.currentRoom.name,
                                                                              Game.currentRoom.exits.keys(), response)
        print c

    def play(self):
        self.createRooms()
        self.setupGUI()
        self.status()

    def process(self, event):
        action = Game.player_input.get()
        action = action.lower()

        if (action == "quit" or action == "exit" or action == "bye"):
            quit(0)

        words = action.split()

        response = "Try Again"

        if len(words) == 2:
            verb = words[0]
            noun = words[1]

        # the verb is go
        if verb == "go":
            # sets a default response
            response = "Invalid Exit"
            if noun in Game.currentRoom.exits:
                if Game.currentRoom.exits[noun][0] == False:
                    print "EUREKA"

        self.status(response)


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

# wait for the window to close
window.mainloop()
