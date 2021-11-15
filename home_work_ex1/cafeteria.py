"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 3
Program: cafeteria.py
"""


def check_cash(cash):
    if cash % 50 == 0 and cash >= 50:
        print("don’t you have smaller cash?")
    elif cash < 50 and cash % 10 == 0:
        print("ok")
    elif cash <= 0:
        print("no service")
    else:
        print("Total: ", cash)


def main():
    user_cash = int(input("Enter amount: "))
    check_cash(user_cash)


main()
