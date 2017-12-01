from __future__ import division
from sys import float_info
from kFold import kFold as fungsi
import random

def probabilitasP(dE,T):
    return float_info.epsilon**(dE/T)

if __name__=='__main__':
    K = random.randrange(500, 1500)
    T = 100000
    curr_K = K
    curr_state = fungsi(K)
    BEST_SO_FAR = curr_state

    i = 0
    for i in range(1, 300):
        K = random.randrange(500, 1500)

        new_state = fungsi(K)
        DeltaE = curr_state - new_state
        # print curr_state,i,curr_K

        if (DeltaE < 0):
            curr_state = new_state
            Best_K = K
            BEST_SO_FAR = curr_state
            print BEST_SO_FAR, Best_K
            # print i
        else:
            p = probabilitasP(DeltaE, T)
            if (p >= random.random()):
                curr_state = new_state
        T = T * 0.9

print('Bestever : '+str(BEST_SO_FAR))