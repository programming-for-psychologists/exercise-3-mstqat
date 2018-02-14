"""4 - Simply randomizing the enture list messes up the block structure
 creating the possibility that participants will see the same trial multiple 
 times in a row. For this part, randomize the trials within each block before 
 printing the list.
"""
import random

# Generate a trial list
                
# generate blocks of trials
# middleList = [] | innerList = [] | numRepetitions = integer
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
  
trialList = repetition(["left","right"],["masked","masked","unmasked"],range(1,6))

# print each pre-shuffled block in order
for block in trialList:
    random.shuffle(block)
    for trial in block:
        print ", ".join(trial)
