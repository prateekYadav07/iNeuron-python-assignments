import random as r

s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
character_list = [x for x in s]


class Basics5:

    def __init__(self):
        self.num1 = r.randint(1, 100)
        self.num2 = r.randint(1, 100)
        self.char = r.choice(character_list)

    def lcm(self):

        global greater
        if self.num1 > self.num2:
            greater = self.num1
        elif self.num2 > self.num1:
            greater = self.num2
        else:
            print(f'LCM of {self.num2} and {self.num1} is {self.num1}')

        while True:
            if (greater % self.num1 == 0) and (greater % self.num2 == 0):
                print(f'LCM of {self.num2} and {self.num1} is {greater}')
                break
            greater += 1

    def hcf(self):

        global lower
        ans = 1
        i = 2
        if self.num1 > self.num2:
            lower = self.num2
        elif self.num1 < self.num2:
            lower = self.num1

        while i <= lower:
            if (self.num1 % i == 0) and (self.num2 % i == 0):
                ans = i
            i += 1

        print(f'HCF of {self.num2} & {self.num1} is {ans}')

    def ascii_value(self):
        print(f'ASCII value of {self.char} is {ord(self.char)}')