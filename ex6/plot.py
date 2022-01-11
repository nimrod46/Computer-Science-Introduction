"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 6
Program: plot.py
"""

from math import *
import matplotlib.pyplot as plt


def plot(funcs, a, b, title="", legend='', show_grid=False, h=0.001):
    """
    Plots all functions in "funcs" to the same plot view
    """
    max_x = 0
    min_x = 100000
    max_y = 0
    min_y = 100000
    for f in funcs:
        x_vals = [a + i * h for i in range(int((b - a) / h))]
        y_vals = [f(x) for x in x_vals]
        plt.plot(x_vals, y_vals, color='red')
        max_x = max(max(x_vals), max_x)
        max_y = max(max(y_vals), max_y)
        min_y = min(min(y_vals), min_y)
        min_x = min(min(x_vals), min_x)
    if legend != '':
        plt.legend([legend])
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis([min_x, max_x, min_y - 0.3, max_y + 0.3])
    plt.grid(show_grid)
    plt.show()


def main():
    """
    Reads all functions from "functions.txt" file and plot range.
    Calling "plot" with the params accordingly
    """
    with open("functions.txt", "r") as funcs_file:
        data = funcs_file.readlines()
    a, b = data[-1].split()[0], data[-1].split()[1]
    data.pop()
    plot(map(lambda f: eval(f"lambda x: {f}"), data), float(a), float(b))


if __name__ == '__main__':
    main()
