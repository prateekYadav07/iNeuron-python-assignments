class Advanced5:

    def __init__(self):
        self.even_or_odd_input_list = [1, 2, 3, 6, 8, 334, 67, 4567, 95, 4]
        self.votes = [["A", "A", "B"], ["A", "A", "A", "B", "C", "A"], ["A", "B", "B", "A", "C", "C"]]
        self.to_censor = [("Today is a Wednesday!", ["Today", "a"], "-"),
                          ("The cow jumped over the moon.", ["cow", "over"], "*"),
                          ("Why did the chicken cross the road ?", ["did", "chicken", "road"], "*")
                          ]
        self.polydivisiblity_check = [1232, 123220]
        self.prime_sum = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                          [2, 3, 4, 11, 20, 50, 71],
                          []
                          ]

    '''
    1. Create a function that takes a number n (integer greater than zero) as an argument, 
    and returns 2 if n is odd and 8 if n is even.
    You can only use the following arithmetic operators: addition of numbers +, subtraction of numbers -,
    multiplication of number *, division of number /, and exponentiation **.
    You are not allowed to use any other methods in this challenge (i.e. no if statements, comparison operators, etc).
    
    Examples
    f(1) ➞ 2
    f(2) ➞ 8
    f(3) ➞ 2
    '''
    # def f(self):
    #     for n in self.even_or_odd_input_list:
    #         even_odd = n%2 ? 2:8
    #
    # def ques1(self):
    #     self.f()

    '''
    2. Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 
    times in a list (where N is the length of the list).

    Examples
    majority_vote(["A", "A", "B"]) ➞ "A"
    majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
    majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
    '''

    def majority_vote(self):
        for lst in self.votes:
            maj_vote = None
            half_length = len(lst) // 2

            for char in lst:
                if lst.count(char) > half_length:
                    maj_vote = char

            print(f'majority_vote({lst}) -> \'{maj_vote}\'')

    def ques2(self):
        self.majority_vote()

    '''
    3. Create a function that takes a string txt and censors any word from a given list lst. 
    The text removed must be replaced by the given character char.

    Examples
    censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
    censor_string("The cow jumped over the moon.", ["cow", "over"], "*") -> "The *** jumped **** the moon."
    censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"
    '''

    def replace(self, sen_list, word, char):
        index_of_w = sen_list.index(word)
        sen_list.remove(word)
        censored_word = char * len(word)
        sen_list.insert(index_of_w, censored_word)

    def censor_string(self):
        for tup in self.to_censor:
            sentence_list = [x for x in tup[0].split()]
            censor_words = tup[1]
            censor_char = tup[-1]

            for word in censor_words:
                if word in sentence_list:
                    self.replace(sentence_list, word, censor_char)

            sentence = ''
            for word in sentence_list:
                sentence += word + " "

            print(f'censor_string({tup[0]}) -> {sentence}')

    def ques3(self):
        self.censor_string()

    '''
    4. In mathematics a Polydivisible Number (or magic number) is a number in a given number base with digits abcde...
     that has the following properties:

    -  Its first digit a is not 0.
    - The number formed by its first two digits ab is a multiple of 2.
    - The number formed by its first three digits abc is a multiple of 3.
    - The number formed by its first four digits abcd is a multiple of 4.
    
    Create a function which takes an integer n and returns True if the given number is a 
    Polydivisible Number and False otherwise.
    
    Examples
    
    is_polydivisible(1232) ➞ True
    # 1     / 1 = 1
    # 12    / 2 = 6
    # 123   / 3 = 41
    # 1232  / 4 = 308
    
    is_polydivisible(123220) ➞ False
    # 1   / 1 = 1
    # 12   / 2 = 6
    # 123   / 3 = 41
    # 1232   / 4 = 308
    # 12322   / 5 = 2464.4         # Not a Whole Number
    # 123220   /6 = 220536.333...  # Not a Whole Number

    '''

    def polydiv_check(self, num):
        num_list = []
        for char in str(num):
            num_list.append(char)

        polydiv = True
        temp = ""
        for i in range(1, len(num_list) + 1):
            temp += num_list[i - 1]
            if int(temp) % i != 0:
                polydiv = False
                break

        return polydiv

    def is_polydivisible(self):
        for num in self.polydivisiblity_check:
            check = self.polydiv_check(num)

            print(f'is_polydiv({num}) -> {check}')

    def ques4(self):
        self.is_polydivisible()

    '''
    5. Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.

    Examples    
    sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
    sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
    sum_primes([]) ➞ None
    '''

    @staticmethod
    def is_prime(num):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        return prime

    def sum_primes(self):
        for lst in self.prime_sum:

            if 1 in lst:
                lst.remove(1)

            sum_of_prime = 0
            for num in lst:
                if self.is_prime(num):
                    sum_of_prime += num

            if sum_of_prime == 0:
                ans = None
            else:
                ans = sum_of_prime

            print(f'sum_prime({lst}) -> {ans}')

    def ques5(self):
        self.sum_primes()
