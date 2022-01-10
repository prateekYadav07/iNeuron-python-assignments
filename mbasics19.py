import random


class Basics19:

    def __init__(self):
        self.ques1_string = 'Hello World!'
        self.ques2_boolean = None
        self.times_folded = random.randint(1,30)
        self.ques4_string = 'eQuINoX'


    '''
    Question1
    Create a function that takes a string and returns a string in which each character 
    is repeated once.
    Examples
    double_char("String") ➞ "SSttrriinngg"
    
    double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"
    
    double_char("1234!_ ") ➞ "11223344!!__  "

    '''

    def string_repetitions(self):
        st_list = [x for x in self.ques1_string]
        op_string = ''
        for char in st_list:
            op_string += char * 2
        print(op_string)

    def ques1(self):
        self.string_repetitions()

    '''
    Question2
    Create a function that reverses a boolean value and returns the string 
    "boolean expected" if another variable type is given.
    Examples
    reverse(True) ➞ False
    
    reverse(False) ➞ True
    
    reverse(0) ➞ "boolean expected"
    
    reverse(None) ➞ "boolean expected"
    '''

    def boolean_reverse(self):
        if type(self.ques2_boolean) == bool:
            print(not self.ques2_boolean)
        else:
            print('boolean expected')

    def ques2(self):
        self.boolean_reverse()

    '''
    Question3
    Create a function that returns the thickness (in meters) of a piece of paper after 
    folding it n number of times. The paper starts off with a thickness of 0.5mm.
    Examples
    num_layers(1) ➞ "0.001m"
    # Paper folded once is 1mm (equal to 0.001m)
    
    num_layers(4) ➞ "0.008m"
    # Paper folded 4 times is 8mm (equal to 0.008m)
    
    num_layers(21) ➞ "1048.576m"
    # Paper folded 21 times is 1048576mm (equal to 1048.576m)
    '''

    def paper_thickness(self):
           return 2**self.times_folded / 1000

    def ques3(self):
        print(f'paper folded {self.times_folded} times, thickness: {self.paper_thickness()} metres')

    '''
    Question4
    Create a function that takes a single string as argument and returns an ordered list 
    containing the indices of all capital letters in the string.
    Examples
    index_of_caps("eDaBiT") ➞ [1, 3, 5]
    index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
    index_of_caps("determine") ➞ []
    index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]
    index_of_caps("sUn") ➞ [1]
    '''

    def capital_index(self):
        op_list = []
        for char in self.ques4_string:
            if char.isupper():
                op_list.append(self.ques4_string.index(char))
        return op_list

    def ques4(self):
        print(f'{self.ques4_string} -> {self.capital_index()}')

    '''
    Question5
    Using list comprehensions, create a function that finds all even numbers from
    1 to the given number.
    Examples
    find_even_nums(8) ➞ [2, 4, 6, 8]
    
    find_even_nums(4) ➞ [2, 4]
    
    find_even_nums(2) ➞ [2]

        BORING!!!!!

    '''

