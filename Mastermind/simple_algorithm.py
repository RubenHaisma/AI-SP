### The following functions where copied from the powerpoint presentation in the assignment: createPossibleCodes, next_guess and evaluate. The other parts where alter or written by myself.###

import random
import itertools

def createPossibleCodes(colors, numberOfPositions: int):
    # Creeert een lijst van alle mogelijke oplossingen op basis van een lijst met colors en het aantal posities
    possibleCodes = []
    for code in itertools.product(colors, repeat=numberOfPositions):
        possibleCodes.append(''.join(code))
    return possibleCodes
    
def next_guess(possibleCodes):
    # Kies de volgende gok uit de lijst van mogelijke combinaties
    # Random guess
    nextGuess = random.choice(possibleCodes)
    return nextGuess    

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
       secretCopy.replace(secret[position], '', 1)
   for i in range(codeLength):
       if i not in used:
           if guess[i] in secretCopy:
               score[1] += 1
               secretCopy.replace(guess[i], '', 1)
   return score

### This function was rewritten from the function reduce, that was proivided in the powerpoint presentation ###

def removeImpossibleCodes(possibleCodes, guess, score):  # remove all codes that are not possible
    for code in possibleCodes:
        if evaluate(code, guess, len(code)) != score:
            possibleCodes.remove(code)
    return possibleCodes

def play_game_0():  # Function to actually start playing the game
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
        if score[0] == code_length:
            print("De computer heeft gewonnen!")
            break
    else:
        print("De computer heeft verloren!")
        print(f"De geheime code was: {secret_code}")

if __name__ == "__main__":
    play_game_0()
