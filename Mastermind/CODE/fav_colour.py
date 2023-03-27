### My algorithm uses the same functions as the other algorithms, but it uses a different next_guess function,
### it takes into account what the favorite colour of the guesses is and uses that to make a first guess.
import itertools

# import the functions from the functions.py file
from functions import *


# In this function the computer will try to guess the code based on the favorite color of the player.
# if the favorite color is in the secret code, the computer will try to guess that color first.
# if the favorite color is not in the secret code, the computer will try to guess a code that contains the favorite color.
def nextGuess(possibleCodes, pastGuesses, favoriteColor):
    if len(pastGuesses) == 0:
        return favoriteColor * len(possibleCodes[0])
    codeLength = len(pastGuesses[0])
    if len(possibleCodes) == 1:
        return possibleCodes[0]
    scores = {}
    for code in possibleCodes:
        scores[code] = {}
        for score in itertools.product(range(codeLength + 1), repeat=2):
            scores[code][score] = len(removeImpossibleCodes(possibleCodes, code, score))
    bestCode = max(scores, key=lambda x: sum(scores[x].values()))
    if favoriteColor in bestCode:
        return bestCode
    else:
        for code in possibleCodes:
            if favoriteColor in code:
                return code
    return bestCode

if __name__ == "__main__":
    playFav(nextGuess)
