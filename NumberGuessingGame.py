import random
import os

randomNumber = random.randint(1, 5)
userChances = 0
Easy = 10
Medium = 5
Hard = 3

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.")

print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)\n")

while True:
    try:
        difficultyInput = input("Enter your choice: ")
        match int(difficultyInput):
            case 1:
                userChances = Easy
            case 2:
                userChances = Medium
            case 3:
                userChances = Hard
        os.system('cls')
        break    
    except ValueError:
        print("Please enter numbers (1-3).")

while True:
    try:
        print("Number of Chances: " + str(userChances))        
        userInput = input("Guess the number (1-5) \n")
        userInput = int(userInput)
        if userInput == randomNumber:            
            print("Congratulations! You guessed the correct number in "+ str(userChances) +" attempts.")
            break
        else:
            if userInput > randomNumber:
                print("Incorrect! The number is less than " +str(userInput)+ ".")
            else:
                print("Incorrect! The number is greater than " +str(userInput)+ ".")            
            userChances -= 1
            if userChances <= 0:
              print("Game Over!")
              break
    except ValueError:
        print("Please enter a number.")



