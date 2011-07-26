#! usr/bin/python

# Fibonacci and related functions by Hector
import math as m

def fibonacci(n):
    """
    fibonacci(n) returns the 'n'th Fibonacci number.
    It is calculated using the 
    """
    a = 0
    b = 1
    for i in range(0, n):
        b = a + b
        a = b - a
    return a


def fibonacci_app(n):
    """
    For large Fibonacci numbers ( for 100th  and above), as returns the Fibonacci number approximately close to that index using direct formula.
    """
    golden_ratio = 1.6180339887498948
    if n < 100:
        return fibonacci(n)
    else:
        f_100 = 354224848179261915075 # It is 100th Fibonacci number
        return f_100*golden_ratio**(n-100)

def nearest_int(f):
    """
    Returns the nearest integer for the given float number.
    Used in fibonacci_fast
    """
    if f - m.floor(f) < 1/2:
        return int(f)
    else:
        return int(f) + 1

def fibonacci_list(m):
    """
    Returns the list of first m Fibonacci numbers
    """
    F = [ 1 for i in range(0,m)]
    for i in range(2, m):
        F[i] =  F[i-1] + F[i-2]
    return F


def fibonacci_below(z):
    """
    Returns the list of Fibonacci numbers less than or equal to z
    Uses the fact that F(n) is the closest integer to (phi)**n / 5 to determine n.
    """
    golden_ratio = 1.618033
    n = int(m.floor(m.log(z*m.sqrt(5) + .5)/m.log(golden_ratio)))
    return fibonacci_list(n)

def is_perfect_sq(N):
    """
    Returns True if N is the perfect square. 

    Used in is_fibonacci function.
    """
    n = int(m.sqrt(N))
    if N == n**2:
        return True
    else:
        return False

def is_fibonacci(N):
    """
    This function returns whether the given number is Fibonacci or not.

    I. Gessel gave a simple test in 1972, N is a Fibonacci number if and only if 5**N*2 + 4 or 5*N**2 - 4 is a square number.
    """
    if is_perfect_sq(5 * N**2 + 4) or is_perfect_sq(5 * N**2 - 4):
        return True 
    else:
        return False
