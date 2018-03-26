# CMPT 120 - Lab #6
# Sarosh Ranji
# 19-03-2018
###

# There is a single commit

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def doLoop():
    while True:
        while True:
            cmd = input("What computation do you want to perform? ").lower()
            if cmd == "add" or cmd == "sub" or cmd == "mult" or cmd == "div" or cmd == "quit":
                break
            else:
                print(cmd,"is not a valid command.")
            if cmd == quit:
                break
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if cmd == "add":
            result = num1 + num2
        elif cmd == "sub":
            result = num1 - num2
        elif cmd == "mult":
            result = num1 * num2
        elif cmd == "div":
            result = num1 // num2
        elif cmd == "quit": # You should put this at the beginning so you don't ask for the numbers
            result = print("Please come back again soon!")
            break
        print("The result is " + str(result) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()

main()
