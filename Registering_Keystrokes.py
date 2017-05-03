# program to register key strokes

import pygame
from time import sleep
pygame.init()
while True:
    for event in pygame.event.get():
        if event.type is KEYDOWN:
            _ = pygame.key.name(event.key)
            print _

            if _ is "left":
                print "west"
            elif _ is "right":
                print "east"
            elif _ is "up":
                print "north"
            elif _ is "down":
                print "south"
        #if this doesn't work, let me know
        key = pygame.key.get_pressed()
        print key
    sleep(4)