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
    for i in range(1, n+1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if len(output) == 0:
            output = i
        print(output)
        n = n + 1

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
