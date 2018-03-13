#!/usr/bin/python3
"""A number guessing game"""

from random import randint


def think():
    comp_guess = randint(1, 100)
    user_tries = []
    play(comp_guess, user_tries)


def play(comp_guess, user_tries):
    try:
        user_guess = int(input("\nGuess the number I have thought:  "))
    except ValueError:
        print('Invalid input. The number is between 1 and 100.')
        play(comp_guess, user_tries)
    else:
        user_tries.append(user_guess)
        calculate(user_guess, comp_guess, user_tries)


def calculate(user_guess, comp_guess, user_tries):
    while user_guess != comp_guess:
        if comp_guess > user_guess:
            print("My number is bigger than yours.")
            play(comp_guess, user_tries)
        else:
            print("My number is smaller than yours.")
            play(comp_guess, user_tries)
    print("Contratulations! My number was {0}. You made {1} tries before"
          " getting the answer right.".format(comp_guess, len(user_tries) - 1))
    print("\nYour tries were:", user_tries)
    ask_play_again()


def ask_play_again():
    play_again = input("\nDo you want to play again?: ")
    if play_again.startswith(('Y', 'y')):
        think()
    elif play_again.startswith(('N', 'n')) or play_again == 'quit':
        exit()
    else:
        print("Invalid input. Type 'yes', 'no' or 'quit' to quit the game.")
        ask_play_again()


if __name__ == '__main__':
    print("""Welcome to number guessing game!
          The program thinks of a number between 1 and 100.
          You have to predict the number. Hints will be given.""")
    think()
