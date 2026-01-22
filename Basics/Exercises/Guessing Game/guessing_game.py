"""
========================================================================
Computer picks a random number; you guess with “too high/too low” hints.
========================================================================
"""

import random

number = random.randint(1, 10)
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("You guessed the number")
        break
    elif guess > number:
        print("Number too high")
    else:
        print("Number too low")


