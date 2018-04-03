#quadratic.py

import math

def main():
    print("This program finds the real solutions to a quadratic\n")

#    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

       
            discRoot = math.sqrt(discrim)
            root1 = (-b + discRoot) / (2 * a)
            root2 = (-b + discRoot) / (2 * a)
            print("The solutions are:", root1, root2)
#        except ValueError:
#            print("\nNo real roots!")

            

main()
