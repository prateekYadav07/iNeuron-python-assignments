import re


class Advanced2:

    def __init__(self):
        self.pentagon_sizes = [1, 2, 3, 8]
        self.words_to_encrypt = ['banana', 'karaca', 'burak', 'alpaca', 'googlaetyu']
        self.cookies = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
        self.singular_words = [["cow", "pig", "cow", "cow"], ["table", "table", "table"], ["chair", "pencil", "arm"]]

    '''
    1. Write a function that takes a positive integer num and calculates how many dots exist in a pentagonal
    shape around the center dot on the Nth iteration. In the image below you can see the first iteration is
    only a single dot. On the second, there are 6 dots. On the third, there are 16 dots, and on the fourth there are 31 dots.

    ###### Image is in files given ######
    Return the number of dots that exist in the whole pentagon on the Nth iteration.

    Examples
    pentagonal(1) ➞ 1
    pentagonal(2) ➞ 6
    pentagonal(3) ➞ 16
    pentagonal(8) ➞ 141
    '''

    def pentagonal(self):
        for size in self.pentagon_sizes:
            dots = 1
            for i in range(1, size + 1):
                dots += 5 * (i - 1)

            print(f'pentagonal({size}) -> {dots}')

    def ques1(self):
        self.pentagonal()

    '''
    2.  Make a function that encrypts a given input with these steps:
    Input: "apple"
    Step 1: Reverse the input: "elppa"
    Step 2: Replace all vowels using the following chart:
    
    a => 0
    e => 1
    i => 2
    o => 2
    u => 3
    
    # "1lpp0"
    Step 3: Add "aca" to the end of the word: "1lpp0aca"
    Output: "1lpp0aca"
    Examples
    encrypt("banana") ➞ "0n0n0baca"
    encrypt("karaca") ➞ "0c0r0kaca"
    encrypt("burak") ➞ "k0r3baca"
    encrypt("alpaca") ➞ "0c0pl0aca"
    '''

    def encrypt(self):
        for word in self.words_to_encrypt:
            reverse = word[-1::-1]
            encrypted_word = ''
            vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 2, 'u': 3}
            for char in reverse:
                if char.lower() in vowels.keys():
                    encrypted_word += str(vowels[char])
                else:
                    encrypted_word += char
            encrypted_word += 'aca'

            print(f'encrypt({word}) -> {encrypted_word}')

    def ques2(self):
        self.encrypt()

    '''
    4. Write a regular expression that will help us count how many bad cookies are produced every day. You must use RegEx negative lookbehind.

    Example
    lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
    pattern = "yourregularexpressionhere"
    len(re.findall(pattern, ", ".join(lst))) ➞ 2
    '''

    def bad_cookies(self):
        pattern = 'bad cookie'
        print(f'bad cookies -> {len(re.findall(pattern, ", ".join(self.cookies)))}')

    def ques4(self):
        self.bad_cookies()

    '''
    5. Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.
    
    Examples
    pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
    pluralize(["table", "table", "table"]) ➞ { "tables" }
    pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
    '''

    def pluralize(self):
        for lst in self.singular_words:
            plural = []
            for char in lst:
                if lst.count(char) > 1:
                    plural.append(char + 's')
                else:
                    plural.append(char)

            print(f'pluralize({lst}) -> {set(plural)}')

    def ques5(self):
        self.pluralize()
