"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 2
Program: stats.py
"""

import math


def three_of_max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    return num3


def three_of_sd(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    sd = math.sqrt(((num1 - avg)**2 + (num2 - avg)**2 + (num3 - avg)**2) / 3)
    return sd


def main():
    num1 = int(input("Enter first numbers: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    print("max", three_of_max(num1, num2, num3))
    print("Standard deviation", three_of_sd(num1, num2, num3))
    pass


main()
