import random


class Basics11:

    def __init__(self):
        self.word_length = 7
        self.bin_string = '11001001'
        self.str1 = 'Python is an amazing language'
        self.str2 = 'So is Java, its amazing as well as cool'
        self.dup_str = 'hello there freak , I said Hello you freak'
        print(self.str1)
        print(self.str2)
        self.alphabets = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def generate_words(self):
        a_list = [x for x in self.alphabets]
        gen_word_list = []
        for i in range(self.word_length):
            gen_word_list.append(random.choice(a_list))

        output_string = ''
        for char in gen_word_list:
            output_string += char

        return output_string

    def removing_char(self):
        index = 6
        original = self.generate_words()
        print(f'original word: {original}')
        o_list = [x for x in original]
        o_list.remove(o_list[index])

        output_string = ''
        for char in o_list:
            output_string += char
        print(f'modded word: {output_string}')

    def is_binary(self):
        usr_bin = self.bin_string

        if not usr_bin.isdigit():
            return False
        else:
            bin_list = [x for x in usr_bin]
            for char in bin_list:
                if not (char == '1' or char == '0'):
                    return False
            return True

    def binary_check(self):
        if self.is_binary():
            print(f'{self.bin_string} is a binary number')
        else:
            print(f'{self.bin_string} is not a binary number')

    def uncommon_words(self):

        w_l1 = self.str1.split(' ')
        w_l2 = self.str2.split(' ')

        o_l = []
        if len(w_l1) >= len(w_l2):
            short_list = w_l2
            length = len(w_l2)
        else:
            short_list = w_l1
            length = len(w_l1)

        for i in range(length):
            word = short_list[i]
            if (word in w_l1) and not (word in w_l2):
                o_l.append(word)

        print(f'uncommon words are: {o_l}')

    def duplicate_strings(self):
        d_list = self.dup_str.lower().split(' ')
        output_list = []

        for char in d_list:
            if (d_list.count(char) > 1) and not (char in output_list):
                output_list.append(char)

        print(f'original: {self.dup_str}')
        print(f'duplicates: {output_list}')
