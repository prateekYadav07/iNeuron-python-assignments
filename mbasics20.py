import math


class Basics20:

    def __init__(self):
        self.ques2_list = [[0, 0, 0, 0, 0], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
        self.cones = [(3, 2), (15, 6), (18, 0)]
        self.points = [1, 6, 215]
        self.missing_numbers_list = [[1, 2, 3, 4, 6, 7, 8, 9, 10], [7, 2, 3, 6, 5, 9, 1, 4, 8],
                                     [10, 5, 1, 2, 4, 6, 8, 3, 9]]

    '''
    Question2
    Given a list of numbers, create a function which returns the list but with each 
    element's index in the list added to itself. This means you add 0 to the number 
    at index 0, add 1 to the number at index 1, etc...
    Examples
    add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
    add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
    add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
    '''

    def ques2(self):
        for lst in range(len(self.ques2_list)):
            temp_list = self.ques2_list[lst]
            for i in range(len(temp_list)):
                temp_list[i] += i

            print(f'{temp_list}')

    '''
    Question3
    Create a function that takes the height and radius of a cone as arguments and returns 
    the volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.
    Examples
    cone_volume(3, 2) ➞ 12.57
    cone_volume(15, 6) ➞ 565.49
    cone_volume(18, 0) ➞ 0
    '''

    def volume_of_cone(self):
        for tup in self.cones:
            height = tup[0]
            radius = tup[-1]

            volume = f'{(math.pi * radius ** 2 * height) / 3: .2f}'
            print(f'cone_volume(height: {height}, radius: {radius}) -> {volume}')

    def ques3(self):
        self.volume_of_cone()

    '''
    Question4
    This Triangular Number Sequence is generated from a pattern of dots that form a triangle. 
    The first 5 numbers of the sequence, or dots, are: 
    1, 3, 6, 10, 15
    This means that the first triangle has just one dot, the second one has three dots, 
    the third one has 6 dots and so on.
    Write a function that gives the number of dots with its corresponding triangle number 
    of the sequence.
    Examples
    triangle(1) ➞ 1
    triangle(6) ➞ 21
    triangle(215) ➞ 23220
    '''

    def triangle(self):
        for point in self.points:
            triangles = 0
            for j in range(point):
                triangles += j + 1

            print(f'triangle({point}) -> {triangles}')

    def ques4(self):
        self.triangle()

    '''
    Question5
    Create a function that takes a list of numbers between 1 and 10 (excluding one number) and
    returns the missing number.
    Examples
    missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
    missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
    missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
    '''

    def missing_num(self):
        for lst in self.missing_numbers_list:
            missing = 0
            for j in range(1, 11):
                if j not in lst:
                    missing = j
                    break

            print(f'missing_num({lst}) -> {missing}')

    def ques5(self):
        self.missing_num()
