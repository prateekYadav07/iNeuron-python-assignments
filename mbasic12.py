import random


class Basics12:

    def __init__(self):

        self.names = ['suresh', 'mahesh', 'ramesh', 'naresh', 'thugesh', 'fuckesh', 'futesh', 'suckesh', 'hitesh']
        self.names2 = ['sonu', 'monu', 'tonu', 'susano', 'sukano', 'sasuke', 'sakura', 'hinata', 'tobi']
        self.numbers_dict = {}
        self.numbers_dict_2 = {}
        for name in self.names:
            self.numbers_dict[name] = random.randint(1, 50)
        for name in self.names2:
            self.numbers_dict_2[name] = random.randint(1, 50)

        print(self.numbers_dict)
        print(self.numbers_dict_2)

    def sum_values(self):
        print(f'sum of all values: {sum(self.numbers_dict.values())}')

    def merging_dicts(self):
        merged_dict = {}

        merged_dict = self.numbers_dict | self.numbers_dict_2
        print(merged_dict)

    def sorting(self):
        # sort by key
        print('sorted by keys ')
        keys = list(sorted(self.numbers_dict))
        sort_by_keys = {}
        print(keys)
        for key in keys:
            sort_by_keys[key] = self.numbers_dict[key]

        print(sort_by_keys)

        # sort by values
        print('sorted by values')
        values = list(sorted(self.numbers_dict.values()))
        sort_by_value = {}
        for i in values:
            key = list(self.numbers_dict.keys())[list(self.numbers_dict.values()).index(i)]
            sort_by_value[key] = i
        print(sort_by_value)
