class Basics15:

    def __init__(self):
        self.n1 = 500
        self.n2 = 10
        self.n3 = 7
        self.email = 'prateek@gmail.com'

    '''
    Question 1:
    Please write a program using generator to print the numbers 
    which can be divisible by 5 and 7 between 0 and n
    in comma separated form while n is input by console.
    Example:
    If the following n is given as input to the program:
    100
    Then, the output of the program should be:
    0,35,70
    '''

    @staticmethod
    def generate_7(num):
        if num % 7 == 0 and num % 5 == 0:
            yield num

    def ques1(self):
        o_list = []
        for num in range(self.n1):
            for i in self.generate_7(num):
                o_list.append(i)

        for i in range(len(o_list) - 1):
            print(o_list[i], end=',')
        print(o_list[-1])

    '''
    Question 2:
    Please write a program using generator to print the even numbers between
    0 and n in comma separated form while n is input by console.
    Example:
    If the following n is given as input to the program:
    10
    Then, the output of the program should be:
    0,2,4,6,8,10
    '''

    @staticmethod
    def even_generator(num):
        if num % 2 == 0:
            yield num

    def ques2(self):
        o_list = []
        for num in range(self.n2 + 1):
            for i in self.even_generator(num):
                o_list.append(i)

        for i in range(len(o_list) - 1):
            print(o_list[i], end=',')
        print(o_list[-1])

    '''
    Question 3:
    The Fibonacci Sequence is computed based on the following formula:
    f(n)=0 if n=0
    f(n)=1 if n=1
    f(n)=f(n-1)+f(n-2) if n>1
    Please write a program using list comprehension to print the Fibonacci
    sequence in comma separated form with a given n input by console.
    Example:
    If the following n is given as input to the program:
    7
    Then, the output of the program should be:
    0,1,1,2,3,5,8,13

    '''

    @staticmethod
    def fib_recursion(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return Basics15.fib_recursion(num - 1) + Basics15.fib_recursion(num - 2)

    def ques3(self):
        fib = []
        for i in range(self.n3 + 1):
            fib.append(self.fib_recursion(i))

        for i in range(len(fib) - 1):
            print(fib[i], end=',')
        print(fib[-1])

    '''
    Question 4:
    Assuming that we have some email addresses in the "username@companyname.com"
    format, please write program to print the user name of a given email 
    address. Both user names and company names are composed of letters only.
    Example:
    If the following email address is given as input to the program:
    john@google.com
    Then, the output of the program should be:
    john

    '''

    def ques4(self):
        name = self.email.split('@')[0]
        print(name)

    '''
    Question 5:
    Define a class named Shape and its subclass Square. The Square class 
    has an init function which takes a length as argument. 
    Both classes have a area function which can print the area of 
    the shape where Shape's area is 0 by default.
    '''

    class Shape:

        def __init__(self):
            pass

        def show_shapes(self):
            print('Shapes: \n1.Square \n2.Triangle \n3.Rectangle \n4.Circle \n5.Trapezium')

        def get_area(self):
            area = 0
            return area

        class Square:

            def __init__(self):
                self.side = 9

            def set_side(self, usr_input):
                self.side = usr_input

            def get_area(self):
                area = self.side ** 2
                return f'{area :0.2f}'

            def get_perimeter(self):
                return f'{4 * self.side :0.2f}'
