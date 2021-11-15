def multi_table():
    num = int(input("range: ")) + 1
    for i in range(1, num):
        for j in range(1, num):
            print(i * j, end=" ")
        print()


multi_table()
