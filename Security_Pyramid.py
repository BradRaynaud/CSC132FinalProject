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
global SCORE
SCORE = 0
TEMPQUESTION = []
EXIT = "Test_Room_7A"
DEFAULTSCORES = ["Cade:2500\n", "Tristan:1500\n", "Brad:1200\n", "Andrew:1000\n", "John:700\n"]
GAMEOVER = False
global QUESTIONMODE
QUESTIONMODE = False
QUESTIONDICT = {}
QUESTIONBANK = []
DIRECTION = None
LIVES = 3
global ATTEMPTS
ATTEMPTS = 2
GAMEACTIVE = True

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


    # Function generates the rooms
    def createRooms(self):
        A1 = Room("Room A1")
        A2 = Room("Room A2")
        A3 = Room("Room A3")
        A4 = Room("Room A4")
        A5 = Room("Room A5")
        A6 = Room("Room A6")
        A7 = Room("Room A7")
        A8 = Room("Room A8")

        B1 = Room("Room B1")
        B2 = Room("Room B2")
        B3 = Room("Room B3")
        B4 = Room("Room B4")
        B5 = Room("Room B5")
        B6 = Room("Room B6")
        B7 = Room("Room B7")
        B8 = Room("Room B8")

        C1 = Room("Room C1")
        C2 = Room("Room C2")
        C3 = Room("Room C3")
        C4 = Room("Room C4")
        C5 = Room("Room C5")
        C6 = Room("Room C6")
        C7 = Room("Room C7")
        C8 = Room("Room C8")

        D1 = Room("Room D1 : Exit")
        D2 = Room("Room D2")
        D3 = Room("Room D3")
        D4 = Room("Room D4")
        D5 = Room("Room D5")
        D6 = Room("Room D6")
        D7 = Room("Room D7")
        D8 = Room("Room D8")

        E1 = Room("Room E1")
        E2 = Room("Room E2")
        E3 = Room("Room E3")
        E4 = Room("Room E4")
        E5 = Room("Room E5")
        E6 = Room("Room E6")
        E7 = Room("Room E7")
        E8 = Room("Room E8 : Entrance")

        F1 = Room("Room F1")
        F2 = Room("Room F2")
        F3 = Room("Room F3")
        F4 = Room("Room F4")
        F5 = Room("Room F5")
        F6 = Room("Room F6")
        F7 = Room("Room F7")
        F8 = Room("Room F8")

        G1 = Room("Room G1")
        G2 = Room("Room G2")
        G3 = Room("Room G3")
        G4 = Room("Room G4")
        G5 = Room("Room G5")
        G6 = Room("Room G6")
        G7 = Room("Room G7")
        G8 = Room("Room G8")

        H1 = Room("Room H1")
        H2 = Room("Room H2")
        H3 = Room("Room H3")
        H4 = Room("Room H4")
        H5 = Room("Room H5")
        H6 = Room("Room H6")
        H7 = Room("Room H7")
        H8 = Room("Room H8")

        A1.addExits(eExit=B1, sExit=A2, North=False, West=False)
        A2.addExits(nExit=A1, eExit=B2, South=False, West=False)
        A3.addExits(eExit=B3, sExit=A4, North=False, West=False, southLocked=True)
        A4.addExits(nExit=A3, South=False, East=False, West=False)
        A5.addExits(eExit=B5, sExit=A6, North=False, West=False)
        A6.addExits(nExit=A5, eExit=B6, South=False, West=False)
        A7.addExits(eExit=B7, sExit=A8, North=False, West=False)
        A8.addExits(nExit=A7, eExit=B8, South=False, West=False, northLocked=True)

        B1.addExits(wExit=A1, North=False, South=False, East=False)
        B2.addExits(wExit=A2, sExit=B3, North=False, East=False, westLocked=True)
        B3.addExits(nExit=B2, wExit=A3, sExit=B4, East=False)
        B4.addExits(sExit=B5, nExit=B3, East=False, West=False)
        B5.addExits(nExit=B4, wExit=A5, East=False, South=False, northLocked=True)
        B6.addExits(wExit=A6, sExit=B7, North=False, East=False, westLocked=True)
        B7.addExits(nExit=B6, wExit=A7, East=False, South=False)
        B8.addExits(wExit=A8, eExit=C8, North=False, South=False)

        C1.addExits(eExit=D1, sExit=C2, North=False, West=False, eastLocked=True)
        C2.addExits(nExit=C1, sExit=C3, East=False, West=False, northLocked=True)
        C3.addExits(nExit=C2, sExit=C4, East=False, West=False, northLocked=True)
        C4.addExits(nExit=C3, sExit=C5, West=False, East=False)
        C5.addExits(nExit=C4, eExit=D5, South=False, West=False, northLocked=True)
        C6.addExits(eExit=C5, sExit=C7, North=False, West=False)
        C7.addExits(nExit=C6, eExit=D7, South=False, West=False)
        C8.addExits(eExit=D8, wExit=B8, North=False, South=False, westLocked=True)

        D1.addExits(wExit=C1, North=False, East=False, South=False)
        D2.addExits(eExit=E2, North=False, South=False, West=False)
        D3.addExits(eExit=E3, sExit=D4, North=False, West=False)
        D4.addExits(nExit=D3, eExit=E4, South=False, West=False, eastLocked=True)
        D5.addExits(wExit=C5, eExit=E5, North=False, South=False, westLocked=True)
        D6.addExits(wExit=C6, eExit=E6, North=False, South=False, eastLocked=True)
        D7.addExits(wExit=C7, eExit=E7, sExit=D8, North=False, westLocked=True, southLocked=True)
        D8.addExits(wExit=C8, eExit=E8, North=False, South=False)

        E1.addExits(eExit=F1, sExit=E2, North=False, West=False, eastLocked=True)
        E2.addExits(nExit=E1, eExit=F2, wExit=D2, South=False, westLocked=True)
        E3.addExits(wExit=D3, eExit=F3, North=False, South=False, westLocked=True)
        E4.addExits(wExit=D4, North=False, South=False, East=False)
        E5.addExits(wExit=D5, sExit=E6, North=False, East=False)
        E6.addExits(nExit=E5, wExit=D6, East=False, South=False)
        E7.addExits(wExit=D7, eExit=F7, North=False, South=False)
        E8.addExits(eExit=F8, North=False, South=False, West=False, eastLocked=True)

        F1.addExits(wExit=E1, North=False, South=False, East=False)
        F2.addExits(wExit=E2, eExit=G2, North=False, South=False)
        F3.addExits(wExit=E3, eExit=G3, sExit=F4, North=False, eastLocked=True)
        F4.addExits(nExit=F3, eExit=G4, sExit=F5, West=False)
        F5.addExits(nExit=F4, sExit=F6, East=False, West=False, southLocked=True)
        F6.addExits(nExit=F5, sExit=F7, East=False, West=False)
        F7.addExits(nExit=F6, wExit=E7, East=False, South=False, westLocked=True)
        F8.addExits(wExit=E8, eExit=G8, South=False, North=False)

        G1.addExits(sExit=G2, eExit=H1, North=False, West=False)
        G2.addExits(wExit=F2, nExit=G1, East=False, South=False, westLocked=True)
        G3.addExits(wExit=F3, North=False, South=False, East=False)
        G4.addExits(wExit=F4, eExit=H4, North=False, South=False, westLocked=True)
        G5.addExits(eExit=H5, sExit=G6, North=False, West=False, eastLocked=True)
        G6.addExits(nExit=G5, sExit=G7, East=False, South=False)
        G7.addExits(nExit=G6, sExit=G8, eExit=H7, West=False, northLocked=True)
        G8.addExits(wExit=F8, nExit=G7, East=False, South=False, northLocked=True)

        H1.addExits(wExit=G1, sExit=H2, North=False, East=False)
        H2.addExits(nExit=H1, sExit=H3, East=False, West=False, northLocked=True)
        H3.addExits(nExit=H2, sExit=H4, East=False, West=False)
        H4.addExits(nExit=H3, sExit=H5, wExit=G4, East=False, westLocked=True)
        H5.addExits(nExit=H4, sExit=H6, wExit=G5, East=False, northLocked=True, southLocked=True)
        H6.addExits(nExit=H5, East=False, South=False, West=False)
        H7.addExits(wExit=G7, sExit=H8, North=False, East=False, southLocked=True)
        H8.addExits(nExit=H7, East=False, South=False, West=False)


        Game.currentRoom = E8

    # Function creates and formats the GUI
    def setupGUI(self, i):
        if i == 0:
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

            Button(self, text="Give Up", command = lambda: saveScore()).grid(row=2, column=4, columnspan=1)


    # exports the status to the GUI
    def status(self, response=None):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if response == None:
            response = "Welcome to the Labyrinth."
        if (Game.currentRoom.name == "Room D1 : Exit"):
            # if the end is found let the player know
            response = "Congratulations you have found the exit"

        # otherwise, display the appropriate status
        Game.text.insert(END, str(Game.currentRoom) +"\nScore:{}\nLives:{}\nAttempts Remaining:{}".format(SCORE,LIVES,ATTEMPTS) + "\n\n" + response)
        Game.text.config(state=DISABLED)

    # exports a status to the GUI when the player is asked a question
    def questionStatus(self, response):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)

        response = "\nTo get through the door answer the question\n\n" + response

        # otherwise, display the appropriate status
        Game.text.insert(END, str(Game.currentRoom) +"\nScore:{}\nLives:{}\nAttempts Remaining:{}\n"
                         .format(SCORE,LIVES,ATTEMPTS) + response)
        Game.text.config(state=DISABLED)

    # function that starts the GUI and plays the game
    def play(self):
        self.createRooms()
        self.setupGUI(0)
        self.status()

    # function that moves the player from room to room
    # if exit is locked it calls the askquestion function to setup the question mode
    def moveRoom(self, direction):
        global DIRECTION
        # needs to check if door is locked and find question if it is
        if direction in Game.currentRoom.exits:
            if Game.currentRoom.exits[direction][0] == False:
                response = "Room Changed"
                Game.currentRoom = Game.currentRoom.exits[direction][1]
                self.status(response)
            elif Game.currentRoom.exits[direction][0] == True:
                self.askQuestion()
                DIRECTION = direction

    # function that selects a question from the Dictionary and formats and exports the question to the questionStatus
    #  function
    def askQuestion(self):
        global TEMPQUESTION
        QNAME = selectQuestion()
        TEMPQUESTION = QUESTIONDICT[QNAME]
        response = "{}\n{}\n{}\n{}\n{}".format(QNAME, TEMPQUESTION[0][0], TEMPQUESTION[1][0], TEMPQUESTION[2][0], TEMPQUESTION[3][0])
        self.questionStatus(response)
        question()

    # unlocks your current rooms exit in the direction provided via argument
    def unlockExit(self, direction):
        Game.currentRoom.exits[direction][0] = False





