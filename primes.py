"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f"number_of_primes={number_of_primes} should have been positive number")
    list = []
    n = 2
    while len(list) != number_of_primes:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                break
        else:
            list.append(n)
        n += 1

    return list

