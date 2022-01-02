class Basics9:

    def __init__(self):
        self.disarn = 135
        self.happy = 13
        self.harshad = 121

    def count_digits(self, number):
        temp = 0
        while number > 0:
            number = number // 10
            temp += 1

        return int(temp)

    def is_disarium(self, num):
        count = self.count_digits(num)
        temp = num
        summed = 0
        while num > 0:
            rem = num % 10
            summed += rem ** count
            num = num // 10
            count -= 1
        if int(summed) == int(temp):
            return True
        else:
            return False

    def disarium_number(self):
        num = self.disarn
        if self.is_disarium(num):
            print(f'{num} is a disarium number')
        else:
            print(f'{num} is not a disarium number')

    def print_disarium_numbers(self):
        print('Disarium numbers: ', end='')
        for i in range(200):
            if self.is_disarium(i):
                print(i, end=' ')

        print()

    def is_happy(self, num):
        temp = 0
        over = True
        while over:

            while num > 0:
                temp += (num % 10) ** 2
                num = num // 10
            if temp < 10:
                over = False
            else:
                num = temp
                temp = 0

        if int(temp) == 1 or int(temp) == 7:
            return True
        else:
            return False

    def happy_number(self):
        n1 = self.happy

        if self.is_happy(n1):
            print(f'{n1} is a happy number')
        else:
            print(f'{n1} is not a happy number')

    def print_happy_number(self):
        for i in range(101):
            if self.is_happy(i):
                print(i, end=' ')
        print()

    def is_harshad(self, num):
        deno = 0
        numer = num
        while num > 0:
            rem = int(num % 10)
            deno += rem
            num = num // 10

        if int(numer % deno) == 0:
            return True
        else:
            return False

    def harshad_number(self):
        if self.is_harshad(self.harshad):
            print(f'{self.harshad} is a harshad number')
        else:
            print(f'{self.harshad} is not a harshad number')

    def print_harshad_numbers(self):
        print('sddf')
        for i in range(10, 201):
            if self.is_harshad(i):
                print(i, end=' ')
        print()
