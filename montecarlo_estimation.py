#Courtney Peterson
#CSCI2244: Randomness and Computation

from __future__ import print_function, division
import numpy as np  # this is a universal shorthand for numpy
import matplotlib.pyplot as plt
import random

'''This program estimates the answer to...

A bit string of length n is generated randomly, where the value of each bit in the string
is independent of the values of all the other bits. Moreover, each bit takes the value 1
with probability 0.2 (and 0 otherwise).
Determine the probability that there is at least one 1 in the string (the length of the string is n).

...using Monte-Carlo simulations."""

def bitstring(trial_num, p):
    trialn=[]
    i = 0
    for n in range(1, 16):
        num = 0
        for i in range(0, trial_num + 1):
            sarray = np.random.choice([0,1],p=[1-p,p],size=n)
            if (np.sum(sarray) > 0):
                num+=1
        trialn.append(float(num)/trial_num)
    return trialn
    print(trialn)

def formula_line():
    form_array = []
    for i in range(1, 16):
        form_array.append(1-(.8)**i)
    return form_array

def plot(trial_num, p) :
    num = bitstring(trial_num, p)
    formula = formula_line()
    fig = plt.figure()
    plt.plot(np.arange(15), num)
    plt.plot(np.arange(15), formula)

    plt.title(('# of ones in bit string with n {:d} length and {:.2f} probability').format(trial_num, p), y=1.05)

    plt.xlabel('Length of String')
    plt.ylabel('Probability of there being at least one 1')
    plt.grid(axis='both', ls=':')
    fig.savefig('Fig1.png')
    return None

plot(5000, .2)
plt.show()
