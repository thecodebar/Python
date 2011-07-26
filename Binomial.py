#! usr/bin/python

# All the Binomial related functions by Hector

import math as m

def binomial_coefficient(n, k):
    """
    Returns the binomial cofficiend(n, k) for positive 'n' and 'k'.
    It generaltes fast binomial coefficeint with the following formula

        C(n, k) = prod of{ (n - (k -i))/i } for i = 1 to k
    """
    if k > n - k: # take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - i)
        c = c / (i + 1)
    return c


def binomial_coefficient_app(n, k):
    """
    Returns the approximate Binomial coefficient of large 'n' and 'k'
    Using the following formula - 

    T == Gamma function
    
        C(n, k) = exp( ln(T(n + 1)) - ln(T(k+1)) - ln(T(n - k + 1)) )

    And ln(T(z)) can be calculated as - 
        ln(T(z)) = (z - 1/2) * ln(z) - z + ln(2 * pi)/2 
    """
    if c < 10000:
        return binomial_coefficient(n, k)

    ln_T_n1 = (n + 1/2.) * m.log(n + 1) - (n + 1) + m.log(2 * m.pi)/2.
    ln_T_k1 = (k + 1/2.) * m.log(k + 1) - (k + 1) + m.log(2 * m.pi)/2.
    ln_T_nk1 = ( n - k + 1/2.) * m.log( n - k + 1)  - (n - k + 1) + m.log(2 * m.pi)/2.

    pw = ln_T_n1 - ln_T_k1 - ln_T_nk1 
    if  pw < 700:
        return m.exp(pw)
    else:
        return "exp(%d)"%pw
