def head(a_list):
    return a_list[0]


def last(a_list):
    return a_list[-1]


def tail(a_list):
    return a_list[1:]


def equal_lists(list_1, list_2):

    if len(list_1) == len(list_2):

        if len(list_1) == 0:
            return True

        for a in range(0, len(list_1)):

            if list_1[a] == list_2[a]:
                return True
            else:
                return False

    else:
        return False

# print(equal_lists([1, 2], [1, 2]))
# print(equal_lists([1, 2], [2, 1]))
# print(equal_lists([], []))


def count_item(element, a_list):

    counter = 0

    for a in a_list:
        if a == element:
            counter += 1

    return counter

# print(count_item(5, [1, 2, 3, 4, 5]))
# print(count_item("winter", ["winter", "winter"]))
# print(count_item(False, [True, True]))


def take(n, a_list):
    return a_list[0: n]

# print(take(2, [1, 2, 3, 4, 5]))
# print(take(3, [3, 4, 5, 6, 7, 8]))
# print(take(10, [1]))


def drop(n, a_list):
    return a_list[n: ]

# print(drop(1, [1, 2, 3]))
# print(drop(2, ["Python", "Ruby", "Django", "Rails"]))
# print(drop(10, [1]))


def reverse(a_list):
    
    new_list = []

    for element in a_list:
        new_list = [element] + new_list

    return new_list

# print(reverse(["Speak", "in", "reverse", "you", "must!"]))
# print(reverse([1, 2, 3]))
# print(reverse([]))