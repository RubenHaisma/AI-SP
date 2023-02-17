import random

# Code generator
def generate_code(colors, code_length):
    return ''.join([random.choice(colors) for i in range(code_length)])

# Code breaker algorithms
def random_algorithm(colors, code_length):
    possible_codes = generate_all_possible_codes(colors, code_length)
    while len(possible_codes) > 1:
        guess = random.choice(possible_codes)
        score = get_possible_scores(guess, possible_codes)
        possible_codes = [code for code in possible_codes if get_possible_scores(code, [guess]) == score]
    return possible_codes[0]

def minimax_algorithm(colors, code_length):
    possible_codes = generate_all_possible_codes(colors, code_length)
    guess = random.choice(possible_codes)
    while len(possible_codes) > 1:
        max_worst_score = 0
        for code in possible_codes:
            worst_score = min([get_possible_scores(guess, [possible_guess])[1] for possible_guess in generate_all_possible_codes(colors, code_length)])
            if worst_score > max_worst_score:
                max_worst_score = worst_score
                guess = code
        possible_codes = [code for code in possible_codes if get_possible_scores(code, [guess]) == (max_worst_score, 0)]
    return possible_codes[0]

def knuth_algorithm(colors, code_length):
    possible_codes = generate_all_possible_codes(colors, code_length)
    guess = ''.join([colors[0] for i in range(code_length)])
    while len(possible_codes) > 1:
        max_minimax_score = 0
        for code in possible_codes:
            minimax_scores = []
            for possible_guess in generate_all_possible_codes(colors, code_length):
                minimax_scores.append(get_possible_scores(code, [possible_guess])[1])
            if min(minimax_scores) > max_minimax_score:
                max_minimax_score = min(minimax_scores)
                guess = code
        possible_codes = [code for code in possible_codes if get_possible_scores(code, [guess]) == (evaluate_guess(code, guess))]
    return possible_codes[0]

# Helper functions
def generate_all_possible_codes(colors, code_length):
    if code_length == 1:
        return colors
    else:
        return [color + subcode for color in colors for subcode in generate_all_possible_codes(colors, code_length - 1)]

def get_possible_scores(guess, codes):
    scores = {}
    for code in codes:
        score = evaluate_guess(code, guess)
        if score in scores:
            scores[score] += 1
        else:
            scores[score] = 1
    return max(scores.items(), key=lambda x: x[1])[0]

def get_secret_code(colors, code_length):
    print("Enter your secret code:")
    secret_code = input().upper()
    while len(secret_code) != code_length or not all(color in colors for color in secret_code):
        print("Invalid code. Codes must be {} characters long and can only include the colors {}.".format(code_length, colors))
        secret_code = input().upper()
    return secret_code

def get_guess_from_algorithm(algorithm, possible_codes, previous_guesses, code_length, colors):
    scores = {}
    for code in possible_codes:
        score = algorithm(previous_guesses, code, code_length, colors)
        if score in scores:
            scores[score].append(code)
        else:
            scores[score] = [code]

    # Choose the code with the minimum worst-case scenario
    max_min_count = 0
    best_code = None
    for code, code_set in scores.items():
        code_set_count = len(code_set)
        if code_set_count > max_min_count:
            max_min_count = code_set_count
            best_code = code_set[0]
        elif code_set_count == max_min_count:
            best_code = code_set[0]

    return best_code

# Feedback generator
def evaluate_guess(secret_code, guess):
    black_pegs = 0
    white_pegs = 0
    code_freq = {}
    guess_freq = {}

    for i in range(len(secret_code)):
        if secret_code[i] == guess[i]:
            black_pegs += 1
        else:
            if secret_code[i] in guess_freq:
                guess_freq[secret_code[i]] += 1
            else:
                guess_freq[secret_code[i]] = 1

            if guess[i] in code_freq:
                code_freq[guess[i]] += 1
            else:
                code_freq[guess[i]] = 1

    for color in code_freq:
        if color in guess_freq:
            white_pegs += min(code_freq[color], guess_freq[color])

    return black_pegs, white_pegs

def play_game_1():
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']
    code_length = 4
    max_guesses = 10
    secret_code = generate_code(colors, code_length)
    print(f"The secret code is: {secret_code}")
    guesses = []
    for i in range(max_guesses):
        print(f"Guess #{i+1}:")
        guess = input().upper()
        while len(guess) != code_length or not all(color in colors for color in guess):
            print(f"Invalid guess. Guesses must be {code_length} characters long and can only include the colors {colors}.")
            guess = input().upper()
        guesses.append(guess)
        if guess == secret_code:
            print(f"Congratulations! You correctly guessed the code {secret_code} in {len(guesses)} guesses.")
            break
        else:
            score = evaluate_guess(guess, secret_code)
            print(f"Result: {score}")
            if i == max_guesses - 1:
                print(f"Sorry, you did not guess the code within {max_guesses} guesses. The secret code was {secret_code}.")

def play_game():
    print("Welcome to Mastermind!")
    print("Enter 'q' at any time to quit the game.")

    colors = ["R", "O", "Y", "G", "B", "P"]
    code_length = 4

    while True:
        print("\nDo you want to be the codebreaker (guess the code) or the codemaker (have the computer guess your code)?")
        print("Enter '1' to be the codebreaker, '2' to be the codemaker.")
        choice = input("Your choice: ")
        if choice == "q":
            break
        elif choice == "1":
            secret_code = generate_code(colors, code_length)
            print("The computer has generated a secret code for you to guess.")
            print("The code consists of {} colors, and the colors can repeat.".format(code_length))
            print("The possible colors are:", ", ".join(colors))
            break
        elif choice == "2":
            print("You will generate a secret code, and the computer will try to guess it.")
            print("The code consists of {} colors, and the colors can repeat.".format(code_length))
            print("The possible colors are:", ", ".join(colors))
            secret_code = get_secret_code(colors, code_length)
            guess_algorithm = input("Which guess algorithm do you want to use? Enter '1', '2', or '3': ")
            break
        else:
            print("Invalid choice. Please enter '1' or '2'.")

    guesses = []
    scores = []
    num_guesses = 0

    while True:
        num_guesses += 1
        print("\nGuess #{}:".format(num_guesses))

        if choice == "1":
            play_game_1()
        else:
            guess = get_guess_from_algorithm(guesses, scores, colors, code_length, guess_algorithm)

        if guess == "q":
            print("The secret code was:", ", ".join(secret_code))
            return

        score = evaluate_guess(guess, secret_code)
        guesses.append(guess)
        scores.append(score)

        if score == (code_length, 0):
            print("Congratulations, you guessed the code in {} guesses!".format(num_guesses))
            print("The secret code was:", ", ".join(secret_code))
            return

        print("Score:", score)


if __name__ == "__main__":
    play_game()

