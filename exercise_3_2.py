"""code a basic trial list for an experiment in which we display an image on
 either the left or the right side of the screen. Both sides of the screen are
 then masked, and we are interested in measuring people's ability (e.g.,
 accuracy, reaction time) in responding whether the image was on the right or
 left side of the screen, while comparing responses on masked vs. nonmasked
 trials.
 
 generate a list of trials in which some proportion is masked and some is not
 masked. Within each condition, we want the image on the left side displayed
 with some proportion of the time, and on the right the remaining times.

Let's begin by having 2/3 masked trials and 1/3 non-masked trials. Within each
 level of the masking factor, half of the targets should be on the left and
 half on the right. Let's have 5 blocks with each block having all the possible
 trial types.
 
 The code you write should output to the terminal output that looks just like
 this (that first number is the block number).
 
 $ python generateTrials.py
1,masked,right
1,masked,left
1,masked,right
1,masked,left
1,nonmasked,right
1,nonmasked,left
2,masked,right
2,masked,left
2,masked,right
2,masked,left
2,nonmasked,right
2,nonmasked,left
3,masked,right
 
 Try redirecting the output from the screen, to a file using `>`. At the
 terminal, type `python generateTrials.py > trialList.txt`. Now open up the
 trialList.txt file and your trial list should be right there. """

#parameters middleList = [] | innerList = [] | numRepetitions = integer
def repetition(innerNumList, middleNumList, blockNumList):
    for i in blockNumList:
        for j in middleNumList:
            for k in innerNumList:
                print i,j,k
                
# to generate 5 blocks with 2/3 of trials masked, and 1/2 of trials on right 
# side, with each block of trials including at least one of each trial type
# call function with 
repetition(["left","right"],["masked","masked","unmasked"],range(1,6))

""" 
 Try redirecting the output from the screen, to a file using `>`. At the
 terminal, type `python generateTrials.py > trialList.txt`. Now open up the
 trialList.txt file and your trial list should be right there. """