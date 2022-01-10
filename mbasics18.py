import random


class Basics18:

    def __init__(self):
        self.lst1 = [1, 2, "a", 'b', 'v']
        self.lst = ["a", "a", "a", "b"]
        self.string = 'Hello Python'
        self.ele = 'a'

    '''
    Question 1
    Create a function that takes a list of non-negative integers and strings and return a 
    new list without the strings.
    Examples
    filter_list([1, 2, "a", "b"]) ➞ [1, 2]
    
    filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
    
    filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
    '''

    def filter_list(self):
        lst = self.lst1
        for char in lst:
            if str(char).isalpha():
                lst.remove(char)
        print(f'{self.lst1} -> {lst}')

    def ques1(self):
        self.filter_list()

    '''
    Question 2
    The "Reverser" takes a string as input and returns that string in reverse order, with the 
    opposite case.
    Examples
    reverse("Hello World") ➞ "DLROw OLLEh"
    
    reverse("ReVeRsE") ➞ "eSrEvEr"
    
    reverse("Radar") ➞ "RADAr"

    '''

    def reverse(self):
        op_string = ''
        op_string = self.string[-1::-1].swapcase()
        print(f'{self.string} -> {op_string}')

    def ques2(self):
        self.reverse()

    '''
    Question 5
    Write a function that moves all elements of one type to the end of the list.
    Examples
    move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
    # Move all the 1s to the end of the array.
    
    move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
    
    move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]
    '''

    def move_to_end(self):
        temp_list = self.lst
        element = self.ele
        op_list = []
        count_element = 0
        for i in range(len(temp_list)):
            if temp_list[i] == element:
                count_element +=1

        for i in range(len(temp_list)):
            if not element == temp_list[i]:
                op_list.append(temp_list[i])

        for i in range(count_element):
            op_list.append(element)

        print(f'{temp_list} -> {op_list}')

    def ques5(self):
        self.move_to_end()
