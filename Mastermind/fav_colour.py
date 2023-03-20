### My algorithm uses the same functions as the simple algorithm, but it uses a different next_guess function,
### it takes into account what the favorite colour of the guesses is and uses that to make a first guess.
import itertools

def createPossibleCodes(colors, numberOfPositions: int):
    # Creeert een lijst van alle mogelijke oplossingen op basis van een lijst met colors en het aantal posities
    possibleCodes = []
    for code in itertools.product(colors, repeat=numberOfPositions):
        possibleCodes.append(''.join(code))
    return possibleCodes
    
def evaluateGuess(guess, secret, codeLength):
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
    # Create a new list of possible codes that should be kept
    newPossibleCodes = []
    for code in possibleCodes:
        if evaluateGuess(code, guess, len(code)) == score:
            newPossibleCodes.append(code)
    # Replace the original list with the new list
    possibleCodes[:] = newPossibleCodes
    return possibleCodes

def next_guess(possibleCodes, pastGuesses, favoriteColor):
    if len(pastGuesses) == 0:
        # Use favorite color to form the first guess
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
    return bestCode

def play_game_2():  # Function to actually start playing the game
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']
    code_length = 4
    max_guesses = 10
    possibleCodes = createPossibleCodes(colors, code_length)
    favorite_color = input("Wat is je favoriete kleur? ")
    if favorite_color not in colors:
        print("Dat is geen geldige kleur!")
        play_game_2()
    secret_code = input("Bedenk de geheime code: ")
    print("Laat de computer raden!")
    print(f"De geheime code is: {secret_code}")
    guesses = []
    for i in range(max_guesses):
        print(f"Gok #{i+1}:")
        guess = next_guess(possibleCodes, guesses, favorite_color)
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

if __name__ == '__main__':
    play_game_2()
    