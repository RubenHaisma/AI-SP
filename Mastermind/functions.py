import random
import itertools

COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']
CODELENGTH = 4
MAXGUESSES = 10

def createPossibleCodes(colors, numberOfPositions: int):
    # Creeert een lijst van alle mogelijke oplossingen op basis van een lijst met colors en het aantal posities
    possibleCodes = []
    for code in itertools.product(colors, repeat=numberOfPositions):
        possibleCodes.append(''.join(code))
    return possibleCodes   

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

# This function was rewritten from the function reduce, that was proivided in the powerpoint presentation
def removeImpossibleCodes(possibleCodes, guess, score):
    newPossibleCodes = []
    for code in possibleCodes:
        if evaluateGuess(code, guess, len(guess)) == score:
            newPossibleCodes.append(code)
    return newPossibleCodes


def playGame(nextGuess):  # Function to actually start playing the game
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
            print("De computer heeft gewonnen!")
            break
        if possibleCodes == []:
            print("De computer heeft verloren!")
            break
    else:
        print("De computer heeft verloren!")
        print(f"De geheime code was: {secret_code}")
    return guesses

def playFav(nextGuess):
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']
    code_length = 4
    max_guesses = 10
    possibleCodes = createPossibleCodes(colors, code_length)
    favorite_color = input("Wat is je favoriete kleur? ")
    if favorite_color not in colors:
        print("Dat is geen geldige kleur!")
        playFav()
    secret_code = input("Bedenk de geheime code: ")
    print("Laat de computer raden!")
    print(f"De geheime code is: {secret_code}")
    guesses = []
    for i in range(max_guesses):
        print(f"Gok #{i+1}:")
        guess = nextGuess(possibleCodes, guesses, favorite_color)
        guesses.append(guess)
        print(guess)
        score = evaluateGuess(guess, secret_code, code_length)
        print(score)
        possibleCodes = removeImpossibleCodes(possibleCodes, guess, score)
        print(f"Aantal mogelijke combinaties: {len(possibleCodes)}")
        if score[0] == code_length:
            print("De computer heeft gewonnen!")
            break
    else:
        print("De computer heeft verloren!")
        print(f"De geheime code was: {secret_code}")

def playAI():
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']
    code_length = 4
    max_guesses = 10
    possibleCodes = createPossibleCodes(colors, code_length)
    secret_code = random.choice(possibleCodes)
    print("De computer heeft een code gegenereerd!")
    guesses = []
    for i in range(max_guesses):
        print(f"Gok #{i+1}:")
        guess = input("Voer een code in: ")
        guesses.append(guess)
        score = evaluateGuess(guess, secret_code, code_length)
        print(score)
        if score[0] == code_length:
            print("Je hebt de code geraden!")
            break
    else:
        print("Je hebt verloren!")
        print(f"De geheime code was: {secret_code}")


if __name__ == "__main__":
    playGame()
