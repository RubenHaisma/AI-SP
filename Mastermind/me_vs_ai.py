### Functions from functions.py were used and the nextGuess was written by me. 
import random

# Import the functions from the functions.py file
from functions import *

# Function to randomly select a code from a list of possible codes
def next_guess(possibleCodes):
    return random.choice(possibleCodes)

# Function to allow the computer to generate a code and the player to guess it
if __name__ == "__main__":
    playAI(next_guess)
    