### This file contains the Most-Parts algorithm which was written by ChatGPT. The other code was copied from the previous file and altered by me to fit. ###

import random
import itertools

#import the functions from the functions.py file
from functions import *

# Most-Parts algorithm
# This algorithm is based on the idea that the guess with the most parts is the best guess.
def nextGuess(possibleCodes):
    bestGuess = None
    minMaxRemaining = len(possibleCodes)
    for guess in possibleCodes:
        remainingCounts = {}
        for code in possibleCodes:
            score = evaluateGuess(guess, code, len(guess))
            remainingCounts.setdefault(tuple(score), set()).add(code)
        maxRemaining = max(len(codes) for codes in remainingCounts.values())
        if maxRemaining < minMaxRemaining:
            bestGuess = guess
            minMaxRemaining = maxRemaining
    return bestGuess




if __name__ == "__main__":
    playGame(nextGuess)
