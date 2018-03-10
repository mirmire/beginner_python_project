#!/usr/bin/python3
'''A python program to check whether a triangle is pythagorean triple or
   not'''


def ask():
    try:
        lengths = input('Type the sides of the triangle separated by comma: ')
        length_list = lengths.split(',')
        for index in range(0, 3):
            length_list[index] = int(length_list[index])
    except (IndexError,  ValueError):
        print('Please type exactly three sides of the triangle in numeric'
              ' format.\n')
        ask_to_play_again()
    hypotenuse = max(length_list)
    square_of_pb = 0  # square sum  of perpendicular and base
    for length in length_list:
        if length != hypotenuse:
            square_of_pb += length ** 2
    if hypotenuse ** 2 == square_of_pb:   # because h**2 = p**2 + b**2
        print('\nYes, this triangle is Pythagorean triple.\n')
    else:
        print('\nNo, this is not a Pythagorean triple.\n')
    ask_to_play_again()


def ask_to_play_again():
    ui = input('Do you have any other triangle to test?:  ')
    if ui.startswith(('Y', 'y')):
        ask()
    elif ui.startswith(('N', 'n')) or ui == 'exit':
        exit()
    else:
        print("Not recognised. Please type 'yes' or 'no' or 'exit' to exit.")
        ask_to_play_again()


if __name__ == '__main__':
    print(' ----- Welcome to Pythagorean triple check! -----')
    ask()
