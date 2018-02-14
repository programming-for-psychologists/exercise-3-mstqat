"""Have your generate trials routine do all the 
randomization ahead of time such that your trials file (here, trialList.txt) 
contains the exact trial order that will be seen by a participant. There are 
two reasons. 
    First, this lets you modularize all the trial handling outside of your main 
experiment script. 
    Second, it allows you to save individual trial files that show the trial order 
seen by a given participant. It comes in handy for making sure your trial list 
is set up as you want it. So: let's go ahead and randomize the trial list 
before printing.
"""
import random

# Generate a trial list
# parameters middleList = [] | innerList = [] | numRepetitions = integer
def repetition(innerList, middleList, blockNumList):
    trialList = []
    for blocknumber in blockNumList:
        for masked in middleList:
            for side in innerList:
                #trialList is a non-random list of multiple tuples
                #each tuple is a single trial
                trialList.append((str(blocknumber),masked,side))
    return trialList
                
# to generate 5 blocks with 2/3 of trials masked, and 1/2 of trials on right 
# side, with each block of trials including at least one of each trial type
# call function with this:
trialList = repetition(["left","right"],["masked","masked","unmasked"],range(1,6))

random.shuffle(trialList)
for i in trialList:
    print ", ".join(i)
