import math


class Advanced9:

    def __init__(self):
        self.duration_speed = [("00:30:00", 2), ("01:20:00", 1.5), ("51:20:09", 0.5)]
        self.volumes = [1071225, 4183059834009, 16]
        self.fulcrum_lists = [[3, 1, 5, 2, 4, 6, -1],
                              [1, 2, 4, 9, 10, -10, -9, 3],
                              [9, 1, 9],
                              [7, -1, 0, -1, 1, 1, 2, 3],
                              [8, 8, 8, 8]
                              ]
        self.socks = [[1, 2, 1, 2, 1, 3, 2],
                      [10, 20, 20, 10, 10, 30, 50, 10, 20],
                      [50, 20, 30, 90, 30, 20, 50, 20, 90],
                      []
                      ]

    '''
    1. YouTube offers different playback speed options for users. This allows users to increase or decrease the speed of 
    the video content. Given the actual duration and playback speed of the video, calculate the playback duration of the 
    video.
    Examples
    playback_duration("00:30:00", 2) ➞ "00:15:00"
    playback_duration("01:20:00", 1.5) ➞ "00:53:20"
    playback_duration("51:20:09", 0.5) ➞ "102:40:18"
    '''

    @staticmethod
    def convert_time(time, speed):
        hours = time[0]
        minutes = time[1]
        seconds = time[2]

        real_hours, real_minutes, real_seconds = 0, 0, 0

        if int(hours // speed) < 1:
            real_minutes += hours / speed
        else:
            real_hours += hours / speed

        if int(minutes / speed) > 60:
            real_hours += (minutes / speed) // 60
            minutes = minutes % 60
            real_minutes += minutes
        else:
            real_minutes += minutes // speed

        if int(seconds / speed) > 60:
            real_minutes += (seconds / speed) // 60
            seconds = seconds % 60
            real_seconds += seconds
        else:
            real_seconds += seconds // speed

        return str(int(real_hours)) + ":" + str(int(real_minutes)) + ":" + str(int(real_seconds))

    def playback_duration(self):
        for tup in self.duration_speed:
            time = [int(x) for x in tup[0].split(":")]
            speed = tup[1]
            realtime_duration = self.convert_time(time, speed)

            print(f'playback_duration({tup}) -> {realtime_duration}')

    def ques1(self):
        self.playback_duration()

    '''
    2. We needs your help to construct a building which will be a pile of n cubes. The cube at the bottom will have a 
    volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.
    Given the total volume m of the building, can you find the number of cubes n required for the building?
    
    In other words, you have to return an integer n such that:
    n^3 + (n-1)^3 + ... + 1^3 == m
    Return None if there is no such number.
    Examples
    pile_of_cubes(1071225) ➞ 45
    pile_of_cubes(4183059834009) ➞ 2022
    pile_of_cubes(16) ➞ None
    '''

    @staticmethod
    def quadratic_eqn(a, b, c):
        D = b ** 2 - 4 * a * c

        if D < 0:
            return None
        else:
            return (-1 * b + math.pow(D, 0.5)) / 2 * a

    def pile_of_cubes(self):
        for volume in self.volumes:
            c = -2 * math.pow((volume), 0.5)
            a = 1
            b = 1
            n = self.quadratic_eqn(a, b, c)

            print(f'pile_of_cubes({volume}) -> {int(n)}')

    def ques2(self):
        self.pile_of_cubes()

    '''
    3. A fulcrum of a list is an integer such that all elements to the left of it and all elements to the right of it 
    sum to the same value. Write a function that finds the fulcrum of a list.
    To illustrate:

    find_fulcrum([3, 1, 5, 2, 4, 6, -1]) ➞ 2
    // Since [3, 1, 5] and [4, 6, -1] both sum to 9
    
    Examples
    find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]) ➞ 4
    find_fulcrum([9, 1, 9]) ➞ 1
    find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]) ➞ 0
    find_fulcrum([8, 8, 8, 8]) ➞ -1
    '''

    def find_fulcrum(self):
        for lst in self.fulcrum_lists:
            for i in range(1, len(lst) - 1):
                if sum(lst[0:i]) == sum(lst[i + 1:]):
                    element = lst[i]
                    break
                else:
                    element = -1

            print(f'find_fulcrum({lst}) -> {element}')

    def ques3(self):
        self.find_fulcrum()

    '''
    4. Given a list of integers representing the color of each sock, determine how many pairs of socks with matching 
    colors there are. For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and 
    one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.
    Create a function that returns an integer representing the number of matching pairs of socks that are available.
    
    Examples
    sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3
    sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) ➞ 4
    sock_merchant([]) ➞ 0
    '''

    def sock_merchant(self):
        for sock_list in self.socks:
            sock_list.sort()
            pairs = 0
            first_index = 0
            step = 2
            for i in range(first_index, len(sock_list) - 1, step):
                if sock_list[i] == sock_list[i + 1]:
                    pairs += 1
            print(f'sock_merchant({sock_list}) -> {pairs}')

    def ques4(self):
        self.sock_merchant()

    '''
    5. Create a function that takes a string containing integers as well as other characters and return the sum of the 
    negative integers only.

    Examples
    negative_sum("-12 13%14&-11") ➞ -23
    # -12 + -11 = -23
    
    negative_sum("22 13%14&-11-22 13 12") ➞ -33
    # -11 + -22 = -33
    '''
