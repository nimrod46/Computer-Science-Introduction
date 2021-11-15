"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 1
Program: your_name.py
"""


def name_print(full_name):
    for c in full_name:
        if c == " ":
            print()
            continue
        print(c, end="")


def main():
    name = input("Enter your name: ")
    name_print(name)


main()
