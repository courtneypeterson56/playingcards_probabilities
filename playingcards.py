#Courtney Peterson
#CSCI2244: Randomness and Computation

from __future__ import print_function, division
import numpy as np  # this is a universal shorthand for numpy
import matplotlib.pyplot as plt
import random

"""Two cards are randomly chosen without replacement from an ordinary deck of 52 cards. Simulate probability of...

1.Both cards chosen are queens given Queen of Spades is chosen.
2.Both cards are queens given at least one Queen is chosen.

10,000 trials gets good approximations
for these conditional probabilities """

def playingcards(n):
    #0-4 Queen
    #0 is Queen of Spades

    nE1 = 0
    nE2 = 0
    nE3 = 0

    for i in range(0, n):
        list1 = np.random.choice(51, size=1) #already pulled one out that is Queen of Spades
        if list1[0]==1 or list1[0]==2 or list1[0]==3:
                nE1 +=1
    print("The times both cards chosen are Queens and one is Queen of Spades:", nE1)
    print ("The probability that both cards chosen are Queens given Queen of Spades is chosen:", nE1/n)

    for i in range(0, n):
        list2 = np.random.choice(52, size=2)
        if list2[0] == 0 or list2[0] ==1 or list2[0] ==2 or list2[0] ==3:
            if list2[1] == 0 or list2[1] ==1 or list2[1] ==2 or list2[1] ==3:
                nE2 +=1
        if list2[0] in range(0,4) or list2[1] in range(0,3):
            nE3 += 1
    print("The times both cards chosen are Queens:", nE2, "And one queen is chosen:", nE3)
    print ("The probability that both cards are Queens given at least one Queen is chosen:", (nE2/n)/(nE3/n))

playingcards(10000)
