#Fibonacci

def fib():
    n = int(input("Enter the fibonacci term to find: "))
    x, y = 1, 1
    for i in range (1, n-1):
        x, y = y, x+y

    print("The ",n,"term is ", y)

def fib2():
    n = int(input("Enter the fibonacci term to find: "))
    print("The ",n,"term is ", y)

def fibRec(n):
    if (n ==1):
        return 1
    if (n ==2):
        return 1
    return fibRec(n - 1) + fibRec(n - 2)

fib2()
