# Eimar Michelle Quinn
# Python Basics
# 18/02/2021

# number to calculate factorial of
# n = 20
def factorial(n):
    """Number to calculate factorial of."""
    # copy value
    m = n
    # running total - eventually factorial
    total = 1

    # while loop to do multiplications
    while m > 0:
        total = total * m
        m = m - 1
    # return the answer
    return total

# print(total)

# test function def
n = 20
# calculate the factorial of n
 print(f"The factorial of {n} is {factorial{n}}.") # not working :/

