class Advanced7:

    def __init__(self):
        self.rugs = [
            [
                "AAAA",
                "ABBA",
                "AAAA"
            ],
            [
                "AAAAAAAAA",
                "ABBBBBBBA",
                "ABBAAABBA",
                "ABBBBBBBA",
                "AAAAAAAAA"
            ],
            [
                "AAAAAAAAAAA",
                "AABBBBBBBAA",
                "AABCCCCCBAA",
                "AABCAAACBAA",
                "AABCADACBAA",
                "AABCAAACBAA",
                "AABCCCCCBAA",
                "AABBBBBBBAA",
                "AAAAAAAAAAA"
            ]
        ]
        self.dance_forms = [
            [
                "Dub,Dancehall",
                "Industrial,Heavy Metal",
                "Techno,Dubstep",
                "Synth-pop,Euro-Disco",
                "Industrial,Techno,Minimal"
            ],
            [
                "Soul",
                "House,Folk",
                "Trance,Downtempo,Big Beat,House",
                "Deep House",
                "Soul"
            ]
        ]
        self.power_ques_inputs = [(2, 49, 65), (3, 1, 27), (10, 1, 5), (5, 31, 33), (4, 250, 1300)]
        self.find_difference = [972882, 3320707, 90010]

    '''
    1. Write a function that counts how many concentric layers a rug.
    
    Examples
    
    count_layers([
      "AAAA",
      "ABBA",
      "AAAA"
    ]) ➞ 2
    
    count_layers([
      "AAAAAAAAA",
      "ABBBBBBBA",
      "ABBAAABBA",
      "ABBBBBBBA",
      "AAAAAAAAA"
    ]) ➞ 3
    
    count_layers([
      "AAAAAAAAAAA",
      "AABBBBBBBAA",
      "AABCCCCCBAA",
      "AABCAAACBAA",
      "AABCADACBAA",
      "AABCAAACBAA",
      "AABCCCCCBAA",
      "AABBBBBBBAA",
      "AAAAAAAAAAA"
    ]) ➞ 5

    '''

    def count_layers(self):
        for rug in self.rugs:
            size = len(rug)
            layers = size // 2 + 1
            print(f'count_layers({rug}) -> {layers}')

    def ques1(self):
        self.count_layers()

    '''
    2. There are many different styles of music and many albums exhibit multiple styles. Create a function 
    that takes a list of musical styles from albums and returns how many styles are unique.
    Examples
    
    unique_styles([
      "Dub,Dancehall",
      "Industrial,Heavy Metal",
      "Techno,Dubstep",
      "Synth-pop,Euro-Disco",
      "Industrial,Techno,Minimal"
    ]) ➞ 9
    
    unique_styles([
      "Soul",
      "House,Folk",
      "Trance,Downtempo,Big Beat,House",
      "Deep House",
      "Soul"
    ]) ➞ 7
    '''

    def unique_style(self):
        for dances in self.dance_forms:
            different_styles = []
            for string in dances:
                if len(string) > 1:
                    for x in string.split(","):
                        different_styles.append(x)
                else:
                    different_styles.append(string)

            print(f'unique_styles({dances}) -> {len(set(different_styles))}')

    def ques2(self):
        self.unique_style()

    '''
    4. Create a function that takes in n, a, b and returns the number of positive values raised to the 
    nth power that lie in the range [a, b], inclusive.

    Examples
    power_ranger(2, 49, 65) ➞ 2
    # 2 squares (n^2) lie between 49 and 65, 49 (7^2) and 64 (8^2)
    
    power_ranger(3, 1, 27) ➞ 3
    # 3 cubes (n^3) lie between 1 and 27, 1 (1^3), 8 (2^3) and 27 (3^3)
    
    power_ranger(10, 1, 5) ➞ 1
    # 1 value raised to the 10th power lies between 1 and 5, 1 (1^10)
    
    power_ranger(5, 31, 33) ➞ 1
    
    power_ranger(4, 250, 1300) ➞ 3

    '''

    def power_ranger(self):
        for tup in self.power_ques_inputs:
            n = tup[0]
            a = tup[1]
            b = tup[2]

            power_list = []
            temp = 0
            i = 1
            while temp < b:
                num = i ** n
                if a <= num <= b:
                    power_list.append(num)
                temp = num
                i += 1

            print(f'power_ranger({tup}) -> {len(power_list)}')

    def ques4(self):
        self.power_ranger()

    '''
    5. Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.

    Examples
    rearranged_difference(972882) ➞ 760833
    # 988722 - 227889 = 760833
    
    rearranged_difference(3320707) ➞ 7709823
    # 7733200 - 23377 = 7709823
    
    rearranged_difference(90010) ➞ 90981
    # 91000 - 19 = 90981
    '''

    def rearranged_difference(self):
        for number in self.find_difference:
            num_list = [int(x) for x in str(number)]
            num_list.sort(reverse=True)
            max_num = ""

            for n in num_list:
                max_num += str(n)
            max_num = int(max_num)

            min_num = ""
            for n in sorted(num_list):
                min_num += str(n)
            min_num = int(min_num)

            difference = max_num - min_num
            print(f'rearranged_defference({number}) -> {difference}')

    def ques5(self):
        self.rearranged_difference()
