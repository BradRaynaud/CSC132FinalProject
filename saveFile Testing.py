from sys import *
import os.path

PreDetermined = ["Line1\n", "Line2\n", "Line3\n", "Line4\n", "Line5\n"]

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

print data
print "Your name: " + data[0]


# now change the 2nd line, note that you have to add a newline
data[1] = 'Mage\n'

# and write everything back
with open('stats.txt', 'w') as file:
    file.writelines(data)
