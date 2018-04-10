#Sarosh Ranji
#guessing-game.py
def main():
    y = ("yes")
    n = ("no")
    animal = ("penguin")
    print ("I'm thinking of an animal")
    guess = input("Guess the animal").lower()#prints text and lets user guess




    while True:
        if guess[:1] == "q":
            print("Goodbye")
            break
        elif guess == animal:
            print("You guessed correctly!")
            print("Do you like the animal? y or n")
            if y == input:
                print("Me too")
            elif n == input:
                print("Oh ok.") 
            break
        else:
            print("Incorrect.")
            guess = input("Would you like to guess again?")
main()
