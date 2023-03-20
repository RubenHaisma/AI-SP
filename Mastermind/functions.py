import random
import itertools

COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']
CODELENGTH = 4
MAXGUESSES = 10

# Creates a list of all possible codes
def createPossibleCodes(colors, numberOfPositions: int):
    possibleCodes = []
    for code in itertools.product(colors, repeat=numberOfPositions):
        possibleCodes.append(''.join(code))
    return possibleCodes   

# Function to evaluate the guess
def evaluateGuess(guess, secret, codeLength):
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

# Function to remove impossible codes
# This function was rewritten from the function reduce, that was proivided in the powerpoint presentation
def removeImpossibleCodes(possibleCodes, guess, score):
    newPossibleCodes = []
    for code in possibleCodes:
        if evaluateGuess(code, guess, len(guess)) == score:
            newPossibleCodes.append(code)
    return newPossibleCodes

# Function to actually start playing the game
# This function was written by me with help of stackoverflow. (Nothing was ctrl+c ctrl+v'ed)
def playGame(nextGuess):  
    possibleCodes = createPossibleCodes(COLORS, CODELENGTH)
    secret_code = input("Bedenk de geheime code: ")
    print("Laat de computer raden!")
    print(f"De geheime code is: {secret_code}")
    guesses = []
    for i in range(MAXGUESSES):
        print(f"Gok #{i+1}:")
        guess = nextGuess(possibleCodes)
        guesses.append(guess)
        print(guess)
        score = evaluateGuess(guess, secret_code, CODELENGTH)
        print(score)
        possibleCodes = removeImpossibleCodes(possibleCodes, guess, score)
        if score[0] == CODELENGTH:
            print("De computer heeft gewonnen!", '\n')
            break
        if possibleCodes == []:
            print("De computer heeft verloren!", '\n')
            break
    else:
        print("De computer heeft verloren!")
        print(f"De geheime code was: {secret_code}")
    return guesses

# Function to actually start playing the game for the favorite color algorithm
# This function was rewritten from the function playGame, to fit the special needs of the favorite color algorithm
def playFav(nextGuess):
    possibleCodes = createPossibleCodes(COLORS, CODELENGTH)
    favorite_color = input("Wat is je favoriete kleur? ")
    if favorite_color not in COLORS:
        print("Dat is geen geldige kleur!")
        playFav()
    secret_code = input("Bedenk de geheime code: ")
    print("Laat de computer raden!")
    print(f"De geheime code is: {secret_code}")
    guesses = []
    for i in range(MAXGUESSES):
        print(f"Gok #{i+1}:")
        guess = nextGuess(possibleCodes, guesses, favorite_color)
        guesses.append(guess)
        print(guess)
        score = evaluateGuess(guess, secret_code, CODELENGTH)
        print(score)
        possibleCodes = removeImpossibleCodes(possibleCodes, guess, score)
        print(f"Aantal mogelijke combinaties: {len(possibleCodes)}")
        if score[0] == CODELENGTH:
            print("De computer heeft gewonnen!", '\n')
            break
    else:
        print("De computer heeft verloren!")
        print(f"De geheime code was: {secret_code}", '\n')

