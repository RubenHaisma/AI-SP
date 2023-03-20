### This file contains the Most-Parts algorithm which was written by ChatGPT. The other code was copied from the previous file and altered by me to fit. ###

import random
import itertools

def createPossibleCodes(colors, numberOfPositions: int):
    # Create a list of all possible solutions based on a list of colors and the number of positions
    possibleCodes = []
    for code in itertools.product(colors, repeat=numberOfPositions):
        possibleCodes.append(''.join(code))
    return possibleCodes
    
def next_guess(possibleCodes):
    # Choose the next guess from the list of possible combinations
    # Most-Parts algorithm
    bestGuess = None
    maxEliminated = -1
    for guess in possibleCodes:
        eliminatedCounts = {}
        for code in possibleCodes:
            score = evaluate(guess, code, len(guess))
            eliminatedCounts.setdefault(tuple(score), set()).add(code)
        numEliminated = sum(len(codes) for codes in eliminatedCounts.values())
        if numEliminated > maxEliminated:
            bestGuess = guess
            maxEliminated = numEliminated
    return bestGuess    

def evaluate(guess, secret, codeLength):
   score = [0,0]
   used = []
   # The black pins
   for position in range(codeLength):
        if guess[position] == secret[position]:
            score[0] += 1
            used.append(position)
   # The white pins
   secretCopy = secret[::]
   for position in used:
       secretCopy = secretCopy[:position] + ' ' + secretCopy[position+1:]
   for i in range(codeLength):
       if i not in used:
           if guess[i] in secretCopy:
               score[1] += 1
               secretCopy = secretCopy[:secretCopy.index(guess[i])] + ' ' + secretCopy[secretCopy.index(guess[i])+1:]
   return score

def removeImpossibleCodes(possibleCodes, guess, score):  # remove all codes that are not possible
    for code in possibleCodes:
        if evaluate(code, guess, len(code)) != score:
            possibleCodes.remove(code)
    return possibleCodes

def play_game_1():  # Function to actually start playing the game
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']
    code_length = 4
    max_guesses = 10
    possibleCodes = createPossibleCodes(colors, code_length)
    secret_code = input("Bedenk de geheime code: ")
    print("Laat de computer raden!")
    print(f"De geheime code is: {secret_code}")
    guesses = []
    for i in range(max_guesses):
        print(f"Gok #{i+1}:")
        guess = next_guess(possibleCodes)
        guesses.append(guess)
        print(guess)
        score = evaluate(guess, secret_code, code_length)
        print(score)
        possibleCodes = removeImpossibleCodes(possibleCodes, guess, score)
        print(f"Aantal mogelijke combinaties: {len(possibleCodes)}")
        if score[0] == code_length:
            print("De computer heeft gewonnen!")
            break
    else:
        print("De computer heeft verloren!")
        print(f"De geheime code was: {secret_code}")

if __name__ == '__main__':
    play_game_1()