import random

# import the functions from the functions.py file
from functions import *


def nextGuess(possibleCodes):
    # Kies de volgende gok uit de lijst van mogelijke combinaties
    # Random guess
    nextGuess = random.choice(possibleCodes)
    return nextGuess

if __name__ == "__main__":
    playGame(nextGuess)
    