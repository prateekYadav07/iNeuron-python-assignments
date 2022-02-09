class Advanced10:

    def __init__(self):
        self.frames = [(4, 5, "#"), (10, 3, "*"), (2, 5, "0")]
        self.booleans = [[True, True, False, True],
                         [True, True, False, False],
                         [True, True, False, False]
                         ]
        self.duplicates = ["Fortune favours the bold.", "You can lead a horse to water, but you can't make him drink.",
                           "Look before you leap.", "An apple a day keeps the doctor away."]

    '''
    1. Create a function that takes the width, height and character and returns a picture frame as a 2D list.
    
    Examples
    
    get_frame(4, 5, "#") ➞ [
      ["####"],
      ["#  #"],
      ["#  #"],
      ["#  #"],
      ["####"]
    ]
    # Frame is 4 characters wide and 5 characters tall.
    
    
    get_frame(10, 3, "*") ➞ [
      ["**********"],
      ["*        *"],
      ["**********"]
    ]
    # Frame is 10 characters and wide and 3 characters tall.
    
    
    get_frame(2, 5, "0") ➞ "invalid"
    # Frame's width is not more than 2.
    '''

    def get_frame(self):
        for frame in self.frames:

            height_of_tower = frame[0]
            width_of_pattern = frame[1]
            character = frame[2]

            if height_of_tower <= 2:
                print(f'get_frame({frame}) -> "invalid"')
                break
            else:
                print(f'get_frame({frame}) -> ')
                for i in range(height_of_tower):
                    L = ""
                    if i==0 or i==height_of_tower-1:
                        L += character * width_of_pattern
                    else:
                        L += character + " " * (width_of_pattern - 2) + character

                    op_list = [L]
                    print(op_list)

    def ques1(self):
        self.get_frame()

    '''
    2. Write three functions:

      1. boolean_and
      2. boolean_or
      3. boolean_xor
    These functions should evaluate a list of True and False values, starting from the leftmost element and evaluating 
    pairwise.
    
    Examples
    
    boolean_and([True, True, False, True]) ➞ False
    # [True, True, False, True] => [True, False, True] => [False, True] => False
    
    boolean_or([True, True, False, False]) ➞ True
    # [True, True, False, True] => [True, False, False] => [True, False] => True
    
    boolean_xor([True, True, False, False]) ➞ False
    # [True, True, False, False] => [False, False, False] => [False, False] => False
    '''
    def boolean_xor(self):
        for lst in self.booleans:
            for i in range(len(lst) - 1):
                ans = lst[i] ^ lst[i + 1]

            print(f'boolean_xor({lst}) -> {ans}')

    def boolean_OR(self):
        for lst in self.booleans:
            for i in range(len(lst) - 1):
                ans = lst[i] or lst[i + 1]

            print(f'boolean_or({lst}) -> {ans}')

    def boolean_and(self):
        for lst in self.booleans:
            for i in range(len(lst)-1):
                ans = lst[i] and lst[i+1]

            print(f'boolean_and({lst}) -> {ans}')

    def ques2(self):
        self.boolean_and()
        self.boolean_OR()
        self.boolean_xor()

    '''
    4. Given a common phrase, return False if any individual word in the phrase contains duplicate letters. 
    Return True otherwise.

    Examples
    
    no_duplicate_letters("Fortune favours the bold.") ➞ True
    
    no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True
    
    no_duplicate_letters("Look before you leap.") ➞ False
    # Duplicate letters in "Look" and "before".
    
    no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
    # Duplicate letters in "apple", "keeps", "doctor", and "away".

    '''
    def no_duplicate_letters(self):
        for sentence in self.duplicates:
            no_duplicates = True
            for word in sentence.split(" "):
                for ch in word:
                    if word.count(ch)>1:
                        no_duplicates = False
                        break
            print(f'no_duplicate_letters({sentence}) -> {no_duplicates}')

    def ques4(self):
        self.no_duplicate_letters()

    '''
    
    5. Write a regular expression that will match the states that voted yes to President Trump's impeachment. 
    You must use RegEx positive lookahead.
    
    Example
    
    txt = "Texas = no, California = yes, Florida = yes, Michigan = no"
    pattern = "yourregularexpressionhere"
    
    re.findall(pattern, txt) ➞ ["California", "Florida"]
    '''