import math


def decompose(n):
    decomposed_primes = []
    while n % 2 == 0:  # Decompose number by 2
        decomposed_primes.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)), 2):
        # Decompose number by all prime numbers
        # (this will not include none prime numbers as we are first checking from the bottom up)
        while n % i == 0:
            decomposed_primes.append(i)
            n //= i

    if n > 2:  # Add the number we left with as it's a prime number
        decomposed_primes.append(n)
    return decomposed_primes


def print_decomposition(n):
    primes_to_print = decompose(n)
    prev_prime = primes_to_print[0]
    text = str(primes_to_print[0])
    current_power_count = 1
    primes_to_print.pop(0)

    for i in primes_to_print:
        if i == prev_prime:
            current_power_count += 1
        else:
            if current_power_count != 1:
                text += "^" + str(current_power_count)
                current_power_count = 1
            text += "*" + str(i)
        prev_prime = i

    if current_power_count != 1:
        text += "^" + str(current_power_count)
    print(n, "=", text)


def main():
    while True:
        user_input = input("Please enter an integer greater than 1: ")
        if user_input == "quit":
            break
        try:
            n = int(user_input)
            if n <= 1:
                raise ValueError
        except ValueError:
            print("Illegal input. Try again")
            continue
        print_decomposition(n)

    print("program ends, good bye.")


if __name__ == '__main__':
    main()
