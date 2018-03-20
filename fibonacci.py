#!/usr/bin/python3
# This program prints the value of nth term in Fibonacci sequence
fibo = [0]


def main():
    num = int(input("Fibonacci nth term, what should n be?: "))
    if num <= 1:
        print(num)
        exit()
    else:
        calculate(num)


def calculate(num):
        m = 0
        n = 1
        while True:
            m, n = n, m+n
            fibo.append(m)
            if len(fibo) == num:
                print(fibo[-1])
                break


if __name__ == '__main__':
    main()
