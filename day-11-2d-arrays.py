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
    
    sum_list = []
    glass_sum = 0
    
    for row in range(0, 4):
        for column in range(0, 4):       
            glass_1 = arr[row][column] + arr[row][column+1] + arr[row][column+2]
            glass_2 = arr[row+1][column+1]
            glass_3 = arr[row+2][column] + arr[row+2][column+1] + arr[row+2][column+2]
            glass_sum = glass_1 + glass_2 + glass_3
            sum_list.append(glass_sum)
    
    print(max(sum_list))
