"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 5
Program: check_primes.py
"""

import random


def is_probably_prime(n):
    """
    Calculating whether "n" has a high chance of being a prime number
    :return: True if "n" calculated to be a prime number, else False
    """
    for i in range(20):
        if not is_suspected_prime(n):
            return False
    return True


def is_suspected_prime(n):
    """
    Checking if "n" is a suspected prime number using "Fermat primality test"
    :return: True if "n" found to be a suspected prime, else False
    """
    a = random.randint(2, n - 1)
    d = modular_power(a, (n - 1) // 2, n)
    return d == 1 or d == n - 1


def modular_power(a, b, n):
    """ computes a**b (mod n) using iterated squaring
    assumes b is a nonnegative integer """
    l = []
    while b > 0:
        if b % 2 == 1:
            l = [1] + l
        else:
            l = [0] + l
        b //= 2
    result = 1
    for k in l:
        result = (result ** 2) % n
        if k == 1:
            result = (result * a) % n
    return result


def compute_result(input_file_name, output_file_name):
    """
    Reads list of numbers from "input_file_name" file and writes for each number whether is he a prime or not prime
    using "is_probably_prime".
    Result will be saved into "output_file_name" file, even numbers won't be checked
    """
    with open(input_file_name, "r") as file_input:
        with open(output_file_name, "w") as output_file:
            for n in file_input.readlines():
                n = int(n)
                if n % 2 == 0 or not is_probably_prime(n):
                    output_file.write(f"{n} is not prime\n")
                    continue
                output_file.write(f"{n} is prime\n")


def main():
    """
    Reads numbers from "input_ex1" file into "output_ex1.txt" file using compute_result
    """
    compute_result("input_ex1.txt", "output_ex1.txt")


if __name__ == '__main__':
    main()
