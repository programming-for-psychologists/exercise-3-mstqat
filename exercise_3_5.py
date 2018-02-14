"""
5 - Double the number of trials in each block (so that the repetitions are not 
 quite so predictable), and then randomize within each block as in part 4.
"""

import random

# Generate a trial list
                
# parameters middleList = [] | innerList = [] | numRepetitions = integer
# k here is side of screen, j here is masking, i here is trial block
def repetition(innerList, middleList, blockNumList):
    trialList = []
    for blocknumber in blockNumList:
        blockList= []
        for masked in middleList:
            for side in innerList:
                #trialList is a non-random list of multiple tuples
                #each tuple is a single trial
                blockList.append((str(blocknumber),masked,side))
        trialList.append(blockList)
    return trialList


                
                
# to generate 5 blocks with 2/3 of trials masked, and 1/2 of trials on right 
# side, with each block of trials including at least one of each trial type
# call function with 
  
#double number of trials in each block
trialList = repetition(["left","right"],["masked","masked","unmasked"]*2,range(1,6))


for block in trialList:
    random.shuffle(block)
    for trial in block:
        print ", ".join(trial)
