### This code was partially produced by the help of Github Co-pilot and ChatGPT. Other than that, I did not use any other sources.

import random

def evaluate_guess(guess, code):
    exact_matches = 0
    color_matches = 0
    for i, c in enumerate(guess):
        if c == code[i]:
            exact_matches += 1
        elif c in code:
            color_matches += 1
    return (exact_matches, color_matches)

def game_mode():
    print("Welcome to Mastermind! Select a game mode:")
    print("1. Human vs. Computer")
    print("2. Computer vs. Human")
    print("3. Computer vs. Computer")
    mode = input("Enter the number of your choice: ")

    if mode == "1":
        code = input("Enter a 4-digit code using the colors red (R), green (G), blue (B), yellow (Y), orange (O), and purple (P): ")
        code = [c for c in code]
        print("The code has been set.")
        print("The computer will now make its first guess.")
        max_attempts = 10
        attempts = 0
        while attempts < max_attempts:
            # Computer's guess using a known algorithm
            guess = random.sample(['R', 'G', 'B', 'Y', 'O', 'P'], 4)
            result = evaluate_guess(guess, code)
            print("The computer's guess is: {}".format("".join(guess)))
            print("{} color(s) are correct and in the correct position.".format(result[0]))
            print("{} color(s) are correct but in the wrong position.".format(result[1]))

            if result[0] == 4:
                print("The computer wins! The code was {}.".format("".join(code)))
                break

            attempts += 1
        if attempts == max_attempts:
            print("You win! The code was {}.".format("".join(code)))

    elif mode == "2":
        code = []
        while len(code) < 4:
            guess = input("Enter a color: ")
            if guess in ['R', 'G', 'B', 'Y', 'O', 'P']:
                code.append(guess)
        print("The code has been set.")
        print("You will now try to guess the code.")
        max_attempts = 10
        attempts = 0
        while attempts < max_attempts:
            guess = input("Enter your guess (4 colors): ")
            guess = [c for c in guess]
            result = evaluate_guess(guess, code)
            print("{} color(s) are correct and in the correct position.".format(result[0]))
            print("{} color(s) are correct but in the wrong position.".format(result[1]))

            if result[0] == 4:
                print("You win! The code was {}.".format("".join(code)))
                break

            attempts += 1
        if attempts == max_attempts:
            print("The computer wins! The code was {}.".format("".join(code)))
    elif mode == "3":
        code = random.sample(['R', 'G', 'B', 'Y', 'O', 'P'], 4)
        print("The computer has set a code.")
        print("The computer will now make its first guess.")
        max_attempts = 10
        attempts = 0
        while attempts < max_attempts:
            # Computer's guess using a known algorithm
            guess = random.sample(['R', 'G', 'B', 'Y', 'O', 'P'], 4)
            result = evaluate_guess(guess, code)
            print("The computer's guess is: {}".format("".join(guess)))
            print("{} color(s) are correct and in the correct position.".format(result[0]))
            print("{} color(s) are correct but in the wrong position.".format(result[1]))

            if result[0] == 4:
                print("The computer wins! The code was {}.".format("".join(code)))
                print("it took {} attempts".format(attempts))
                break

            attempts += 1
        if attempts == max_attempts:
            print("The computer loses! The code was {}.".format("".join(code)))


game_mode()