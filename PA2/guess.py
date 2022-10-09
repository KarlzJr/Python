# assignment: programming assignment 2
# author: Alejandra Sicairos
# date: 10/31/2020
# file: guess.py is an interactive game that asks the user to guess a number from 1 to 10
# input: only integers from 1 to 10
# output: interactive messages

from random import randint

#initialize the while loop
done = False
counter = 0
 
print("Play a game: Guess My Number!")

while not done:
    #gets random number for the user to guess
    mynumber = 3 #randint(1,10)
    print("You have three attempts to guess my number")
    n = 0
    guess = int(input("Please enter a number from 1 to 10: "))
    for k in range(2):
        if guess == mynumber:
            break
            print(f"You guessed right. My number is {mynumber}. Congratulations you won!")
        elif guess > mynumber:
            print("You guessed wrong. Your number is bigger than mine")
            guess = int(input("Guess again. Please enter a number: "))
        else:
            print("You guessed wrong. Your number is smaller than mine")
            guess = int(input("Guess again. Please enter a number: "))
            
    if guess != mynumber:
        print(f"Sorry you lost. My number is {mynumber}")
    else:
        print(f"You guessed right. My number is {mynumber}. Congratulations you won!")       

    playAgain = input(str("Would you like to play again [Y/N]? "))
    if playAgain == "n":
        done = True
      
print("Goodbye!")
        

            
