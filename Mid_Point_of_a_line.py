'''Mid point of a line
Medium
Write a Python program to calculate midpoints of a line.
Input:
2
2
4
4
Output:
Midpoint: 3.0 3.0     '''

import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

mid1 = (x1+x2)/2
mid2 = (y1+y2)/2

print("Midpoint:",mid1,mid2)
