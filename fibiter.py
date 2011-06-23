#!usr/bin/python

# Function for Fibonacci by Hector

p = 1000000007
f0, f1 = 0, 1

while True:
    n = input("Enter the value of n \n")
    if n == 0:
        print "fib(0) = ", 0
        continue
    a = f0
    b = f1
    for i in range (2,n+1):
        b = a + b
        a = b - a
        b = b%p
        a = a%p
    print "fib(%d) = %d \n" %(n, b)
    break
