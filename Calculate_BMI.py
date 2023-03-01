'''
Write a Python program to calculate body mass index
Input:
6
65
Output:
1.81               '''

import math

height = float(input())
weight = float(input())

BMI = weight/(height**2)

print(round(BMI,2))
