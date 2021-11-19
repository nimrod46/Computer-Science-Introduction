import random

from ex3.prime_decomposition import *


def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        print(i)
        if n % i == 0:
            return False
    return True


def test_print_decompose(capfd):
    for i in range(100):
        n = random.randint(0, 9999)
        print_decomposition(n)
        out, err = capfd.readouterr()
        assert eval(out.replace(str(n), "", 1).replace(" = ", "").replace("^", "**")) == n


def test_decompose():
    for i in range(100):
        n = random.randint(0, 9999)
        primes = decompose(n)
        composed = 1
        for p in primes:
            assert is_prime(p)
            composed *= p
        assert composed == n
