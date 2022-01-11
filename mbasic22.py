class Basics22:

    def __init__(self):
        self.list_params = [(1, 10, 3), (7, 9, 2), (15, 20, 7)]
        self.simons_lists = [([1, 2], [5, 1]), ([1, 2], [5, 5]), ([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]),
                             ([1, 2, 3, 4, 5], [5, 5, 1, 2, 3])]
        self.secret_names = [["Adam", "Sarah", "Malcolm"], ["Harry", "Newt", "Luna", "Cho"],
                             ["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]]
        self.isograms = ["Algorism", "PasSword", "Consecutive"]
        self.order = ['abc', '123', 'edabit', 'xyzz']

    '''
    Question1
    Create a function that takes three parameters where:
    •	x is the start of the range (inclusive).
    •	y is the end of the range (inclusive).
    •	n is the divisor to be checked against.
    Return an ordered list with numbers in the range that are divisible by the third parameter n. 
    Return an empty list if there are no numbers that are divisible by n.
    Examples
    list_operation(1, 10, 3) ➞ [3, 6, 9]
    list_operation(7, 9, 2) ➞ [8]
    list_operation(15, 20, 7) ➞ []
    '''

    def list_operation(self):
        for tup in self.list_params:
            a = tup[0]
            b = tup[1]
            c = tup[2]
            op_list = [x for x in range(a, b) if x % c == 0]
            print(f'list_ops{tup} -> {op_list}')

    def ques1(self):
        self.list_operation()

    '''
    Question2
    Create a function that takes in two lists and returns True if the second list follows the 
    first list by one element, and False otherwise. In other words, determine if the second 
    list is the first list shifted to the right by 1.
    Examples
    simon_says([1, 2], [5, 1]) ➞ True
    simon_says([1, 2], [5, 5]) ➞ False
    simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
    simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False
    Notes
    •	Both input lists will be of the same length, and will have a minimum length of 2.
    •	The values of the 0-indexed element in the second list and the n-1th indexed element in 
        the first list do not matter.
    '''

    def simon_says(self):
        for tup in self.simons_lists:
            lst1 = tup[0]
            lst2 = tup[1]

            follows = True
            for i in range(len(lst1) - 1):
                if not lst1[i] == lst2[i + 1]:
                    follows = False

            print(f'simon_says({lst1}, {lst2}) -> {follows}')

    def ques2(self):
        self.simon_says()

    '''
    Question3
    A group of friends have decided to start a secret society. The name will be the first 
    letter of each of their names, sorted in alphabetical order.
    Create a function that takes in a list of names and returns the name of the secret society.
    Examples
    society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"
    society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"
    society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]) -> "CJMPRR
    '''

    def secret_society(self):
        for lst in self.secret_names:
            temp = ''
            op = ''
            for name in lst:
                temp += name[0]

            l = sorted(temp)
            for char in l:
                op += char.upper()

            print(f'society_name({lst}) -> {op}')

    def ques3(self):
        self.secret_society()

    '''
    Question4
    An isogram is a word that has no duplicate letters. Create a function that takes a string 
    and returns either True or False depending on whether or not it's an "isogram".
    Examples
    is_isogram("Algorism") ➞ True
    
    is_isogram("PasSword") ➞ False
    # Not case sensitive.
    
    is_isogram("Consecutive") ➞ False
    Notes
    •	Ignore letter case (should not be case sensitive).
    •	All test cases contain valid one word strings.
    '''

    def is_isogram(self):
        for iso in self.isograms:
            isog = True
            word = iso.upper()

            for char in word:
                if word.count(char) > 1:
                    isog = False
                    break

            print(f'is_isogram({iso}) -> {isog}')

    def ques4(self):
        self.is_isogram()

    '''
    Question5
    Create a function that takes a string and returns True or False, depending on whether the 
    characters are in order or not.
    Examples
    is_in_order("abc") ➞ True
    is_in_order("edabit") ➞ False
    is_in_order("123") ➞ True
    is_in_order("xyzz") ➞ True
    Notes
    You don't have to handle empty strings.
    '''

    def is_in_order(self):
        for word in self.order:
            word_list = list(word)
            ordered_list = sorted(word)

            order = False
            if ordered_list == word_list:
                order = True

            print(f'is_in_order({word}) -> {order}')

    def ques5(self):
        self.is_in_order()
