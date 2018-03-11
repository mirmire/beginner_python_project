#!/usr/bin/python3
'''A python program to predict coin number and wrappers needed for them'''


def ask_unit():
    try:
        selected_unit = int(input('Choose a unit: 1 for grams, 2 for pounds:'))
        if not (selected_unit == 1 or selected_unit == 2):
            raise ValueError()
    except (ValueError, TypeError):
        print('Choose a valid number.\n')
        ask_unit()
    ask_weight(selected_unit)


def ask_weight(unit):
    try:
        print("\nType the weight of the coin package without unit.\n"
              "Enter 0 if you have no coins of a group.\n")
        five_weight = float(input('five cents: '))
        ten_weight = float(input('ten cents: '))
        twenty_weight = float(input('twenty cents: '))
        fifty_weight = float(input('fifty cents: '))
        calculate(five_weight, ten_weight, twenty_weight, fifty_weight, unit)
    except (ValueError, TypeError):
        print('Invalid input. Start over again.')
        ask_weight(unit)


def calculate(fiv, ten, twe, fif, unit):
    if unit == 1:
        number_of_five = fiv / 3.92
        number_of_ten = ten / 4.10
        number_of_twenty = twe / 5.74
        number_of_fifty = fif / 7.80
    else:
        number_of_five = fiv / 0.008642121
        number_of_ten = ten / 0.009038953
        number_of_twenty = twe / 0.01265453
        number_of_fifty = fif / 0.01719606

    value_of_five = number_of_five * 5
    value_of_ten = number_of_ten * 10
    value_of_twenty = number_of_twenty * 20
    value_of_fifty = number_of_fifty * 50
    total = (value_of_five + value_of_ten +
             value_of_twenty + value_of_fifty)
    print("""\nYou have: {0} five cent coins,
          {1} ten cent coins,
          {2} twenty cent coins and
          {3} fifty cent coins.\n""".format(round(number_of_five),
                                            round(number_of_ten),
                                            round(number_of_twenty),
                                            round(number_of_fifty)))

    print("""You need: {0} wrapper(s) for five cent coins,
          {1} for ten cents,
          {2} for twenty cents and
          {3} for fifty cents.\n""".format(round(number_of_five/50),
                                           round(number_of_ten/40),
                                           round(number_of_twenty/40),
                                           round(number_of_fifty/40)))
    print("\nYou should have approximately {0:.2f} euros.".format(total/100))


if __name__ == '__main__':
    print("You can calculate how many coins you have and how many wrappers\n"
          " you will need just by giving the weight of the coins.\n")
    ask_unit()
