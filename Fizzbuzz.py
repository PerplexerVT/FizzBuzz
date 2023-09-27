##!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    a = 1;
    while n >= a:
        flag = False
        output = str(a)
        if a % 3 == 0:
            flag = True
            output = "Fizz"
        if a % 5 == 0:
            if flag == True:
                output += "Buzz"
            else:
                output = "Buzz"
        print(output)
        a+=1

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
