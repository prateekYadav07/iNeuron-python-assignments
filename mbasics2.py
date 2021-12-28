import random as r
import calendar
import math


class Basics2:

    def __init__(self):
        self.distance = r.randint(1, 100)
        self.temperature = 20
        self.year = 2022
        self.months = 1
        self.a, self.b, self.c = 2, 7, 1

    def km_to_miles(self):
        miles = f'{self.distance * 0.62 : 0.2f}'
        print(f'{self.distance}km is {miles}miles')

    def celsius_to_fahrenheit(self):
        fahrenheit = (self.temperature * (9 / 5)) + 32
        print(f'{self.temperature}°C is {fahrenheit:0.1f}°F')

    def month(self):
        print(calendar.month(theyear=self.year, themonth=self.months))

    # quadratic equation of the form: aX2 + bX + c = 0
    def quadratic_equation(self):
        D = self.b ** 2 - 4 * self.a * self.c

        if D >= 0:
            root1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(D)) / (2 * self.a)
            print(f'roots are real: {root1 : 0.2f} & {root2 : 0.2f}')
        else:
            real_part = -self.b / (2 * self.a)
            img_part = math.sqrt(-D) / (2 * self.a)
            print(f'roots are imaginary with: real part:{real_part: 0.2f} & img part: {img_part: 0.2f}i')
