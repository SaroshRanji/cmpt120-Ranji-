#pi.py
#Approximates the value of pi
import math

def pi():
    n = int(input("Enter the number of terms to use for the calculation: "))
    sign = 1
    pi = 0
    for i in range (n):
        pi = pi + (4/i * sign)
        sign = sign * -1

    print("The estimate of pi is ", pi)
    print("The error of the estimate is ", math.fabs(pi - math.pi))

pi()
#Fibonacci
# JA: Where is pi?

def fib(n):
    print("This is a way to show the fibonacci sequence.")
    n = eval(input("Input number to calculate the Fibonacci"))
    a,b = 1,1
 for i in range(n):
     print (a)
     #c = a + b
     #a = b
     #b = c
     a,b = b,a+b
fib()
