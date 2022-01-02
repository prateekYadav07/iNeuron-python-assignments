import random


class Basic10:

    def __init__(self):
        self.l1 = []
        self.l2 = []
        self.l3 = [[1, 2, 4], [1, 2, 4, 6, 5], [], [2, 3, 5, 6, 7], []]
        self.count = 5
        for i in range(20):
            self.l1.append(random.randint(1, 100))
            self.l2.append(random.randint(1, 10))
        print(f'list1: {self.l1}')
        print(f'list2: {self.l2}')
        print(f'list3: {self.l3}')

    def sum_of_list(self):
        print(f'sum of l1: {sum(self.l1)}')

    def product_of_elements(self):
        ans = 1
        for i in self.l2:
            ans *= i

        print(f'product of elements of l2: {ans}')

    def smallest_and_largest_number(self):
        l11 = sorted(self.l1)
        l22 = sorted(self.l2)

        print(f'smallest, largest and 2nd largest element in l1: {l11[0]} {l11[-1]} {l11[-2]}')
        print(f'smallest, largest and 2nd largest element in l2: {l22[0]} {l22[-1]} {l22[-2]}')

    def selective_large_elements(self):
        print(f'{self.count} largest elements in l1 is: {self.l1[-1:-self.count:-1]}')
        print(f'{self.count} largest elements in l2 is: {self.l2[-1:-self.count:-1]}')

    def even_odd(self):
        even = []
        odd = []
        for num in self.l1:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        print(f'even elements in l1: {even}')
        print(f'odd elements in l1: {odd}')

        even = []
        odd = []

        for num in self.l2:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        print(f'even elements in l2: {even}')
        print(f'odd elements in l2: {odd}')

    def remove_emptylist(self):
        for i in self.l3:
            if len(i) == 0:
                self.l3.remove(i)

        print(f'after empty lists have been removed: {self.l3}')

    def count_occurrence(self):
        element = random.choice(self.l2)
        print(f'{element} occurred in l1 {self.l2.count(element)} times')
