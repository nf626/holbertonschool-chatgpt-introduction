#!/usr/bin/python3
"""Documentation - Python Factorial"""
import sys

def factorial(n):
    """factorial recursion n"""
    # factorial n
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    f = factorial(int(sys.argv[1]))
    print(f)
