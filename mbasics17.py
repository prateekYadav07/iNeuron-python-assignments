import re


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


class Basics17:

    def __init__(self):
        self.three_numbers = '1,10,3'
        self.signs = '1 < 2 < 6 < 9 > 3'
        self.string = 'minnie mouse'
        self.replacing_char = '?'
        self.fact = 7
        self.string1 = "prateek"
        self.string2 = "parteek"

    '''
    Question1. Create a function that takes three arguments a, b, c and returns the sum of the 
    numbers that are evenly divided by c from the range a, b inclusive.
    Examples
    evenly_divisible(1, 10, 20) ➞ 0
    # No number between 1 and 10 can be evenly divided by 20.
    
    evenly_divisible(1, 10, 2) ➞ 30
    # 2 + 4 + 6 + 8 + 10 = 30
    
    evenly_divisible(1, 10, 3) ➞ 18
    # 3 + 6 + 9 = 18
    '''

    def evenly_divisible(self):
        nl = [int(x) for x in self.three_numbers.split(",")]

        total = 0
        for i in range(nl[0], nl[1] + 1):
            if i % nl[2] == 0:
                total += i

        if total > 0:
            print(f'{total}')
        else:
            print(f'There is no number between {nl[0]} and {nl[1]} divisible by {nl[2]}')

    def ques1(self):
        self.evenly_divisible()

    '''
    Question2. Create a function that returns True if a given inequality expression is correct
    and False otherwise.
    Examples
    correct_signs("3 < 7 < 11") ➞ True
    
    correct_signs("13 > 44 > 33 > 1") ➞ False
    
    correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
    '''

    def correct_signs(self):
        self.signs = self.signs.replace(" ", "")
        res = re.split("[<>]", self.signs)
        num_list = [int(x) for x in res]
        op_string = []
        for i in range(len(num_list) - 1):
            if num_list[i] > num_list[i + 1]:
                op_string.append('>')
            else:
                op_string.append('<')

        output = ""
        output += str(num_list[0])
        for i in range(len(op_string)):
            output += op_string[i] + str(num_list[i + 1])
        print(output)
        if output == self.signs.strip():
            return True
        else:
            return False

    def ques2(self):
        if self.correct_signs():
            print('True')
        else:
            print('False')

    '''
    Question3. Create a function that replaces all the vowels in a string with a 
    specified character.
    Examples
    replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
    
    replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
    
    replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"

    '''

    def replacing_vowels(self):
        vowels = 'aeiou'
        op_string = self.string
        for char in op_string:
            if char.lower() in vowels:
                op_string = op_string.replace(char, self.replacing_char)

        print(f'original: {self.string}, vowels replaced: {op_string}')

    def ques3(self):
        self.replacing_vowels()

    '''
    Question4. Write a function that calculates the factorial of a number recursively.
    Examples
    factorial(5) ➞ 120
    
    factorial(3) ➞ 6
    
    factorial(1) ➞ 1
    
    factorial(0) ➞ 1
    '''

    def ques4(self):
        print(f'factorial({self.fact}) -> {factorial(self.fact)}')

    '''
    Question 5
    Hamming distance is the number of characters that differ between two strings.
    To illustrate:
    String1: "abcbba"
    String2: "abcbda"
    
    Hamming Distance: 1 - "b" vs. "d" is the only difference.
    Create a function that computes the hamming distance between two strings.
    
    Examples
    hamming_distance("abcde", "bcdef") ➞ 5
    hamming_distance("abcde", "abcde") ➞ 0
    hamming_distance("strong", "strung") ➞ 1
    '''

    def hamming_distance(self):
        sum1, sum2 = 0, 0
        for char in self.string1: sum1 += ord(char)
        for char in self.string2: sum2 += ord(char)

        print(f'hamming_distance({self.string1},{self.string2}), hamming distnce:{abs(sum1 - sum2)}')

    def ques5(self):
        self.hamming_distance()
