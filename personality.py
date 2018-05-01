#Personality.py

# Get the mode of interaction from the user
# Params: none
# Returns: an integer indicating one of reward, punish, joke, or threaten
def getInteraction():
    print("1. Reward")
    print("2. Punish")
    print("3. Threaten")
    print("4. Joke")
    print("5. Quit")
    choice = input("Which option would you like to choose?(Pick a number)" )
    return int(choice) # return a corresponding integer

# Based on a given emotion and action, determine the next emotional state
# Params:
# personality - a current emotion
# choice - a user interaction
# Returns: an emotion
def lookupEmotion(personality, choice):
    # JA: This could be done simpler with a 2-dimensional array
    if choice == 1:
        #Happy and surprised plus 1
        personality[0].append(personality[0][len(personality[0])-1]+1) #Happy
        personality[5].append(personality[5][len(personality[5])-1]+1) #Surprised
        #Anger, Disgust, Fear, Sad minus 1
        personality[1].append(personality[1][len(personality[1])-1]-1) #Anger
        personality[2].append(personality[2][len(personality[2])-1]-1) #Disgust
        personality[3].append(personality[3][len(personality[3])-1]-1) #Fear
        personality[4].append(personality[4][len(personality[4])-1]-1) #Sad
    elif choice == 2:
        #Anger and Fear plus 1
        personality[3].append(personality[3][len(personality[3])-1]+1) #Fear
        personality[1].append(personality[1][len(personality[1])-1]+1) #Anger
        #Disgust, sad, happy and suprised plus one
        personality[0].append(personality[0][len(personality[0])-1]-1) #Happy
        personality[5].append(personality[5][len(personality[5])-1]-1) #Surprise
        personality[2].append(personality[2][len(personality[2])-1]-1) #Disgust
        personality[5].append(personality[4][len(personality[4])-1]-1) #Sad
    elif choice == 3:
        #Fear and Disgust plus 1
        personality[2].append(personality[2][len(personality[2])-1]+1) #Disgust
        personality[3].append(personality[3][len(personality[3])-1]+1) #Fear
        #Anger, sad, happy, suprised
        personality[1].append(personality[1][len(personality[1])-1]-1) #Anger
        personality[4].append(personality[4][len(personality[4])-1]-1) #Sad
        personality[0].append(personality[0][len(personality[0])-1]-1) #Happy
        personality[5].append(personality[5][len(personality[5])-1]-1) #Surprised
    elif choice == 4:
        #Happy and suprisded plus one
        personality[0].append(personality[0][len(personality[0])-1]+1) #Happy
        personality[5].append(personality[5][len(personality[5])-1]+1) #Surprised
        #Anger, disgust, sad, fear
        personality[1].append(personality[1][len(personality[1])-1]-1) #Anger
        personality[2].append(personality[2][len(personality[2])-1]-1) #Disgust
        personality[4].append(personality[3][len(personality[3])-1]-1) #Fear
        personality[5].append(personality[4][len(personality[4])-1]-1) #Sad
    else:
        return 5
    currentEmotion = 0
    maxNum = -9999
    for i in range(0, len(personality)):
        if personality[i][len(personality[i])-1] > maxNum:
            currentEmotion = i
            maxNum = personality[i][len(personality[i])-1]
    return currentEmotion # return an integer corresponding to an emotion

#Print out an introduction
#Give the options to the User
print("Welcome to the artificial personality")
personality = [[0], [0], [0], [0], [0] ,[0]]
while True:
    choice = getInteraction()#Number of corresponding interaction
    if choice == 5:
        break
    else:
        currentEmotion = lookupEmotion(personality, choice)
        if currentEmotion == 0:
            print("I am happy!")
        elif currentEmotion ==1:
            print("What a suprise")
        elif currentEmotion ==2:
            print("Ew gross!")
        elif currentEmotion ==3:
            print("Yikes! That's scary")
        elif currentEmotion ==4:
            print("I'm feeling pretty sad today.")
print("Thanks for playing!")

