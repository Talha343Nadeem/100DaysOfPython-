import random
from art import  logo
print(logo)
numberToGuess = random.randint(1,100)
# print(numberToGuess)
print("Welcome to Talha's Number guessing game")
print("I have Chosen a number betweeen 1 and 100")
modeSelect = input("Choose the Difficulty easy or hard: ")
# if modeSelect == "hard":


# if modeSelect == "easy":
def Game():
    # guessRemaning = -1
    if modeSelect == "hard":
        guessRemaining = 5

    elif modeSelect == "easy":

        guessRemaining = 10
    # print(f"You have {guessRemaining} attempts to guess the number")
    #
    #
    guess = ""
    while guess != numberToGuess and guessRemaining != 0:
        print(f"You have {guessRemaining} attempts to guess the number")

        guess = input("Make a Guess :")

        try:
            guess = int(guess)
        except:
            print('guess Again')
            guessRemaining -=1
            continue


        if guess == numberToGuess:
            print("great success")
        elif guess > numberToGuess:
            print("too high")
            guessRemaining -= 1
        elif guess < numberToGuess:

           guessRemaining -= 1
           print("too low")
    if guessRemaining == 0:
        print("you ran out of guesses lmao ;( ")

Game()


