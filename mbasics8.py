import random


class Basics8:

    def __init__(self):

        self.punc = '!"#$%&\'()*+,-./:;?@[\]^_`{|}~ '
        self.matrix = []
        self.second_matrix = []
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(random.randint(1, 20))
            self.matrix.append(temp)

            temp = []
            for j in range(3):
                temp.append(random.randint(1, 20))
            self.second_matrix.append(temp)

        print(self.matrix)
        print(self.second_matrix)

    def add_matrices(self):
        m1 = self.matrix
        m2 = self.second_matrix
        m3 = []
        for i in range(3):
            temp = []
            for j in range(3):
                s = m1[i][j] + m2[i][j]
                temp.append(s)
            m3.append(temp)

        print(m3)

    def mul_matrix(self):
        m1 = self.matrix
        m2 = self.second_matrix
        m3 = []

        for k in range(3):
            temp = []
            for i in range(3):
                s = 0
                for j in range(3):
                    s += m1[k][j] * m2[j][i]
                temp.append(s)
            m3.append(temp)

        print(m3)

    def transpose(self):
        m1 = self.matrix
        print(f'original: {m1}')
        m1_trans = []
        for i in range(len(m1[0])):
            temp = []
            for j in range(len(m1[0])):
                temp.append(m1[j][i])
            m1_trans.append(temp)

        print(f'transposed: {m1_trans}')

    def is_punc(self, char):
        punc_list = [x for x in self.punc]
        return char in punc_list

    def remove_punctutation(self):
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        letters_list = [x for x in letters]
        pt = [x for x in self.punc]

        word = []
        for x in range(15):
            word.append(random.choice(random.choice((letters_list, pt))))

        original_string = ''
        for char in word:
            original_string += char

        print(f'original string: {original_string}')

        for i in range(len(word)):
            if self.is_punc(word[i]):
                word[i] = ' '

        unpunc_string = ''
        for char in word:
            unpunc_string += char

        print(f'unpunctuated string: {unpunc_string.strip()}')
