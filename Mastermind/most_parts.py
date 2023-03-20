### This file contains the Most-Parts algorithm which was written by ChatGPT. The other code was copied from the previous file and altered by me to fit. ###

import random
import itertools

#import the functions from the functions.py file
from functions import *

def nextGuess(possibleCodes):
    # Choose the next guess from the list of possible combinations
    # Most-Parts algorithm
    bestGuess = None
    maxEliminated = -1
    for guess in possibleCodes:
        eliminatedCounts = {}
        for code in possibleCodes:
            score = evaluateGuess(guess, code, len(guess))
            eliminatedCounts.setdefault(tuple(score), set()).add(code)
        numEliminated = sum(len(codes) for codes in eliminatedCounts.values())
        if numEliminated > maxEliminated:
            bestGuess = guess
            maxEliminated = numEliminated
    return bestGuess    

playGame(nextGuess)