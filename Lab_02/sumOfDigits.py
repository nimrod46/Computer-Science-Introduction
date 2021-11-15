def sum_of_digits():
    num = int(input("num?"))
    sum = 0
    while num != 0:
        sum += num % 10
        num = int(num / 10)
    print(sum)


def main():
    pass


main()
