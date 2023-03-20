### Basically the same functions were used, but the code was rewritten (by me) 
### to reverse the code and let me play against the computer. 

import random
import itertools

#import the functions from the functions.py file
from functions import *

# Function to randomly select a code from a list of possible codes
def next_guess(possibleCodes):
    return random.choice(possibleCodes)

# Function to allow the computer to generate a code and the player to guess it
playAI()