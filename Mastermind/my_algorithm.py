### 

import random
import itertools

def createPossibleCodes(colors, numberOfPositions: int):
    # Creeert een lijst van alle mogelijke oplossingen op basis van een lijst met colors en het aantal posities
    possibleCodes = []
    for code in itertools.product(colors, repeat=numberOfPositions):
        possibleCodes.append(''.join(code))
    return possibleCodes
    
def evaluate(guess, secret, codeLength):
    score = [0, 0]
    used = []
    # The black pins
    for position in range(codeLength):
        if guess[position] == secret[position]:
            score[0] += 1
            used.append(position)
    # The white pins
    secretCopy = list(secret)
    for position in used:
        secretCopy[position] = None
    for i in range(codeLength):
        if i not in used and guess[i] in secretCopy:
            score[1] += 1
            secretCopy[secretCopy.index(guess[i])] = None
    return score

def removeImpossibleCodes(possibleCodes, guess, score):
    # remove all codes that are not possible
    return [code for code in possibleCodes if evaluate(code, guess, len(code)) == score]


def next_guess(possibleCodes, pastGuesses):
    if len(pastGuesses) == 0:
        return random.choice(possibleCodes)
    codeLength = len(pastGuesses[0])
    if len(possibleCodes) == 1:
        return possibleCodes[0]
    scores = {}
    for code in possibleCodes:
        scores[code] = {}
        for score in itertools.product(range(codeLength + 1), repeat=2):
            scores[code][score] = len(removeImpossibleCodes(possibleCodes, code, score))
    bestCode = max(scores, key=lambda x: sum(scores[x].values()))
    return bestCode

def play_game_2():  # Function to actually start playing the game
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
        guess = next_guess(possibleCodes, guesses)
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
    play_game_2()


