import itertools

COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']
CODELENGTH = 4
MAXGUESSES = 10

# Creates a list of all possible codes
# Function was rewritten from the function createAllCodes, that was proivided in the powerpoint presentation
def createPossibleCodes(colors, numberOfPositions: int):
    possibleCodes = []
    for code in itertools.product(colors, repeat=numberOfPositions):
        possibleCodes.append(''.join(code))
    return possibleCodes   

# Function to evaluate the guess
# Function was written by ChatGPT and was alterted to fit my needs
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
# Source: https://github.com/LinaBlijlevenHU/StructuredProgramming2023
def removeImpossibleCodes(possibleCodes, guess, score):
    newPossibleCodes = []
    for code in possibleCodes:
        if evaluateGuess(code, guess, len(guess)) == score:
            newPossibleCodes.append(code)
    return newPossibleCodes

# Function to actually start playing the game
# This function was written by me with help of ChatGPT and my own knowing.
def playGame(nextGuess):  
    possibleCodes = createPossibleCodes(COLORS, CODELENGTH)
    secret_code = input("Think of a secret code: ")
    if len(secret_code) != CODELENGTH:
        print("That's not a valid code!")
        playGame(nextGuess)
    if not all(char in COLORS for char in secret_code):
        print("That's not a valid code!")
        playGame(nextGuess)
    print("Let the computer do it's magic!")
    print(f"The secret code is: {secret_code}")
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
            print("The computer has won!", '\n')
            break
        if possibleCodes == []:
            print("The computer has lost!", '\n')
            break
    else:
        print("The computer has lost!")
        print(f"The secret code was: {secret_code}")
    return guesses

# Function to actually start playing the game for the favorite color algorithm
# This function was rewritten from the function playGame, to fit the special needs of the favorite color algorithm
def playFav(nextGuess):
    possibleCodes = createPossibleCodes(COLORS, CODELENGTH)
    favorite_color = input("What is your favorite colour? ")
    if favorite_color not in COLORS:
        print("That's not a valid code!")
        playFav()
    if len(favorite_color) != CODELENGTH:
        print("That's not a valid code!")
        playFav()
    secret_code = input("Think of a secret code (RGBY): ")
    print("Let the computer do it's magic!")
    print(f"The secret code is: {secret_code}")
    guesses = []
    for i in range(MAXGUESSES):
        print(f"Guess #{i+1}:")
        guess = nextGuess(possibleCodes, guesses, favorite_color)
        guesses.append(guess)
        print(guess)
        score = evaluateGuess(guess, secret_code, CODELENGTH)
        print(score)
        possibleCodes = removeImpossibleCodes(possibleCodes, guess, score)
        print(f"Possible combinations: {len(possibleCodes)}")
        if score[0] == CODELENGTH:
            print("The computer has won!", '\n')
            break
    else:
        print("The computer has lost!")
        print(f"The secret code was: {secret_code}", '\n')
