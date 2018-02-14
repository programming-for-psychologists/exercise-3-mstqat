import random

# Generate a trial list
# parameters middleList = [] | innerList = [] | numRepetitions = integer
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
  
#double number of trials in each block
trialList = repetition(["left","right"],["masked","masked","unmasked"]*2,range(1,6))

#print doubled, preshuffled blocks
for block in trialList:
    random.shuffle(block)
    for trial in block:
        print ", ".join(trial)

"""
Instructions 5 - Double the number of trials in each block (so that the repetitions are not 
 quite so predictable), and then randomize within each block as in part 4.
"""