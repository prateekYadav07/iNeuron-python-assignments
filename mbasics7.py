import random


class Basics7:

    def __init__(self):
        self.array = []
        for x in range(20):
            self.array.append(random.randint(1, 100))
        print(self.array)

    def sum_of_array(self):
        print(sum(self.array))

    def largest_element(self):
        numbers = sorted(self.array)
        print(numbers[-1])

    def shift_amount(self, i, shift):
        return (i + shift) % len(self.array)

    def array_rotation(self):
        numbers_list = self.array

        shift = random.randint(0, len(numbers_list))
        print(f'shift will be of: {shift} in left direction', end=' ')
        for i in range(len(numbers_list)):
            sa = self.shift_amount(i, shift)
            print(numbers_list[sa], end=' ')

        print()

    def splitting_array(self):
        numbers_list = self.array

        split = random.randint(0, len(numbers_list) - 1)
        temp = []
        print(f'array will be splitted from {split}', end=' ')
        for i in range(split, len(numbers_list)):
            temp.append(numbers_list[i])

        for i in range(0, split):
            temp.append(numbers_list[i])

        print(temp)
