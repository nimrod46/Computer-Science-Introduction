"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 2
Program: triangle.py
"""


def print_triangle(height, dollars_count, spaces_count):
    current_dollar_count = 0
    current_spaces_count = 0
    for row in range(0, height - 1):
        print(" " * (height - row - 1), end="*")    # Row offset from left, includes the left "*"
        for column in range(0, row * 2 - 1):
            if current_dollar_count != dollars_count:
                current_dollar_count += 1
                print("$", end="")
            elif current_spaces_count != spaces_count:
                current_spaces_count += 1
                print(" ", end="")
            else:
                current_spaces_count = 0
                current_dollar_count = 1
                print("$", end="")
        if row != 0:
            print("*", end="")  # Right "*" (excludes the first row)
        print()
    print("*" * (height * 2 - 1))   # Last "*" row


def main():
    height = int(input("Enter height: "))
    dollars_count = int(input("Enter number of $: "))
    spaces_count = int(input("Enter number of spaces: "))
    print_triangle(height, dollars_count, spaces_count)


if __name__ == '__main__':
    main()
