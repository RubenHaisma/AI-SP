### Main function to bring it al to gether. Created by me. ###
# import the different algorithms from the different files
from fav_colour import nextGuess as nextGuessFav
from simple_algorithm import nextGuess as nextGuessSimple
from most_parts import nextGuess as nextGuessMostParts
from me_vs_ai import playAI
from functions import *

# Menu for the different play options
def menu():
    print('Welcome to Mastermind!')
    print('Please choose a mode:', '\n')
    print('1. Play against the computer using the Most-Parts algorithm')
    print('2. Play against the computer using the Simple algorithm')
    print('3. Play against the computer using the Favorite-Colour algorithm')
    print('4. Let the computer think of a code and you guess it')
    print('5. Exit', '\n')
    choice = input('Enter your choice: ')
    if choice == '1':
        playGame(nextGuessMostParts)
        menu()
    elif choice == '2':
        playGame(nextGuessSimple)
        menu()
    elif choice == '3':
        playFav(nextGuessFav)
        menu()
    elif choice == '4':
        playAI()
        menu()
    elif choice == '5':
        print('Goodbye!')
        exit()
    else:
        print('Invalid choice, please try again.')
        menu()

menu()
