### Functions from functions.py were used and the nextGuess was written by me. 
import random

# Import the functions from the functions.py file
from functions import *

# Function to actually start playing the game for the AI algorithm
# This function was rewritten from the function playGame, to fit the special needs of the AI algorithm
def playAI():
    possibleCodes = createPossibleCodes(COLORS, CODELENGTH)
    secret_code = random.choice(possibleCodes)
    print("De computer heeft een code gegenereerd!")
    guesses = []
    for i in range(MAXGUESSES):
        print(f"Gok #{i+1}:")
        guess = input("Voer een code in: ")
        guesses.append(guess)
        score = evaluateGuess(guess, secret_code, CODELENGTH)
        print(score)
        if score[0] == CODELENGTH:
            print("Je hebt de code geraden!", '\n')
            break
    else:
        print("Je hebt verloren!")
        print(f"De geheime code was: {secret_code}", '\n')

# Function to allow the computer to generate a code and the player to guess it
if __name__ == "__main__":
    playAI()
