#

import time
import sys
import random
from psychopy import visual,event,core,gui

def repetition(letters, numberBeforeSwitch, numRepetitions):
    for i in range(numRepetitions):
        for j in letters:
            for k in range(numberBeforeSwitch):
                print j
                
                
repetition(["A","B"],4,3)
