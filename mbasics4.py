import random as r
import math


def check_armstrong(num):
    temp = 0
    numsss = num
    while numsss > 0:
        rem = numsss % 10
        temp += math.pow(rem, 3)
        numsss = numsss // 10

    if int(temp) == num:
        return True
    else:
        return False


class Basics4:

    def __init__(self):
        self.NUM = 153
        self.fact_num = r.randint(1, 20)
        self.table_num = r.randint(11, 30)
        self.upto = r.randint(11, 20)

    def fact(self):
        ans = 1
        for i in range(1, self.fact_num + 1):
            ans = ans * i

        print(f'factorial of {self.fact_num} is {ans}')

    def mulp_table(self):
        for i in range(1, 11):
            print(f'{self.table_num} x {i} : {self.table_num * i}')

    def armstrong(self):
        if check_armstrong(self.NUM):
            print(f'{self.NUM} is an armstrong')
        else:
            print(f'{self.NUM} is not an armstrong')

    def print_armstrong(self):
        for i in range(100, 10000):
            if check_armstrong(i):
                print(i, end=' ')
        print()

    def natural_numbers(self):
        total = 0
        for i in range(1, self.upto+1):
            total += i

        print(f'sum of natural numbers upto {self.upto} is {total}')

    def fib(self):
        a = 0
        b = 1
        for i in range(self.upto):
            print(a, end=' ')
            a, b = a + b, a
        print()
