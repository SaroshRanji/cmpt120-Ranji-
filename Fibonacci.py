#Fibonacci

def fib(): #JA
    print("This is a way to show the fibonacci sequence.")
    n = eval(input("Input number to calculate the Fibonacci"))
    a,b = 1,1
    for i in range(n): #JA
        print (a)
        #c = a + b
        #a = b
        #b = c
        a,b = b,a+b
fib()
