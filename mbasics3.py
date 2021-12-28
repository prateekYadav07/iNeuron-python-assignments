import random as r


def is_prime(temp):
    prime = True
    for i in range(2, temp):
        if temp % i == 0:
            prime = False
            return prime
    return prime


class Basics3:

    def __init__(self):
        self.num = r.randint(-20, 20)
        self.year = r.randint(1800, 3000)
        self.prime_num = r.randint(1, 1000)
        self.upto = 10000

    def pos_neg_zero(self):

        if self.num > 0:
            print(f'{self.num} is positive')
        elif self.num < 0:
            print(f'{self.num} is negative')
        else:
            print(f'{self.num} is zero')

    def odd_even(self):

        if self.num % 2 == 0:
            print(f'{self.num} is even')
        else:
            print(f'{self.num} is odd')

    def leap_year(self):

        leap = False

        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False

        if leap:
            print(f'{self.year} is a leap year')
        else:
            print(f'{self.year} is not a leap year')

    def check_prime(self):

        if is_prime(self.prime_num):
            print(f'{self.prime_num} is prime')
        else:
            print(f'{self.prime_num} is not a prime')

    def print_primes(self):

        for i in range(2, self.upto + 1):
            if is_prime(i):
                print(i, end=', ')

        print()