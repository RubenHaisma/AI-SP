### This code was partially produced by the help of Github Co-pilot and ChatGPT. Other than that, I did not use any other sources.

import random
import itertools
import math

def main():
    print("Welcome to Mastermind!")
    print("Select a game mode:")
    print("1. Codemaker (Player creates the code, AI tries to break it)")
    print("2. Codebreaker (AI creates the code, Player tries to break it)")
    print("3. Codemaker vs Codebreaker (AI creates the code, AI tries to break it)")
    game_mode = input("Enter the number corresponding to your choice: ")
    colors = ["R", "G", "B", "Y", "O", "P"]
    code_length = 4
    while True:
        if game_mode == "1":
            code = player_codemaker(colors, code_length)
            game_mode_1(code, colors, code_length)
        elif game_mode == "2":
            code = ai_codemaker(colors, code_length)
            game_mode_2(code, colors)
        elif game_mode == "3":
            game_mode_3(colors, code_length)
        else:
            print("Invalid choice. Please try again.")
        play_again = input("Do you want to play again? (yes/no) ").lower()
        if play_again == "no":
            break
        else:
            game_mode = input("Enter the number corresponding to your choice: ")
    print("Thanks for playing Mastermind!")

def player_codemaker(colors, code_length):
    code = input("Enter your code ({} letters from {}):".format(code_length, colors))
    while True:
        if all(c in colors for c in code) and len(code) == code_length:
            return code
        else:
            print("Invalid code. Please try again.")
            code = input("Enter your code ({} letters from {}):".format(code_length, colors))

def ai_codemaker(colors, code_length):
    code = "".join(random.choices(colors, k=code_length))
    print("The AI's code is: {}".format(code))
    return code

def game_mode_1(code, colors, code_length):
    MAX_GUESSES = 10
    n = len(colors)
    s = [set() for i in range(code_length+1)]
    for x in itertools.product(colors, repeat=code_length):
        for p in itertools.permutations(x):
            b, w = get_feedback(p, code)
            s[b].add(p)
    guess = random.choice(list(s[code_length-1]))
    print("The AI's first guess is: {}".format(guess))
    for i in range(MAX_GUESSES-1):
        b, w = get_feedback(guess, code)
        s = [set([x for x in t if get_feedback(x, guess) == (b,w)]) for t in s]
        if not s[code_length-1]:
            return []
        guess = random.choice(list(s[code_length-1]))
        print("The AI's next guess is: {}".format(guess))
        print("Steps taken: ", i + 2)
        if guess == code:
            print(guess)
            print("The AI has won!")
    return [guess]



def minimax_guess(possible_codes):
    count = {code: 0 for code in possible_codes}
    for guess in possible_codes:
        for code in possible_codes:
            feedback = get_feedback(guess, code)
            count[guess] = max(count[guess], min_possible_feedback(feedback, possible_codes))
    return max(count, key=count.get)

def update_possible_codes(guess, feedback, possible_codes):
    return [code for code in possible_codes if get_feedback(guess, code) == feedback]

def min_possible_feedback(feedback, possible_codes):
    min_count = float("inf")
    for code in possible_codes:
        count = 0
        for other_code in possible_codes:
            if get_feedback(code, other_code) != feedback:
                count += 1
        min_count = min(min_count, count)
    return min_count


def ai_guesser(colors, code_length, feedback=None):
    if feedback:
        # Use feedback to eliminate possibilities and make a better guess
        pass
    else:
        # Make an initial random guess
        guess = "".join(random.choice(colors) for _ in range(code_length))
    return guess

def game_mode_2(code, colors):
    code_length = len(code)
    print("The code has been created. You have 10 chances to guess the code.")
    for i in range(10):
        guess = input("Enter your guess ({} letters from {}):".format(code_length, colors))
        while True:
            if all(c in colors for c in guess) and len(guess) == code_length:
                break
            else:
                print("Invalid guess. Please try again.")
                guess = input("Enter your guess ({} letters from {}):".format(code_length, colors))
        feedback = get_feedback(guess, code)
        print("{} black pegs and {} white pegs".format(feedback[0], feedback[1]))
        if feedback[0] == code_length:
            print("You win! The code was {}".format(code))
            break
    else:
        print("You lose! The code was {}".format(code))


def ai_guess(code, colors):
    guess = "".join(random.choices(colors, k=len(code)))
    return guess

def get_feedback(guess, code):
    black_pegs = 0
    white_pegs = 0
    code_list = list(code)
    for i in range(len(guess)):
        if guess[i] == code[i]:
            black_pegs += 1
            code_list[i] = None
    for i in range(len(guess)):
        for j in range(len(code_list)):
            if guess[i] == code_list[j]:
                white_pegs += 1
                code_list[j] = None
                break
    return black_pegs, white_pegs - black_pegs


def original_algorithm(code, colors, code_length):
    possible_codes = [''.join(i) for i in itertools.product(colors, repeat=code_length)]
    guess = random.choice(possible_codes)
    for i in range(1, len(possible_codes)):
        feedback = get_feedback(code, guess)
        possible_codes = [x for x in possible_codes if get_feedback(x, guess) == feedback]
        if len(possible_codes) == 4:
            return possible_codes[0]
        guess = random.choice(possible_codes)
    return guess

def game_mode_3(colors, code_length):
    code = ai_codemaker(colors, code_length)
    possible_codes = [''.join(i) for i in itertools.product(colors, repeat=code_length)]
    guess = original_algorithm(code, colors, code_length)
    turn = 0
    while True:
        turn += 1
        print("AI's guess: ", guess)
        feedback = get_feedback(code, guess)
        print("Feedback: ", feedback)
        if feedback == code_length * 'B':
            print("AI broke the code in {} turns".format(turn))
            break
        code = ai_codemaker(colors, code_length)
        possible_codes = [x for x in possible_codes if get_feedback(x, guess) == feedback]
        guess = original_algorithm(code, colors, code_length)

if __name__ == '__main__':
    main()