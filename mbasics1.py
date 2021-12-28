import random as r


class Basics1:

    def __init__(self):
        self.n1 = r.randint(1, 20)
        self.n2 = r.randint(1, 20)
        print('Hello Python')

    def add(self):
        result = self.n1 + self.n2
        print(f'add({self.n1},{self.n2}) returns {result}')

    def divide(self):
        div = f'{self.n1 / self.n2 : 0.2f}'
        print(f'{self.n1} / {self.n2} : {div}')

    def area_of_triangle(self):
        area = f'{.5 * self.n1 * self.n2 : 0.2f}'
        print(f'base: {self.n1} & height: {self.n2} , area: {area}')

    def swap(self):
        print(f'{self.n1} and {self.n2} before swap')
        self.n1, self.n2 = self.n2, self.n1
        print(f'{self.n1} and {self.n2} after swap')

    def random_number(self):
        upto = r.randint(1, 100)
        print(f'a random number {r.randint(0, upto)}')