####################################################
# Functions

# Function that looks to see if any "hotkeys" are pressed
def detectInput(arg):
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if arg == 0:
            # WSAD will be used to move from room to room
            if key == "w":
                g.moveRoom("north")
            if key == "s":
                g.moveRoom("south")
            if key == "a":
                g.moveRoom("west")
            if key == "d":
                g.moveRoom("east")
        if arg == 1:
            # 1,2,3,4 will be placeholders for A,B,C,D
            if key == "1":
                answerQuestion(0)
            if key == "2":
                answerQuestion(1)
            if key == "3":
                answerQuestion(2)
            if key == "4":
                answerQuestion(3)


# This function is called when the game is over or the player quits
def saveScore():
    savedata = readSave()
    savedata = formatSave(savedata)
    savedata = compareData(savedata, SCORE)
    savedata = reformatData(savedata)
    pushData(savedata)
    global GAMEACTIVE
    GAMEACTIVE = False

    # function switches to the scoreboard and Saves the score onto the save file
    # also references the score file to pull up the top 5

# This function starts question mode
def question():
    global QUESTIONMODE
    QUESTIONMODE = True

# this function is called when the player presses one of the assigned buttons for A/B/C/D
# if the choice is correct then the player is "rewarded" by having their global point score increased
# if the choice is incorrect then the player is "penalized" by loosing one of their remaining attempts
# if the player runs out of attempts then the door unlocks but they loose a life
def answerQuestion(choice):
    global QUESTIONMODE
    global LIVES
    global SCORE
    global ATTEMPTS
    if ATTEMPTS > 0:
        if TEMPQUESTION[choice][1] == "T":
            print "correct"
            SCORE += 100
            QUESTIONMODE = False
            g.status()
            g.unlockExit(DIRECTION)
        else:
            print "incorrect"
            ATTEMPTS -= 1

    else:
        LIVES -= 1
        print LIVES
        QUESTIONMODE = False
        ATTEMPTS = 2
        g.unlockExit(DIRECTION)
        g.status()

