#####################################################
#
#
#
#
#####################################################
# Imports
from Tkinter import *

#####################################################
# Room Class

class Room(object):
    # Constructor for the Room Class
    def __init__(self, name, image):
        # information about constructor goes here
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = {}

    # Getters and setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self,value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value



#####################################################