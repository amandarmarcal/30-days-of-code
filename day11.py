#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

        
    maxGlobal = -100000000
    
    for i in range(1, len(arr)-1):
        for j in range (1, len(arr)-1):
            maxLocal = 0
            maxLocal+= sum(arr[i-1][j-1:j+2])
            maxLocal+= arr[i][j]
            maxLocal+= sum(arr[i+1][j-1:j+2])
            
            if maxLocal > maxGlobal:
                maxGlobal = maxLocal
            
    print (maxGlobal)
    