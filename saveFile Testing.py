from sys import *
import os.path
from random import randint

rawData = []
PreDetermined = ["Line1\n", "Line2\n", "Line3\n", "Line4\n", "Line5\n"]
testDict = {}
Questionbank = []

def selectQuestion():
    temp = randint(0, len(Questionbank) - 1)
    temp2 = Questionbank[temp]
    print temp2
    print testDict[temp2]


if os.path.isfile("stats.txt") == False:
    text_file = open("stats.txt", "w")
    text_file.writelines(PreDetermined)
    text_file.close()
else:
    print "This already Exists"

def formatData():
    # with is like your try .. finally block in this case
    with open('stats.txt', 'r') as file:
        # reads the text file and turns each line into a string
        data = file.readlines()

    # splits each entry of the data list
    for i in range(len(data)):
        example.append(data[i].split("|"))

    for i in range(len(example)):
        testDict[example[i][0]] = [[example[i][1],example[i][2]],
                                   [example[i][3],example[i][4]],
                                   [example[i][5],example[i][6]],
                                   [example[i][7],example[i][8]]]

        Questionbank.append(example[i][0])
        testDict[example[i][0]][3][1] = testDict[example[i][0]][3][1][0]

formatData()
selectQuestion()