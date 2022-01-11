class Basics23:

    def __init__(self):
        self.symm_nums = [7227, 12567, 44444444, 9939, 1112111]
        self.mul_nums = [(2, 3), (1, 2, 3, 4), (54, 75, 453, 0), (10, -2)]
        self.square_input = [9119, 2483, 3212]
        self.setify_input = [[1, 3, 3, 5, 5], [4, 4, 4, 4], [5, 7, 8, 9, 10, 15], [3, 3, 3, 2, 1]]
        self.data = [42, 12345, 666, 512]

    '''
    Question 1
    Create a function that takes a number as an argument and returns True or False depending 
    on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.
    Examples
    is_symmetrical(7227) ➞ True
    is_symmetrical(12567) ➞ False
    is_symmetrical(44444444) ➞ True
    is_symmetrical(9939) ➞ False
    is_symmetrical(1112111) ➞ True
    '''

    def is_symmetrical(self):
        for num in self.symm_nums:
            num_list = list(str(num))
            rev_list = list(str(num))
            rev_list.reverse()
            symm = False
            if num_list == rev_list:
                symm = True

            print(f'is_symmetrical({num}) -> {symm}')

    def ques1(self):
        self.is_symmetrical()

    '''
    Question 2
    Given a string of numbers separated by a comma and space, return the product of the numbers.
    Examples
    multiply_nums("2, 3") ➞ 6
    multiply_nums("1, 2, 3, 4") ➞ 24
    multiply_nums("54, 75, 453, 0") ➞ 0
    multiply_nums("10, -2") ➞ -20
    '''

    def multiply_names(self):
        for tup in self.mul_nums:
            ans = 1
            for n in tup:
                ans *= n
            print(f'multiply_names{tup} -> {ans}')

    def ques2(self):
        self.multiply_names()

    '''
    Question 3
    Create a function that squares every digit of a number.
    Examples
    square_digits(9119) ➞ 811181
    square_digits(2483) ➞ 416649
    square_digits(3212) ➞ 9414
    Notes
    The function receives an integer and must return an integer.
    '''

    def square_digits(self):
        for n in self.square_input:
            digit_list = list(str(n))
            ans = ''
            for digit in digit_list:
                ans += str(int(digit) ** 2)

            print(f'square_digits({n}) -> {ans}')

    def ques3(self):
        self.square_digits()

    '''
    Question 4
    Create a function that sorts a list and removes all duplicate items from it.
    Examples
    setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
    setify([4, 4, 4, 4]) ➞ [4]
    setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
    setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]
    '''

    def setify(self):
        for lst in self.setify_input:
            temp_list = lst
            temp_list.sort()
            for n in temp_list:
                if temp_list.count(n) > 1:
                    temp_list.remove(n)

            print(f'{temp_list}')

    def ques4(self):
        self.setify()

    '''
    Question 5
    Create a function that returns the mean of all digits.
    Examples
    mean(42) ➞ 3
    mean(12345) ➞ 3
    mean(666) ➞ 6
    Notes
    •	The mean of all digits is the sum of digits / how many digits there are 
        (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
    •	The mean will always be an integer.
    '''

    def mean(self):
        for num in self.data:
            total = 0
            number = num
            digits = 0
            while number > 0:
                rem = number % 10
                total += rem
                number = number // 10
                digits += 1

            print(f'mean({num}) -> {total // digits}')

    def ques5(self):
        self.mean()
