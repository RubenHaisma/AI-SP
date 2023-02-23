from simple_algorithm import *
from algorithm_1 import *
from my_algorithm import *
from me_vs_ai import *

# create a main function that calls the play_game functions from the other files and gives the user the option to choose which algorithm to use. Also add an option to play against the computer.
def main():
    print("Welkom bij Mastermind!")
    print("Kies een algoritme of spelvorm:")
    print("1. The Simple Algorithm")
    print("2. The Most-Parts Algorithm")
    print("3. My Algorithm")
    print("4. Spelen tegen de computer")
    print("5. Stoppen")
    choice = input("Kies een algoritme: ")
    if choice == "1":
        play_game_0()
    elif choice == "2":
        play_game_1()
    elif choice == "3":
        play_game_2()
    elif choice == "4":
        play_game_3()
    elif choice == "5":
        print("Bedankt voor het spelen!")        
    else:
        print("Ongeldige keuze!")
    
    if choice != "5":
        main()
        

main()
