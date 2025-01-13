#!/usr/bin/python3
"""Debugging - Python Factorial"""
import sys

def factorial(n):
    #factorial n
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

f = factorial(int(sys.argv[1]))
print(f)
