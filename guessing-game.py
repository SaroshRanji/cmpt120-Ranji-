#Sarosh Ranji
#guessing-game.py
def main():
    animal = ("penguin")
    print ("I'm thinking of an animal")
    guess = input("Guess the animal") #prints text and lets user guess

    while True:
        if guess == animal:
            print("You guessed correctly!")
            break
        else:
            print("Incorrect.")
            guess = input("Would you like to guess again?")
main()