import math
import sys


def my_name():
    print("*******************")
    print("*     My name     *")
    print("*******************")


def israel_flag():
    pass


def stars_phrase():
    phrase = input("type a phrase")
    start_count = int(input("How many starts?"))
    star = "*"
    print((star * start_count) + phrase + (star * start_count))


def even_nums():
    num_of_even = 0
    for i in range(0, 4):
        n = int(input("n" + str(i) + "?"))
        num_of_even += n % 2
    print(num_of_even)


def sum_of_digits():
    num = int(input("num?"))
    sum = 0
    while num != 0:
        sum += num % 10
        num = int(num / 10)
    print(sum)


def line_equation():
    print("A(x1; y1):")
    x1 = int(input("x1="))
    y1 = int(input("y1="))
    print("B(x2; y2):")
    x2 = int(input("x2="))
    y2 = int(input("y2="))

    m = (y1 - y2) / (x1 - x2)
    b = -x1 * m + y1
    print("Equation:")
    print("y = ", m, "*x + ", b, )


if __name__ == '__main__':
    # my_name()
    # print()
    # stars_phrase()
    # even_nums()
    # sum_of_digits()
    line_equation()
