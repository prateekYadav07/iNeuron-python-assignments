class Basics25:

    def __init__(self):
        self.integers_list = [(3, 4, 3), (1, 1, 1), (3, 4, 1)]
        self.vowels = [("apples and bananas", "u"), ("cheese casserole", "o"), ("stuffed jalapeno poppers", "e")]
        self.ascii_strings = ["to be or not to be!", "THE LITTLE MERMAID", "Oh what a beautiful morning."]

    '''
    Question1
    Create a function that takes three integer arguments (a, b, c) and returns the amount of 
    integers which are of equal value.
    Examples
    equal(3, 4, 3) ➞ 2
    equal(1, 1, 1) ➞ 3
    equal(3, 4, 1) ➞ 0 
    Notes
    Your function must return 0, 2 or 3.
    '''

    def equal(self):
        for tup in self.integers_list:
            lst = []
            for char in tup:
                if tup.count(char) > 1:
                    lst.append(char)

            print(f'equal({tup}) -> {len(lst)}')

    def ques1(self):
        self.equal()

    '''
    Question4
    Write a function, that replaces all vowels in a string with a specified vowel.
    Examples
    vow_replace("apples and bananas", "u") ➞ "upplus und bununus"
    
    vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"
    
    vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"
    Notes
    All words will be lowercase. Y is not considered a vowel.

    '''

    def vow_replace(self):
        for tup in self.vowels:
            phrase = tup[0]
            replaciaso = tup[1]
            vowels = 'aeiou'

            for char in phrase:
                if char.lower() in vowels:
                    phrase = phrase.replace(char, replaciaso)

            print(f'vow_replace{tup} -> {phrase}')

    def ques4(self):
        self.vow_replace()

    '''
    Question5
    Create a function that takes a string as input and capitalizes a letter if its ASCII code 
    is even and returns its lower case version if its ASCII code is odd.
    Examples
    ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"
    
    ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"
    
    ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."
    '''

    def ascii_capitalize(self):
        for phrase in self.ascii_strings:
            sentence = phrase
            op = ''
            for char in sentence:
                if char.isalpha() and ord(char) % 2 == 0:
                    op += char.capitalize()
                else:
                    op += char.lower()
            print(f'ascii_capitalize({phrase}) -> {op}')

    def ques5(self):
        self.ascii_capitalize()
