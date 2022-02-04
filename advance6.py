class Advanced6:

    def __init__(self):
        self.words = [("abcd", "abcde"), ("", "y"), ("ae", "aea")]
        self.datatypes_list = [[1, 45, "Hi", False],
                               [[10, 20], ("t", "Ok"), 2, 3, 1],
                               ["Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25,
                                23],
                               [4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]]
                               ]
        self.string_fibonnaci = [(3, ["j", "h"]),
                                 (5, ["e", "a"]),
                                 (6, ["n", "k"]),
                                 ]
        self.oth = [10, 15, 22]

    '''
    1. You are given two strings s and t. String t is generated by randomly shuffling string s and 
    then adding one more letter at a random position. Return the letter that was added to t.

    Examples
    find_the_difference("abcd", "abcde") ➞ "e"
    find_the_difference("", "y") ➞ "y"
    find_the_difference("ae", "aea") ➞ "a"
    '''

    def find_the_difference(self):
        for tup in self.words:
            list1 = [x for x in tup[0]]
            list2 = [x for x in tup[-1]]
            added_word = ""
            for ch in list2:
                if list1.count(ch) > 1 or ch not in list1:
                    added_word = ch

            print(f'find_the_difference({tup}) -> {added_word}')

    def ques1(self):
        self.find_the_difference()

    '''
    2. Given a function that accepts unlimited arguments, check and count how many data types are in those arguments.
     Finally return the total in a list.
    
    List order is:
    [int, str, bool, list, tuple, dictionary]
    Examples
    count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]
    count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]
    count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]
    count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]
    '''

    def count_datatypes(self):
        for lst in self.datatypes_list:
            dl = {"int": 0, "str": 0, "bool": 0, "list": 0, "tuple": 0, "dict": 0}
            for data in lst:
                if type(data) == int:
                    dl["int"] += 1
                elif type(data) == str:
                    dl["str"] += 1
                elif type(data) == bool:
                    dl["bool"] += 1
                elif type(data) == list:
                    dl["list"] += 1
                elif type(data) == tuple:
                    dl["tuple"] += 1
                elif type(data) == dict:
                    dl["dict"] += 1

            print(f'count_datatypes({lst}) -> {list(dl.values())}')

    def ques2(self):
        self.count_datatypes()

    '''
    3. A Fibonacci string is a precedence of the Fibonacci series. It works with any two characters of the English alphabet
     (as opposed to the numbers 0 and 1 in the Fibonacci series) as the initial items and concatenates them together as it progresses 
     in a similar fashion as the Fibonacci series.
    
    Examples
    fib_str(3, ["j", "h"]) ➞ "j, h, hj"
    fib_str(5, ["e", "a"]) ➞ "e, a, ae, aea, aeaae"
    fib_str(6, ["n", "k"]) ➞ "n, k, kn, knk, knkkn, knkknknk"
    '''

    def fib_str(self):
        for data in self.string_fibonnaci:
            length = data[0]
            char_list = data[-1]

            a = char_list[0]
            b = char_list[-1]

            fib_list = []

            for i in range(length):
                fib_list.append(a)
                a, b = b, b + a

            print(f'fib_str({data}) -> {fib_list}')

    def ques3(self):
        self.fib_str()

    '''
    4. Given an integer between 0 and 26, make a variable (self.answer). That variable would be assigned to a string in this format:
    "nines:your answer, threes:your answer, ones:your answer"
    You need to find out how many ones, threes, and nines it would at least take for the number of each to add up to the given integer when multiplied by one, three or nine (depends).

    Examples    
    ones_threes_nines(10) ➞ "nines:1, threes:0, ones:1"
    ones_threes_nines(15) ➞ "nines:1, threes:2, ones:0"
    ones_threes_nines(22) ➞ "nines:2, threes:1, ones:1"
    '''

    def ones_threes_nines(self):
        for temp in self.oth:
            n = temp
            oth_dic = {"nines": 0, "threes": 0, "ones": 0}
            while n >= 1:
                if n // 9 > 0:
                    oth_dic["nines"] += n // 9
                    n = n % 9
                elif n // 3 > 0:
                    oth_dic["threes"] += n // 3
                    n = n % 3
                else:
                    oth_dic["ones"] += 1
                    n = n - 1

            print(f'ones_threes_nines({temp}) -> "', end=" ")
            for key, value in oth_dic.items():
                print(key, ":", value, end=", ")
            print('"')

    def ques4(self):
        self.ones_threes_nines()

