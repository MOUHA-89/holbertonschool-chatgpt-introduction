#!/usr/bin/python3
import sys
# Function description:
# This function calculates the factorial of a given integer n using recursion.

# Parameters:
# n (int): The integer for which the factorial is to be calculated. The function expects n to be a non-negative integer.

# Returns:
# int: The factorial of the input integer n. If n is 0, the function returns 1 (as 0! = 1).
# For any positive integer n, the function returns the product of all integers from 1 to n.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
