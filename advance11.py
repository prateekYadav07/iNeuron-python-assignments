import random as r


class Advanced11:

    def __init__(self):
        self.water_ballons = [[0, 0, 0, 0, 4, 0, 0, 0, 0],
                              [0, 0, 0, 3, 0, 0, 0],
                              [0, 0, 2, 0, 0],
                              [0]
                              ]
        self.alphanumeric_list = [["932c", "832u32", "2344b"],
                                  ["99a", "78b", "c2345", "11d"],
                                  ["572z", "5y5", "304q2"],
                                  []
                                  ]

    '''
    2. Once a water balloon pops, is soaks the area around it. The ground gets drier the further away you travel from the balloon.
    The effect of a water balloon popping can be modeled using a list. Create a function that takes a list which takes the pre-pop 
    state and returns the state after the balloon is popped. The pre-pop state will contain at most a single balloon, whose size is 
    represented by the only non-zero element.
    
    Examples
    pop([0, 0, 0, 0, 4, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]
    pop([0, 0, 0, 3, 0, 0, 0]) ➞ [0, 1, 2, 3, 2, 1, 0]
    pop([0, 0, 2, 0, 0]) ➞ [0, 1, 2, 1, 0]
    pop([0]) ➞ [0]
    '''

    def pop(self):
        for ballon_list in self.water_ballons:
            if len(ballon_list) < 2 or len(ballon_list) % 2 == 0:
                op_list = ballon_list
            else:
                middle = len(ballon_list) // 2
                middle_index = ballon_list.index(middle)
                for i in range(1, middle_index):
                    ballon_list[i] = i

                middle -= 1
                for j in range(middle_index + 1, len(ballon_list) - 1):
                    ballon_list[j] = middle
                    middle -= 1
                    op_list = ballon_list

            print(f'pop({ballon_list}) -> {op_list}')

    def ques1(self):
        self.pop()

    '''
    3. "Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one byone,
    saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.
    Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every 
    alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.
    
    Examples
    loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"
    loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"
    loves_me(1) ➞ "LOVES ME"
    '''

    def loves_me(self):
        for i in range(4):
            yes = "loves me"
            no = "loves me not"

            op_string = ""
            x = r.randint(1, 9)
            for i in range(x):
                if i % 2 == 0:
                    if i == x - 1:
                        op_string += yes.upper()
                    else:
                        op_string += yes + ","
                else:
                    if i == x - 1:
                        op_string += no.upper()
                    else:
                        op_string += no + ","

            print(f'loves_me({x}) -> {op_string}')

    def ques3(self):
        self.loves_me()

    '''
    4. Write a function that sorts each string in a list by the letter in alphabetic ascending order (a-z).
    
    Examples
    sort_by_letter(["932c", "832u32", "2344b"])
    ➞ ["2344b", "932c", "832u32"]
    
    sort_by_letter(["99a", "78b", "c2345", "11d"])
    ➞ ["99a", "78b", "c2345", "11d"]
    
    sort_by_letter(["572z", "5y5", "304q2"])
    ➞ ["304q2", "5y5", "572z"]
    
    sort_by_letter([])
    ➞ []
    '''

    @staticmethod
    def sorted_list_by_letter(lst):
        output = []
        str_list = []
        str_num = {}

        for char in lst:
            digits = ""

            for c in char:
                if c.isalpha():
                    str_list.append(c)
                else:
                    digits += str(c)
            str_num[str_list[-1]] = int(digits)

        str_list = sorted(str_num.keys())
        for i in range(len(str_list)):
            output.append(str(str_num[str_list[i]]) + str_list[i])

        return output

    def sort_by_letter(self):
        for lst in self.alphanumeric_list:
            if len(lst) < 1:
                op_list = []
            else:
                op_list = self.sorted_list_by_letter(lst)

            print(f'sort_by_letter({lst}) -> {op_list}')

    def ques4(self):
        self.sort_by_letter()

    '''
    5. There are three cups on a table, at positions A, B, and C. At the start, there is a ball hidden under the cup at
     position B. However, I perform several swaps on the cups, which is notated as two letters. For example, if I swap 
     the cups at positions A and B, I could notate this as AB or BA.
    Create a function that returns the letter position that the ball is at, once I finish swapping the cups. The swaps will be given to you as a list.
    
    Example
    cup_swapping(["AB", "CA", "AB"]) ➞ "C"
    
    # Ball begins at position B.
    # Cups A and B swap, so the ball is at position A.
    # Cups C and A swap, so the ball is at position C.
    # Cups A and B swap, but the ball is at position C, so it doesn't move.

    '''

    # +++++++++++++++ Wrong implementation ++++++++++++++++++

    @staticmethod
    def cup_swapping():
        swappings = ["AB", "CA", "AB"]
        positions = {"A to B": 1, "A to C": 1, "B to A": 2, "B to C": 2, "C to A": 3, "C to B": 3}
        pos_of_B = 2
        for current_position in swappings:
            st = ""
            for c in current_position:
                st += c + " to "
            st = st[:6].strip()

            pos_of_B = positions[st]

        d = {1: "A", 2: "B", 3: "C"}
        print(f'cup_swapping({swappings}) -> {d[pos_of_B]}')

    def ques5(self):
        self.cup_swapping()
