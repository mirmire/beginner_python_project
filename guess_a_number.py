#!/usr/bin/python3
"""A number guessing game"""

from random import randint

my_guess = randint(1, 100)
user_tries = []


def play():
    try:
        user_guess = int(input("\nGuess the number I have thought:  "))
    except ValueError:
        print('Invalid input. The number is between 1 and 100.')
        play()
    else:
        user_tries.append(user_guess)
        calculate(user_guess)


def calculate(user_guess):
    while user_guess != my_guess:
        if my_guess > user_guess:
            print("My number is bigger than yours.")
            play()
        else:
            print("My number is smaller than yours.")
            play()
    print("Contratulations! My number was {0}. You made {1} tries before"
          " getting the answer right.".format(my_guess, len(user_tries) - 1))
    print("\nYour tries were:", user_tries)
    exit()


if __name__ == '__main__':
    print("""Welcome to number guessing game!
          The program thinks of a number between 1 and 100.
          You have to predict the number. Hints will be given.""")
    play()
