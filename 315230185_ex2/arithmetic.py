"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 1
Program: arithmetic.py
"""


def arithmetic_find(lst):
    lists_of_arithmetics = []
    current_count = 0
    current_start_index = 0
    diff = 0

    for i in range(0, len(lst) - 1):
        if lst[i] - lst[i + 1] == diff:
            current_count += 1
        else:
            lists_of_arithmetics.append((current_start_index, current_count))
            current_start_index = i
            current_count = 0
            diff = lst[i] - lst[i + 1]
    lists_of_arithmetics.append((current_start_index, current_count))

    max_count = 0
    max_index = 0
    for (index, count) in lists_of_arithmetics:
        if max_count < count:
            max_index = index
            max_count = count

    return max_index


def main():
    numbers = list(map(int, input("Enter number, followed by a comma: ").replace(" ", "").split(",")))
    index = arithmetic_find(numbers)
    diff = numbers[index] - numbers[index + 1]
    last_num = numbers[index]
    print("Longest arithmetic sequence: ", end="")
    print(last_num, end="")
    for num in numbers[index+1:]:   # Printing the arithmetic separated by commas
        if last_num - num != diff:
            break
        print(end=",")
        print(num, end="")
        last_num = num


main()
