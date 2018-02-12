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
