"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 6
Program: intersection.py
"""

from math import *
from random import *


def func_diff(f, g):
    """
    :return: Lambda wrapping the diff between "f" and "g" funcs
    """
    return lambda x: (f(x) - g(x))


def diff(f):
    """
    :return: The derivative of f
    """
    h = 0.000001
    return lambda x: (f(x + h) - f(x)) / h


def read_input(file_name):
    """
    :return: Two funcs and range from file by "file_name"
    """
    with open(file_name) as input_file:
        lines = input_file.readlines()
    return eval("lambda x :" + lines[0]), eval("lambda x :" + lines[1]), float(lines[2].split()[0]), float(lines[2].
                                                                                                           split()[1])


def find_intersection(f, a, b, epsilon=10 ** (-4), n=100):
    """ finds an approximation to a root of
    f using the Newton Raphson method
    """
    deriv = diff(f)
    x0 = uniform(a, b)
    while abs(deriv(x0)) < epsilon:
        x0 = uniform(a, b)
    x = x0
    y = f(x)
    count = 1
    while abs(y) > epsilon and count <= n:
        count += 1
        y = f(x)
        x = x - y / deriv(x)
    if count > n:
        return None
    if a > x or b < x:
        return find_intersection(f, a, b)
    return x


def get_intersection_result(x, f):
    """
    :return: Formats intersection result
    """
    return f"intersection: ({x:.4f}, {f(x):.4f})"


def print_output(file_name):
    """
    :return: Prints result from "find_intersection", if func failed "no intersection" will be printed
    """
    f, g, a, b = read_input(file_name)
    try:
        x = find_intersection(func_diff(f, g), a, b)
    except:
        print("no intersection")
        return
    print(get_intersection_result(x, f))


def main():
    print_output("input.txt")


if __name__ == '__main__':
    main()