# This function checks to see if the save file exists and if one is found then nothing happens
# however, if one is not found a file called save.txt is generated
def generateSave():
    if os.path.isfile("save.txt") == False:
        text_file = open("save.txt", "w")
        text_file.writelines(DEFAULTSCORES)
        text_file.close()
        # This function Generates a save if a save file is not found

# This function reads the save and converts it into a list
# the list is returned
def readSave():
    with open('save.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    return data

# This function reads the Questions.txt file and converts each line into a string
# The string is then put into a list in order of occurence. After the string in each index of rawData is converted into
# a dictionary in the format Dict[QuestionName] = [ [AnswerA, T or F], [AnswerB, T or F], [AnswerC, T or F], [AnswerD, T or F] ]
# each key is then added to the list QUESTIONBANK
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

# chooses a random index of the QUESTIONBANK
def selectQuestion():
    temp = randint(0, len(QUESTIONBANK) - 1)
    return QUESTIONBANK[temp]

# formats the raw data into something that can be used
def formatSave(data):
    for index in range(len(data)):
        data[index] = data[index].split(":")
        data[index][1] = data[index][1].split("\n")
        del data[index][1][1]
        data[index][1][0] = int(data[index][1][0])
        data[index][1] = data[index][1][0]
    return data

# compares the scores and overwrites the appropriate scores
def compareData(data, score):
    for index in range(len(data)):
        if score > data[index][1]:
            data[index][1] = score
            data[index][0] = "Player"
            break
    return data

# formats the data into something that can be pushed back into the save file
def reformatData(data):
    for index in range(len(data)):
        data[index] = str(data[index][0]) + ":" + str(data[index][1]) + "\n"
    return data

# writes the save data back into the save.txt
def pushData(data):
    print data
    with open('save.txt', 'w') as file:
        file.writelines(data)



####################################################
# Main Program
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Maze Gate")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# Checks to see if a save file exists and if one is not found it creates a savefile
generateSave()

# pulls all the questions from the Questions.txt file and converts it into something usable
formatData()


# wait for the window to close
# substitutes mainloop due to window.mainloop being an Infinite While true loop
while GAMEACTIVE == True:
    window.update()
    if LIVES != 0:
        detectInput(0)
    while QUESTIONMODE == True:
        window.update()
        detectInput(1)
        Timer += 1
        sleep(.1)
    if g.currentRoom.name == EXIT:
        saveScore()
    if LIVES == 0:
        saveScore()
        response = "You are out of lives Give up"
        g.status(response)

    Timer += 1
    sleep(.1)
    if Timer == 60:  # when the timer reaches the limit the game will switch to the score board and player score will be saved
        # change to Scoreboard and save score
        pass
quit()