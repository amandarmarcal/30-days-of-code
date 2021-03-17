#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    maxGlobal = 0
    maxLocal = 0
    
    strBin = bin(n)
    strBin = strBin[2:]
    
    for i in strBin:
        if int(i) == 1:
            maxLocal+=1
        else:
            if maxLocal > maxGlobal:
                maxGlobal = maxLocal
            maxLocal = 0

        if maxLocal > maxGlobal:
            maxGlobal = maxLocal

    print (maxGlobal)



    
