import random
import itertools
from functions import playGame


def nextGuess(possibleCodes):
    # Kies de volgende gok uit de lijst van mogelijke combinaties
    # Random guess
    nextGuess = random.choice(possibleCodes)
    return nextGuess

playGame(nextGuess)