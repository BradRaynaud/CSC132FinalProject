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

    def addExit(self, exit, room, islocked=False, key=None):
        # append the exit, room, islocked, and key to the appropriate dictionary
        self._exits[exit] = [room, islocked, key]

#####################################################
R2 = Room("test2")
R1 = Room("test")
R1.addExit("north",R2)

print R1.exits
