#!/usr/bin/python3
"""Minimum operations calculation using Copy All and Paste."""


def minOperations(n):
    """Return the minimum number of operations to get n H characters.

    If n is impossible or invalid, return 0.
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
