import random as r
import math


class Basics6:

    def __init__(self):
        self.fibupto = 10
        self.fact = r.randint(5, 11)
        self.cubesum = r.randint(1, 100)
        self.weight = 65
        self.height = 1.81

    def factorial(self, n):

        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return n * self.factorial(n=n - 1)

    def bmicalc(self):
        bmi = self.weight / self.height ** 2

        if 0 < bmi <= 18.5:
            print(f'BMI is {bmi:.2f}:Underweight')
        elif 18.5 < bmi <= 25:
            print(f'BMI is {bmi:.2f}:Normal Weight')
        elif 25 < bmi <= 30:
            print(f'BMI is {bmi:.2f}:overweight')
        elif 30 < bmi <= 35:
            print(f'BMI is {bmi:.2f}:obese')
        else:
            print(f'BMI is {bmi:.2f}:clinically Obese')

    def cube_sum(self):
        n = self.cubesum
        csum = (n / 2 * (n + 1)) ** 2
        print(f'cube sum of first {self.cubesum} numbers is: {csum}')

    def finding_log(self):
        n = r.randint(1, 100)
        print(f'natural log of {n} is {math.log(n): 0.3f}')
        print(f'base 10 log of {n} is {math.log(n, 10.0): 0.3f}')
