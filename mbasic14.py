from random import choice
from random import randint


class Basics14:

    def __init__(self):
        self.n = 100
        self.line = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'
        self.numbers = []
        for x in range(20):
            self.numbers.append(randint(1, 100))
        self.lookfor = choice(self.numbers)

    '''
    Question 1: Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

    '''

    @staticmethod
    def generate_7(num):
        if num % 7 == 0:
            yield num

    def ques1(self):
        for i in range(self.n):
            for j in self.generate_7(i):
                print(j, end=' ')
        print()

    '''
    Question 2:
    Write a program to compute the frequency of the words from the input. The output should output after sorting the 
    key alphanumerically. 
    Suppose the following input is supplied to the program:
    New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
    Then, the output should be:
    2:2
    3.:1
    3?:1
    New:1
    Python:5
    Read:1
    and:1
    between:1
    choosing:1
    or:2
    to:1
    '''

    def ques2(self):
        input_list = self.line.split()
        output_dic = {}
        new_dic = {}

        for i in input_list:
            output_dic[i] = input_list.count(i)

        keys_list = output_dic.keys()
        keys_list = sorted(keys_list)
        for key in keys_list:
            new_dic[key] = output_dic[key]

        print(new_dic)

    '''
    Question 3:
    Define a class Person and its two child classes: Male and Female.
     All classes have a method "getGender" which can
     print "Male" for Male class and "Female" for Female class.
    '''

    class Person:

        class Male:

            def __init__(self):
                self.sex = 'male'

            def getGender(self):
                print(self.sex)

        class Female:
            def __init__(self):
                self.sex = 'Female'

            def getGender(self):
                print(self.sex)

    '''
    Question 4:
    Please write a program to generate all sentences where subject is in ["I", "You"] 
    and verb is in ["Play", "Love"] and the 
    object is in ["Hockey","Football"].

    '''

    def ques4(self):
        subject = ['I', 'You']
        verb = ['play', 'love']
        objects = ['Hockey', 'football']
        output_sentences = []

        while len(output_sentences) < 6:
            s = choice(subject)
            v = choice(verb)
            o = choice(objects)

            sen = f'{s} {v} {o}'
            if sen not in output_sentences:
                output_sentences.append(sen)

        for sentence in output_sentences:
            print(sentence)

    '''
    Question 6:
    Please write a binary search function which searches an item in a sorted list. 
    The function should return the index of element to be searched in the list.
    '''

    def ques6(self):
        num_list = sorted(self.numbers)
        print(num_list)
        print(f'index of {self.lookfor}')
        first_index = 0
        last_index = len(num_list)

        for i in range(first_index, last_index):
            middle = (first_index + last_index)//2

            if num_list[middle] == self.lookfor:
                print(middle)
                break
            elif num_list[middle]> self.lookfor:
                last_index = middle
            else:
                first_index = middle

