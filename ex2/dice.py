"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 2
Program: dice.py
"""


import random


def generate_dice_data(throw_count):
    count_by_sum = {}
    for i in range(2, 12 + 1):
        count_by_sum.setdefault(i, 0)

    for i in range(0, throw_count):
        sum = random.randint(1, 6) + random.randint(1, 6)
        count_by_sum[sum] += 1
    return count_by_sum


def main():
    count_by_sum = generate_dice_data(int(input("Enter number of throws: ")))
    rows = max(count_by_sum.values())
    items = sorted(count_by_sum.items())  # Ensures the dicts is sorted and casting to iterable obj
    for i in range(0, rows):
        for (sum, throw_count) in items:
            print(" " * (len(str(sum)) - 1), end="")    # Offset for wide columns
            if i >= rows - throw_count:
                print("x", end=" ")
            else:
                print(" ", end=" ")
        print()

    for i in range(2, 12 + 1):
        print(i, end=" ")


if __name__ == '__main__':
    main()
