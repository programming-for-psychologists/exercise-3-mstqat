
#parameters middleList = [] | innerList = [] | numRepetitions = integer
def repetition(innerNumList, middleNumList, blockNumList):
    for i in blockNumList:
        for j in middleNumList:
            for k in innerNumList:
                print i,j,k

repetition(["left","right"],["masked","masked","unmasked"],range(1,6))


"""
Instructions
 code a basic trial list for an experiment in which we display an image on
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
""" 