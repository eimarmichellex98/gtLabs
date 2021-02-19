"""Verifying the Collatz conjecture"""

# Eimar Michelle Quinn
# 19/02/2021

def f(n):
    # if n is even
    if n % 2 == 0:
        return n // 2 # double // means integer division
                # single / means floating point division
    # if n is odd
    elif n % 2 == 1:
        return (3 * n) + 1
    else:
        return None


def collatz(n):
    so_far = [n]
    # loop until n is 1
    while n !=1:
        #print(n)
        n =f(n)
        so_far.append(n)
    #return True
    return so_far

#print(collatz(10))
print(collatz(27))