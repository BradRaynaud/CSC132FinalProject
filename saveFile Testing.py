from sys import *
import os.path
from random import randint

example = []
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


# with is like your try .. finally block in this case
with open('stats.txt', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

for i in range(len(data)):
    example.append(data[i].split("|"))

for i in range(len(example)):
    print example[i]

for i in range(len(example)):
    testDict[example[i][0]] = [example[i][1],example[i][2],example[i][3],example[i][4]]
    Questionbank.append(example[i][0])


selectQuestion()