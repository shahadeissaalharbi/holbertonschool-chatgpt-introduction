#!/usr/bin/python3
import sys

def factorial(n):
    """
    Computes the factorial of a given number recursively.

    Parameters:
        n (int): The number to compute the factorial of. Must be >= 0.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
