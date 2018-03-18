#!/usr/bin/python3
# A program to find given number's factors

num = int(input("The number to calculate the factors of: "))
factors = []


def calculate_factors(num):
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
            i += 1


calculate_factors(num)
print(factors)
