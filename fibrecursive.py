## Fibonacci numbers (iterative process) solution by Hector


#! usr/bin/python

def fib(n, p):
    if n<=1:
        return n
    else:
        return (fib(n-1,p)+fib(n-2,p))%p


def main(): # Unlike CPP main doesn't have any special meaning in python
    p = 1000000007
    while True:
        n = input('Pls enter the number \n')
        print fib(n,p)

main()
