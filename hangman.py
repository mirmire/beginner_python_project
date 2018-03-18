#!/usr/bin/python3
"""Hangman game in Python3"""
# Prakash Acharya, 18.03.2018
import random


def randomize():
    countries = ['finland', 'nepal', 'germany', 'sweden', 'honduras',
                 'mauritania', 'mongolia', 'bulgaria', 'mozambique']
    selection = random.choice(countries)
    return selection


def play():
    word_to_be_guessed = randomize()
    # create an empty list of underscores
    # of the lenght of the word to be guessed
    guess_status = len(word_to_be_guessed) * ['_']
    number_of_guesses = 15

    def show_answer_and_ask_play_again(won_or_lost):
        if won_or_lost == 'won':
            print("\nCongratulations! The answer was {}.\n"
                  .format(word_to_be_guessed.upper()))
        else:
            print("\nOoops, you lost! The answer was {}.\n"
                  "This is how you are hanged:\n"
                  .format(word_to_be_guessed.upper()))
            print("""
                   +---+
                   |  |
                  \O/ |
                  ||  |
                  /\  |
                      |
             ============
                         """)

        replay_answer = input("Do you want to play the game again? ")
        if replay_answer.startswith(("Y", "y")):
            play()
        else:
            print("Bye!")
            exit()

    while number_of_guesses > 0:
        user_guess = input("{}  Type in your guesses: "
                           .format("".join(guess_status)))

        if len(user_guess) == 1:
            number_of_guesses -= 1
            for letter_index in range(len(word_to_be_guessed)):
                if word_to_be_guessed[letter_index] == user_guess:
                    guess_status[letter_index] = user_guess
            if "_" not in guess_status:
                show_answer_and_ask_play_again('won')

        elif len(user_guess) > 1:
            if user_guess == 'give up':
                show_answer_and_ask_play_again('lost')
            number_of_guesses -= 1
            if user_guess == word_to_be_guessed:
                show_answer_and_ask_play_again('won')

    # if 15 mistakes made, show answer and ask to play again
    show_answer_and_ask_play_again('lost')


if __name__ == '__main__':
    print("Welcome to HangmanPy game. You have to guess the name of\n"
          "a country in 15 tries. Write 'give up' if you give up.\n")
    play()
