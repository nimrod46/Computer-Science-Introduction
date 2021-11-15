"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 4
Program: quadratic.py
"""

import math


def quadratic(a, b, c):
    quadratic_root = b ** 2 - 4 * a * c
    if quadratic_root < 0:  # No solutions
        return None, None
    elif quadratic_root == 0:  # One solution
        return -b / 2 * a, None
    quadratic_result1 = (-b + math.sqrt(quadratic_root)) / (2 * a)
    quadratic_result2 = (-b - math.sqrt(quadratic_root)) / (2 * a)
    return quadratic_result1, quadratic_result2  # Two solutions


def main():
    a = int(input("Enter first parameter (a): "))
    b = int(input("Enter second parameter (b): "))
    c = int(input("Enter third parameter (c): "))
    first_result, second_result = quadratic(a, b, c)
    if first_result is None and second_result is None:
        print("No solution")
    elif first_result is None or second_result is None:
        print("One solution: ", first_result if first_result is not None else second_result)
    else:
        print("Two solutions: ", first_result, second_result)


main()
