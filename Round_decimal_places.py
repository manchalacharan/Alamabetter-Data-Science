'''
Write a Python program to round a floating-point number to specified number decimal places

Input:
10.5247
2
Output:
10.52            '''

import math

n1 = float(input())
n2 = int(input())

print(round(n1,n2))
