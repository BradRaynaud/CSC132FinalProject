import RPi.GPIO as GPIO
from time import sleep

# These are set up individually so that they can be interpreted
# individually by the program

GPIO.setmode(GPIO.BCM)

#Took me a bit to realize what the whole "GPIO.PUD_DOWN" was actually doing
#turns out its actually a built in feature that prevents debouncing
#pretty neat. Also, did each one individually so that it was
#easier to call them individually.

#These are for MOVEMENT
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#These are for answering QUESTIONS
GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


try:
    while True:
        # The button linked to 21 will be the one that moves the player
        # north
        #again, these are for MOVEMENT
        inputN = GPIO.input(21)
        inputS = GPIO.input(20)
        inputE = GPIO.input(16)
        inputW = GPIO.input(17)

        #and these are for answering QUESTIONS
        inputA = GPIO.input(25)
        inputB = GPIO.input(24)
        inputC = GPIO.input(23)
        inputD = GPIO.input(18)

        #these are for MOVEMENT
        # if the switch connected to 21 is pressed, print north
        if inputN:
            print "North"
        # if the switch connected to 20 is pressed, print south
        elif inputS:
            print "South"
        # if the switch connected to 16 is pressed, print east
        elif inputE:
            print "East"
        # if the button connected to 17 is pressed, print west
        elif inputW:
            print "West"
            
        #these are for QUESTIONS
        elif inputA:
            print "Answer A chosen"
        elif inputB:
            print "Answer B chosen"
        elif inputC:
            print "Answer C chosen"
        elif inputD:
            print "Answer D chosen"
            
        # otherwise, don't do anything
        else:
            pass
        
        # this 1 second break prevents switch bouncing from triggering
        # multiple movements after only 1 press. Increase or decrease at your own risk.
        sleep(1)

        # this can be changed at any time, just make sure not to remove the pause or the
        # switch assignments
        
#detect Ctrl+C
except KeyboardInterrupt:
    #reset the GPIO pins
    GPIO.cleanup()
    print "\nSionara!"
        
