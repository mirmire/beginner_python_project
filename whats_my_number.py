#!/usr/bin/python3
# This problem has seven conditions to be met which is written below


def summation(num):
    answer = 0
    for i in str(num):
        answer += int(i)
    return answer


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            i += 1
    return True


def is_odd(num):
    sli = str(num)[:2]
    if (int(sli[0]) + int(sli[1])) % 2 == 0:
        return False
    else:
        return True


def is_even(num):
    if int(str(num)[-2]) % 2 == 0:
        return True
    else:
        return False


def last_digit(num):
    # look at this for example :)
    if str(num)[-1] == str(len(str(num))):
        return True
    else:
        return False


# The number is between 1 and 1000
for num in range(1, 1001):
    # The number has 2 or more digits
    if len(str(num)) > 1:
        # The number is a prime
        if is_prime(num):
            # The number does not contain 1 or 7 in it
            if '1' not in str(num) and '7' not in str(num):
                # The sum of all the digits is less or equal to 10
                if summation(num) <= 10:
                    # The fitst two digits add up to be odd
                    if is_odd(num):
                        # The second to last digit is even
                        if is_even(num):
                            # The last digit is equal to how many digits are
                            # in the number
                            if last_digit(num):
                                # It produces two numbers but
                                # you will understand :)
                                print(num)
