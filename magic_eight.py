#!/usr/bin/python3
import random
import time
'''A python program to play magic 8 ball game '''


def play():
    '''start the game by asking the question'''
    input("Type in your question:    ")
    print('\nHmmm... Thinking......\n')
    time.sleep(3)
    messages = ['Yes', 'No', 'Very likely', 'Ask me tomorrow',
                '60%', '25', 'You should know this yourself']
    print(random.choice(messages))
    ask_play_again()


def ask_play_again():
    '''ask the user if they want to play again'''
    ui = input("Do you have another question?:  ")
    if ui.startswith(('Y', 'y')):
        play()
    elif ui.startswith(('n', 'N')) or ui == 'quit':
        quit()
    else:
        print("Input not recognised. Type 'yes' or 'no' or 'quit' to quit")
        ask_play_again()


if __name__ == '__main__':
    print("Welcome to the Magic 8 ball game!")
    play()
