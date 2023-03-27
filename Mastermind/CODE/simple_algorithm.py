#import random package
import random

# import the functions from the functions.py file
from functions import *

# Kies de volgende gok uit de lijst van mogelijke combinaties
# Random guess
def nextGuess(possibleCodes):
    nextGuess = random.choice(possibleCodes)
    return nextGuess

if __name__ == "__main__":
    playGame(nextGuess)
    
