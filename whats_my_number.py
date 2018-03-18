#!/usr/bin/python3


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
    if str(num)[-1] == str(len(str(num))):
        return True
    else:
        return False


for num in range(1, 1001):
    if len(str(num)) > 1:
        if is_prime(num):
            if '1' not in str(num) and '7' not in str(num):
                if summation(num) <= 10:
                    if is_odd(num):
                        if is_even(num):
                            if last_digit(num):
                                print(num)
