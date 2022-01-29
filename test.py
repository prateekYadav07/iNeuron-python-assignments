import random


def is_possible(word_list):

    all_words_list = []
    for text in word_list:
        wl = list(text)
        count = 0
        while count < 6:
            temp_word = ''
            random.shuffle(wl)
            for ch in wl:
                temp_word += ch

            if temp_word not in all_words_list and temp_word != text:
                all_words_list.append(temp_word)
            count += 1

    possible = True
    for temp_word in word_list:
        if temp_word not in all_words_list:
            possible = False

    return possible


N = int(input())
names_list = []

while N > 0:
    word = input()
    names_list.append(word)
    print(names_list)
    N -= 1

possible_or_not = is_possible(names_list)
if possible_or_not:
    print('Possible')
else:
    print("Not Possible")
# print('possible')


# beta = 1
# gamma = 0
# delta = 0
#
# time_in_seconds = int(input())
# # if 2 < time_in_seconds <= 10:
# #     gamma += 1
# #     beta -= 1
# # if 10 < time_in_seconds <= 26:
# #     gamma -= 1
# #     delta += 1
# # if time_in_seconds > 26:
# #     beta += 1
# #
# # print(f"{beta} {gamma} {delta}")
#
# while time_in_seconds > 0:
#     if time_in_seconds<2:
#         time_in_seconds -= 2
#         continue
#     elif 2 < time_in_seconds <= 10:
#         beta -= 1
#         gamma += 1
#         time_in_seconds-=8
#
