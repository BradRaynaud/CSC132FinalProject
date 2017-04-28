#####################################################
#
#
#
#
#####################################################
# Imports

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
    def generateExit(self, Direction, Exists, Locked):
        if Exists == True:
            self.exits[Direction] = Locked

    # Assumes that rooms exist in all 4 directions and they are unlocked, arguments can be provided to remove exits
    # and lock exits
    def addExits(self, North=True, South=True, East=True, West=True, northLocked=False, southLocked=False,
                 eastLocked=False, westLocked=False):
        self.generateExit("North", North, northLocked)
        self.generateExit("South", South, southLocked)
        self.generateExit("East", East, eastLocked)
        self.generateExit("West", West, westLocked)

    def __str__(self):
        s = "{} ".format(self.name)
        s += str(self.exits)
        return s


#####################################################
# Main Program

Room1A = Room("Test_Room_1A")
Room1A.addExits(northLocked=True, South=False)
print Room1A
