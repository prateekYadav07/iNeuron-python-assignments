import math
import random


class Basics16:

    def __init__(self):
        self.stutter_words = 'incredible, enthusiastic, outstanding'

    '''
    Question1. Write a function that stutters a word as if someone is struggling 
    to read it. The first two letters are repeated twice with an 
    ellipsis ... and space after each, and then the word is pronounced with a 
    question mark ?.
    Examples
    stutter("incredible") ➞ "in... in... incredible?"
    stutter("enthusiastic") ➞ "en... en... enthusiastic?"
    stutter("outstanding") ➞ "ou... ou... outstanding?"
    Hint :- Assume all input is in lower case and at least two characters long.
    '''

    def stutter(self):
        word_list = self.stutter_words.split(",")
        for x in word_list:
            two_letters = x.strip()[0:2]
            temp = two_letters + "..."
            print(temp + " " + temp + " " + x + "?")

    def ques1(self):
        self.stutter()

    '''
    Question 2.Create a function that takes an angle in radians and returns 
    the corresponding angle in degrees rounded to one decimal place.
    Examples
    radians_to_degrees(1) ➞ 57.3
    radians_to_degrees(20) ➞ 1145.9
    radians_to_degrees(50) ➞ 2864.8
    '''

    @staticmethod
    def radians_to_degrees():
        for i in range(3):
            angle_in_radians = random.randint(1, 51)
            angle_in_degrees = math.degrees(angle_in_radians)
            print(f'radians_to_degrees({angle_in_radians}) -> {angle_in_degrees:.1f}')

    def ques2(self):
        self.radians_to_degrees()

    '''
    Question 3. In this challenge, establish if a given integer num is a 
    Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 
    multiplied by num, then num is a Curzon number.
    Given a non-negative integer num, implement a function that returns True if num 
    is a Curzon number, or False otherwise.
    Examples
    is_curzon(5) ➞ True
    # 2 ** 5 + 1 = 33
    # 2 * 5 + 1 = 11
    # 33 is a multiple of 11
    
    is_curzon(10) ➞ False
    # 2 ** 10 + 1 = 1025
    # 2 * 10 + 1 = 21
    # 1025 is not a multiple of 21
    
    is_curzon(14) ➞ True
    # 2 ** 14 + 1 = 16385
    # 2 * 14 + 1 = 29
    # 16385 is a multiple of 29
    '''

    @staticmethod
    def curzon():
        print("All curzon Numbers between 1 and 100:")
        for i in range(1, 50):
            eqn1 = 2 ** i + 1
            eqn2 = 2 * i + 1

            if eqn1 % eqn2 == 0:
                print(i, end=" ")

        print()

    def ques3(self):
        self.curzon()

    '''
    Question 4.Given the side length x find the area of a hexagon.
    Examples
    area_of_hexagon(1) ➞ 2.6    
    area_of_hexagon(2) ➞ 10.4
    area_of_hexagon(3) ➞ 23.4
    '''

    @staticmethod
    def area_of_hexagon():
        print("area of hexagons with sides from 1 to 15:")
        for i in range(1, 16):
            area = (3 * math.pow(3, 0.5)) * i ** 2 / 2
            print(f'side {i} units : area {area : .2f} unit square')

    def ques4(self):
        self.area_of_hexagon()

    '''
    Question 5. Create a function that returns a base-2 (binary) representation of 
    a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and 
    (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
    Going from right to left, the value of the most right bit is 1, now from that 
    every bit to the left will be x2 the value, value of an 8 bit binary numbers 
    are (256, 128, 64, 32, 16, 8, 4, 2, 1).
    Examples
    binary(1) ➞ "1"
    # 1*1 = 1
    
    binary(5) ➞ "101"
    # 1*1 + 1*4 = 5
    
    binary(10) ➞ "1010"
    # 1*2 + 1*8 = 10
    '''

    @staticmethod
    def binary():
        print("Decimal to Binary numbers from 0 to 15: ")
        print(f'binary(0) -> 0000')
        for i in range(1, 16):
            num = i
            temp = ""
            while i > 0:
                rem = i % 2
                temp = str(rem) + temp
                i = i // 2

            if len(temp)<4:
                for j in range(4-len(temp)):
                    temp = "0" + temp
                print(f'binary({num}) -> {temp}')
            else:
                print(f'binary({num}) -> {temp}')

    def ques5(self):
        self.binary()
