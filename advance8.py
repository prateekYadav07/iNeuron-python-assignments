class Advanced8:

    def __init__(self):
        self.vowel_property = ["a very large appliance", "go to edabit", "an open fire", "a sudden applause"]
        self.ques2_list = [("a rabbit jumps joyfully", "a", "j"),
                           ("knaves knew about waterfalls", "k", "w"),
                           ("happy birthday", "a", "y"),
                           ("precarious kangaroos", "k", "a")
                           ]
        self.positional_characters = [([2, 4, 6, 8, 10], "even"),
                                      ("EDABIT", "odd"),
                                      (["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd")
                                      ]

    '''
        1. Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a 
        vowel, while the word immediately after begins with a vowel (a e i o u).

        Examples
        vowel_links("a very large appliance") ➞ True
        vowel_links("go to edabit") ➞ True
        vowel_links("an open fire") ➞ False
        vowel_links("a sudden applause") ➞ False
    '''

    def vowel_links(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for sentence in self.vowel_property:
            prop = False
            word_list = sentence.split(" ")

            for i in range(len(word_list) - 1):
                if (word_list[i][-1] in vowels) and (word_list[i + 1][0] in vowels):
                    prop = True
                    break

            print(f'vowel_links({sentence}) -> {prop}')

    def ques1(self):
        self.vowel_links()

    '''
    2. You are given three inputs: a string, one letter, and a second letter.
    Write a function that returns True if every instance of the first letter occurs before 
    every instance of the second letter.
    
    Examples
    first_before_second("a rabbit jumps joyfully", "a", "j") ➞ True
    # Every instance of "a" occurs before every instance of "j".
    
    first_before_second("knaves knew about waterfalls", "k", "w") ➞  True
    
    first_before_second("happy birthday", "a", "y") ➞ False
    # The "a" in "birthday" occurs after the "y" in "happy".
    
    first_before_second("precarious kangaroos", "k", "a") ➞ False
    '''

    def first_before_second(self):
        for tup in self.ques2_list:
            prop = True

            sentence = tup[0]
            word1 = tup[1]
            word2 = tup[2]

            character_list = [x for x in sentence]

            for i in range(len(character_list) - 1):
                if character_list[i] == word2:
                    if word1 in character_list[i + 1:]:
                        prop = False
                        break

            print(f'first_before_second({sentence}) -> {prop}')

    def ques2(self):
        self.first_before_second()

    '''
    3. Create a function that returns the characters from a list or string r on odd or even positions, 
    depending on the specifier s. The specifier will be "odd" for items on odd positions (1, 3, 5, ...) 
    and "even" for items on even positions (2, 4, 6, ...).

    Examples
    char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
    # 4 & 8 occupy the 2nd & 4th positions
    
    char_at_pos("EDABIT", "odd") ➞ "EAI"
    # "E", "A" and "I" occupy the 1st, 3rd and 5th positions
    
    char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd") ➞ ["A", "B", "T", "A", "I", "Y"]
    '''

    def char_at_pos(self):
        for tup in self.positional_characters:
            input_stream = tup[0]
            position = tup[1]

            output_list = []

            if position.lower() == "even":
                first_index = 1
            else:
                first_index = 0

            for i in range(first_index, len(input_stream), 2):
                output_list.append(input_stream[i])

            output = ""
            if type(input_stream) == str:
                for ch in output_list:
                    output += ch
            else:
                output = output_list

            print(f'char_at_pos({tup}) -> {output}')

    def ques3(self):
        self.char_at_pos()
