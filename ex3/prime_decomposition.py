"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 3
Program: prime_decomposition.py
"""


def decompose(n):
    decomposed_primes = []
    while n % 2 == 0:  # Decompose number by 2
        decomposed_primes.append(2)
        n //= 2

    for i in range(3, n + 1, 2):
        # Decompose number by all prime numbers starting from 3
        # (this will not include none prime numbers as we are starting to check from the bottom up)
        while n % i == 0:
            decomposed_primes.append(i)
            n //= i
    return decomposed_primes


def print_decomposition(n):
    primes_to_print = decompose(n)
    prev_prime = primes_to_print[0]
    text_to_print = str(primes_to_print[0])
    current_power_count = 1
    primes_to_print.pop(0)

    for i in primes_to_print:
        if i == prev_prime:
            current_power_count += 1
        else:  # We are now looking at a different prime number, lets save last the current_power_count
            if current_power_count != 1:  # If the power it not 1, lets add the power to the text
                text_to_print += "^" + str(current_power_count)
                current_power_count = 1
            text_to_print += "*" + str(i)  # Next prime number added to text
        prev_prime = i

    if current_power_count != 1:
        text_to_print += "^" + str(current_power_count)
    print(n, "=", text_to_print)


def main():
    while True:
        user_input = input("Please enter an integer greater than 1: ")

        if user_input == "quit":
            break

        try:
            n = int(user_input)
            if n < 2:
                # We cannot accept a number less then 2,
                # lets raise an exception so we can catch and print a msg accordingly
                raise ValueError
        except ValueError:
            print("Illegal input. Try again")
            continue

        print_decomposition(n)

    print("program ends, good bye.")


if __name__ == '__main__':
    main()
