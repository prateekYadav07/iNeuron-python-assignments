class Basics21:

    def __init__(self):
        self.adding_num = [([5, 6, 7, 8, 9], 1), ([7, 6, 3, 23, 17], 10), ([1, 10, 20, 42], 6), ([], 6)]
        self.budget_list = [
            [{"name": "John", "age": 21, "budget": 23000},
             {"name": "Steve", "age": 32, "budget": 40000},
             {"name": "Martin", "age": 16, "budget": 2700}],
            [
                {"name": "John", "age": 21, "budget": 29000},
                {"name": "Steve", "age": 32, "budget": 32000},
                {"name": "Martin", "age": 16, "budget": 1600}
            ]
        ]
        self.words = ['hello', 'edabit', 'hacker', 'geek', 'javascript']
        self.investment = [(10000, 10, 0.06, 12), (100, 1, 0.05, 1), (3500, 15, 0.1, 4), (100000, 20, 0.15, 365)]

    '''
    Question1
    Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.
    Examples
    next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
    next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
    next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]
    next_in_line([], 6) ➞ "No list has been selected"
    '''

    def next_in_line(self):
        for tup in self.adding_num:
            lst = tup[0]
            element = tup[-1]

            if len(lst) <= 0:
                print('No list has been selected')
            else:
                lst.append(element)
                lst.remove(lst[0])
                print(f'next_in_line({tup[0]}, {element}) -> {lst}')

    def ques1(self):
        self.next_in_line()

    '''
    Question2
    Create the function that takes a list of dictionaries and returns the sum of people's budgets.
    Examples
    get_budgets([
      { "name": "John", "age": 21, "budget": 23000 },
      { "name": "Steve",  "age": 32, "budget": 40000 },
      { "name": "Martin",  "age": 16, "budget": 2700 }
    ]) ➞ 65700
    
    get_budgets([
      { "name": "John",  "age": 21, "budget": 29000 },
      { "name": "Steve",  "age": 32, "budget": 32000 },
      { "name": "Martin",  "age": 16, "budget": 1600 }
    ]) ➞ 62600
    '''

    def get_budgets(self):
        for lst in self.budget_list:
            total = 0
            names = ''
            for d in lst:
                total += d['budget']
                names += d['name'] + " "
            print(f'{names} : budget -> {total}')

    def ques2(self):
        self.get_budgets()

    '''
    Question3
    Create a function that takes a string and returns a string with its letters in alphabetical order.
    Examples
    alphabet_soup("hello") ➞ "ehllo"
    alphabet_soup("edabit") ➞ "abdeit"
    alphabet_soup("hacker") ➞ "acehkr"
    alphabet_soup("geek") ➞ "eegk"
    alphabet_soup("javascript") ➞ "aacijprstv"
    '''

    def alphabet_soup(self):
        for word in self.words:
            word_list = list(word)
            word_list = sorted(word_list)
            op = ''
            for char in word_list:
                op += char
            print(f'alphabet_soup({word}) -> {op}')

    def ques3(self):
        self.alphabet_soup()

    '''
    Question4
    Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded monthly. 
    What will be the value of your investment at the end of the 10 year period?
    Create a function that accepts the principal p, the term in years t, the interest rate r, 
    and the number of compounding periods per year n. The function returns the value at the end 
    of term rounded to the nearest cent.
    For the example above:
    compound_interest(10000, 10, 0.06, 12) ➞ 18193.97
    Note that the interest rate is given as a decimal and n=12 because with monthly compounding 
    there are 12 periods per year. Compounding can also be done annually, quarterly, weekly, or daily.
    Examples
    compound_interest(100, 1, 0.05, 1) ➞ 105.0
    compound_interest(3500, 15, 0.1, 4) ➞ 15399.26
    compound_interest(100000, 20, 0.15, 365) ➞ 2007316.26
    '''

    def compound_interest(self):
        for invest in self.investment:
            principal = invest[0]
            term = invest[1]
            rate = invest[2]
            periods = invest[3]

            ci = f'{principal * (1 + rate / periods) ** (periods*term) : .2f}'

            print(f'compound_interest{invest} -> {ci}')

    def ques4(self):
        self.compound_interest()