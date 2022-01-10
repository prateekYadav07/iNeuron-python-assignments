class Basics20:

    def __init__(self):
        self.ques2_list = [[0, 0, 0, 0, 0], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]

    '''
    Question2
    Given a list of numbers, create a function which returns the list but with each 
    element's index in the list added to itself. This means you add 0 to the number 
    at index 0, add 1 to the number at index 1, etc...
    Examples
    add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
    add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
    add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
    '''

    def ques2(self):
        for l in range(len(self.ques2_list)):
            temp_list = self.ques2_list[l]
            for i in range(len(temp_list)):
                temp_list[i] += i

            print(f'{temp_list}')

    '''
    
    '''