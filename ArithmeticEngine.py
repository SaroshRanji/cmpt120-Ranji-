# CMPT 120 - Lab #6
# Sarosh Ranji
# 19-03-2018
###
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
            if cmd == "add" or cmd == "sub" or cmd == "mult" or cmd == "div":
                break
            elif cmd == quit def showOutro
            else:
                print(cmd,"is not a valid command.")
             #   203 747 0144 jason
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
        elif cmd == "quit":
            break
        print("The result is " + str(result) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()

main()
