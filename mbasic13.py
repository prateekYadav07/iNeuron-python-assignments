import math

from numpy import sort

import mbasic11

C = 50
H = 30


class Basics13(mbasic11.Basics11):

    def __init__(self):
        super().__init__()
        self.D = '100,150,180'
        self.array_size = '3,5'
        self.words = 'without,hello,bag,world'
        self.phrase_string = 'hello world and practice makes perfect and hello world again'
        self.sentence_q5 = 'hello world! 123'
        self.password_list = 'ABd1234@1,a F1#,2w3E*,2We3345'

    '''
    Question 1:
    Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]
    Following are the fixed values of C and H:
    C is 50. H is 30.
    D is the variable whose values should be input to your program in a comma-separated sequence.
    Example
    Let us assume the following comma separated input sequence is given to the program:
    100,150,180
    The output of the program should be:
    18,22,24
    '''

    def ques1(self):
        d_list = [int(x) for x in self.D.split(',')]
        output = []
        for d in d_list:
            q = f'{math.sqrt((2 * C * d) / H):0.0f}'
            output.append(q)

        for i in range(len(output) - 1):
            print(output[i], end=',')
        print(output[-1])

    '''
    Question 2:
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the 
    i-th row and j-th column of the array should be i*j.
    Note: i=0,1.., X-1; j=0,1,¡Y-1.
    Example
    Suppose the following inputs are given to the program:
    3,5
    Then, the output of the program should be:
    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
    '''

    def ques2(self):
        size = [int(x) for x in self.array_size.split(',')]
        m = size[0]
        n = size[-1]
        output = []

        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(i * j)
            output.append(temp)

        print(output)

    '''
    Question 3:
    Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated 
    sequence after sorting them alphabetically.
    Suppose the following input is supplied to the program:
    without,hello,bag,world
    Then, the output should be:
    bag,hello,without,world
    '''

    def ques3(self):
        word_list = [x for x in self.words.split(',')]
        word_list = sort(word_list)
        for i in range(len(word_list) - 1):
            print(word_list[i], end=',')
        print(word_list[-1])

    '''
    Question 4:
    Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing 
    all duplicate words and sorting them alphanumerically.
    Suppose the following input is supplied to the program:
    hello world and practice makes perfect and hello world again
    Then, the output should be:
    again and hello makes perfect practice world
    '''

    def ques4(self):
        unique_phrase = self.remove_duplicates(self.phrase_string)
        output = ''
        for char in sort(unique_phrase.split(' ')):
            output += char + ' '

        print(output.strip())

    '''
    Question 5:
    Write a program that accepts a sentence and calculate the number of letters and digits.
    Suppose the following input is supplied to the program:
    hello world! 123
    Then, the output should be:
    LETTERS 10
    DIGITS 3
    '''

    @staticmethod
    def count_letters_digits(string):
        letters, digits = 0, 0

        for char in list(string):
            if char.isdigit():
                digits += 1
            elif char.isalpha():
                letters += 1

        return letters, digits

    def ques5(self):
        letters, digits = self.count_letters_digits(self.sentence_q5)
        print(f'LETTERS {letters}\nDIGITS {digits}')

    '''
    Question 6:
    A website requires the users to input username and password to register. Write a program to check the validity of 
    password input by users.
    Following are the criteria for checking the password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
    Your program should accept a sequence of comma separated passwords and will check them according to the above
    criteria. Passwords that match the criteria are to be printed, each separated by a comma.
    Example
    If the following passwords are given as input to the program:
    ABd1234@1,a F1#,2w3E*,2We3345
    Then, the output of the program should be:
    ABd1234@1
    '''

    @staticmethod
    def check_validity(p_string):
        small_count, capital_count, num_count, char_count = 0, 0, 0, 0
        if 6 > len(p_string) or len(p_string) > 12:
            return False
        else:
            for char in p_string:
                if char.isspace():
                    return False
                elif char.isdigit():
                    num_count += 1
                elif char.islower():
                    small_count += 1
                elif char.isupper():
                    capital_count += 1
                elif char.isascii():
                    char_count += 1

        if small_count >= 1 and capital_count >= 1 and num_count >= 1 and char_count >= 1:
            return True
        else:
            return False

    def ques6(self):
        output = []
        for char in self.password_list.split(','):
            if self.check_validity(char):
                output.append(char)

        for char in output:
            print(char, end=' ')
        print()
