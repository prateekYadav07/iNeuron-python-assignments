class Advanced4:

    def __init__(self):
        self.fib_input = [5, 10, 20, 50]
        self.censored_strings = [("Wh*r* d*d my v*w*ls g*?", "eeioeo"),
                                 ("abcd", ""), ("*PP*RC*S*", "UEAE")]

    '''
    1. In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, 
        such that each number is the sum of the two preceding ones, starting from 0 and 1:
        The beginning of the sequence is this:
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
        The function fastFib(num) returns the fibonacci number Fn, of the given num as an argument.
        
        Examples
        fib_fast(5) ➞ 5
        fib_fast(10) ➞ 55
        fib_fast(20) ➞ 6765
        fib_fast(50) ➞ 12586269025
    '''

    @staticmethod
    def fibonnaci(num):
        a, b = 0, 1
        for i in range(num):
            a, b = b, a + b
        return a

    def fib_num(self):
        for fib in self.fib_input:
            fib_output = self.fibonnaci(fib)
            print(f'fib_num({fib}) -> {fib_output}')

    def ques1(self):
        return self.fib_num()

    '''
    2. Create a function that takes a strings characters as ASCII and returns each characters hexadecimal value as a string.
    
    Examples    
    convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"
    convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"
    convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"
    '''

    def convert_to_hex(self):
        # still processing for this question
        pass

    def ques2(self):
        self.convert_to_hex()

    '''
    3. Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.
        Given a censored string and a string of the censored vowels, return the original uncensored string.
        Example
        uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
        uncensor("abcd", "") ➞ "abcd"
        uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
    '''

    @staticmethod
    def vowels_added_again(cen_string, vowels):
        index = 0
        output_str = ''
        for char in cen_string:
            if char == '*':
                output_str += vowels[index]
                index += 1
            else:
                output_str += char
        return output_str

    def uncensor(self):
        for cen_string_tup in self.censored_strings:
            vowels = cen_string_tup[-1]
            censored_string = cen_string_tup[0]
            if len(vowels) == 0:
                print(f'uncensor({cen_string_tup}) -> {censored_string}')
            else:
                uncensored_string = self.vowels_added_again(censored_string, vowels)
                print(f'uncensor({cen_string_tup}) -> {uncensored_string}')

    def ques3(self):
        self.uncensor()

    '''
    
    '''

    # N = input()
    # speed_string = input()
    # speed_list = [int(x) for x in speed_string.split(" ")]
    #
    # count = 1
    #
    # for i in range(len(speed_list) - 1):
    #     if speed_list[i] >= speed_list[i + 1]:
    #         count += 1
    # print(count)
