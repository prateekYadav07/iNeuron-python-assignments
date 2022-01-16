class Advanced1:

    def __init__(self):
        self.symbols = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
        self.ques1_input = [[["#", "!"], ["!!", "X"]], [["!!!", "O", "!"], ["X", "#", "!!!"], ["!!", "X", "O"]]]
        self.comb_input = [(2, 3), (3, 7, 4), (2, 3, 4, 5)]
        self.char_to_dots = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
            '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
            ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
            '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
        }
        self.text_to_encode = ['EDABBIT CHALLENGE', 'help me!!', "this is a stupid task"]
        self.prime_list = [7, 56963, 5151512515524]
        self.to_boolean_words = ['deep', 'loves', 'tesh', 'prATeek', 'GOAT']

    '''
    1. Write a function that takes a list of lists and returns the value of all of the 
    symbols in it, where each symbol adds or takes something from the total score. 
    Symbol values:
    # = 5
    O = 3
    X = 1
    ! = -1
    !! = -3
    !!! = -5
    
    A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.
    
    If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.
    
    Examples
    
    check_score([
      ["#", "!"],
      ["!!", "X"]
    ]) ➞ 2
    
    check_score([
      ["!!!", "O", "!"],
      ["X", "#", "!!!"],
      ["!!", "X", "O"]
    ]) ➞ -1
    '''

    def check_score(self):
        for lst in self.ques1_input:
            score = 0
            for lst1 in lst:
                for char in lst1:
                    score += self.symbols[char]

            print(f'check_score({lst}) -> {score}')

    def ques1(self):
        self.check_score()

    '''
    2. Create a function that takes a variable number of arguments, each argument representing 
    the number of items in a group, and returns the number of permutations (combinations) of items 
    that you could get by taking one item from each group.
    Examples
    combinations(2, 3) ➞ 6
    combinations(3, 7, 4) ➞ 84
    combinations(2, 3, 4, 5) ➞ 120
    '''

    def combinations(self):
        for tup in self.comb_input:
            result = 1
            for num in tup:
                result *= num

            print(f'combinations({tup}) -> {result}')

    def ques2(self):
        self.combinations()

    '''
    3. Create a function that takes a string as an argument and returns the Morse code equivalent.
    Examples
    encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
    encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"
    This dictionary can be used for coding:
    char_to_dots = {
      'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
      'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
      'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
      'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
      'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
      '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
      '6': '-....', '7': '--...', '8': '---..', '9': '----.',
      '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
      ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
      '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    '''

    def encode_morse(self):
        for text in self.text_to_encode:
            ans = ''
            for char in text:
                if char.isalpha():
                    ans += self.char_to_dots[char.upper()]
                else:
                    ans += self.char_to_dots[char]
                ans += ' '

            print(f'encode_morse({text}) -> {ans}')

    def ques3(self):
        self.encode_morse()

    '''
    4.  Write a function that takes a number and returns True if it's a prime; False otherwise. The number can be 2^64-1 (2 to the power of 63, not XOR). With the standard technique it would be O(2^64-1), which is much too large for the 10 second time limit.
    Examples
    prime(7) ➞ True
    prime(56963) ➞ True
    prime(5151512515524) ➞ False
    '''

    @staticmethod
    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def prime(self):
        for num in self.prime_list:
            print(f'prime({num}) -> {self.is_prime(num)}')

    def ques4(self):
        self.prime()

    '''
    5.  Create a function that converts a word to a bitstring and then to a boolean list based on the following criteria:

    1. Locate the position of the letter in the English alphabet (from 1 to 26).
    2. Odd positions will be represented as 1 and 0 otherwise.
    3. Convert the represented positions to boolean values, 1 for True and 0 for False.
    4. Store the conversions into an array.

    Examples
    
    to_boolean_list("deep") ➞ [False, True, True, False]
    # deep converts to 0110
    # d is the 4th alphabet - 0
    # e is the 5th alphabet - 1
    # e is the 5th alphabet - 1
    # p is the 16th alphabet - 0
    
    to_boolean_list("loves") ➞ [False, True, False, True, True]
    to_boolean_list("tesh") ➞ [False, True, True, False]
    '''

    @staticmethod
    def even_or_odd(ch):
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        return alphabets.index(ch.lower()) + 1

    def to_boolean_list(self):
        for word in self.to_boolean_words:
            bool = []
            for char in word:
                if self.even_or_odd(char) % 2 == 0:
                    bool.append(False)
                else:
                    bool.append(True)

            print(f'to_boolean_list({word}) -> {bool}')

    def ques5(self):
        self.to_boolean_list()
