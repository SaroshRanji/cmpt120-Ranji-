# convert.py
def main():
        celsius = float(input("What is the Celsius temperature?"))
        farenheit = 9 / 5 * celsius + 32
        print("The temperature is", farenheit, "degrees farenheit.")
        if farenheit > 104:
            print ("It's really hot out there, be careful!")
        if farenheit < 30:
            print ("Brr. Be sure to dress warmly!")
main()
