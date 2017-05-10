import RPi.GPIO as GPIO
from time import sleep

# These are set up individually so that they can be interpreted
# individually by the program

GPIO.setup(23, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

while True:
    # The button linked to 23 will be the one that moves the player
    # north
    inputN = GPIO.input(23)
    inputS = GPIO.input(18)
    inputE = GPIO.input(24)
    inputW = GPIO.input(25)
    # if the switch connected to 23 is pressed, print north
    if inputN:
        print "North"
    # if the switch connected to 18 is pressed, print south
    elif inputS:
        print "South"
    # if the switch connected to 24 is pressed, print east
    elif inputE:
        print "East"
    # if the button connected to 25 is pressed, print west
    elif inputW:
        print "West"
    # otherwise, don't do anything
    else:
        pass
    # this 1 second break prevents switch bouncing from triggering
    # multiple movements after only 1 press. Increase or decrease at your own risk.
    sleep(1)

    # this can be changed at any time, just make sure not to remove the pause or the
    # switch assignments
