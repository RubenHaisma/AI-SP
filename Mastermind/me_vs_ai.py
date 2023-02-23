import random
import itertools

# Function to create a list of all possible codes given a list of colors and number of positions
def createPossibleCodes(colors, numberOfPositions: int):
    possibleCodes = []
    for code in itertools.product(colors, repeat=numberOfPositions):
        possibleCodes.append(''.join(code))
    return possibleCodes

# Function to randomly select a code from a list of possible codes
def next_guess(possibleCodes):
    return random.choice(possibleCodes)

# Function to evaluate a guess and return the score
def evaluate(guess, secret, codeLength):
    score = [0, 0]
    used = []
    # Check for black pins
    for position in range(codeLength):
        if guess[position] == secret[position]:
            score[0] += 1
            used.append(position)
    # Check for white pins
    secretCopy = secret[::]
    for position in used:
        secretCopy = secretCopy[:position] + '-' + secretCopy[position + 1:]
    for i in range(codeLength):
        if i not in used:
            if guess[i] in secretCopy:
                score[1] += 1
                secretCopy = secretCopy[:secretCopy.index(guess[i])] + '-' + secretCopy[secretCopy.index(guess[i]) + 1:]
    return score

# Function to remove all codes that are not possible given a guess and score
def removeImpossibleCodes(possibleCodes, guess, score):
    for code in possibleCodes:
        if evaluate(code, guess, len(code)) != score:
            possibleCodes.remove(code)
    return possibleCodes

# Function to allow the computer to generate a code and the player to guess it
def play_game_3():
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
        score = evaluate(guess, secret_code, code_length)
        print(score)
        if score[0] == code_length:
            print("Je hebt de code geraden!")
            break
    else:
        print("Je hebt verloren!")
        print(f"De geheime code was: {secret_code}")

if __name__ == '__main__':
    play_game_3()