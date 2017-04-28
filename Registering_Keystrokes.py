# program to register key strokes

import pygame
from time import sleep
pygame.init()
while True:
    if pygame.key.get_focused() == True:
        key = pygame.key.get_pressed()
        print key
    sleep(4)