# a --> selection_sort --> b (не го мутира, а връща нов списък)
# [0, 5, 7, 8, -2, -3] --> [-3, -2, 0, 5, 7, 8]


def diff(list1, list2):

    result = []

    for a in list1:
        if a not in list2:
            result.append(a)

    return result

print(diff([0, 1, 3, 5], [0, 1]))  # връща разликата - [3, 5]


# взима индекса на най-малкия елемент, неизползван досега
def min_index_without_used(list_numbers, from_index):  # items, used

    unused_indexes = diff(range(0, len(list_numbers)), from_index)
    min_index = unused_indexes[0]

    for index in unused_indexes:
        if list_numbers[index] < list_numbers[min_index]:
            min_index = index

    return min_index

    # for index in range(from_index, len(list_numbers)):
    #     if list_numbers[index] < list_numbers[min_index]:
    #         min_index = index

    # return min_index


def selection_sort(a_list):

    result = []
    used_indexes = []

    while len(result) != len(a_list):
        min_index = min_index_without_used(a_list, used_indexes)
        used_indexes.append(min_index)
        result.append(a_list[min_index])

    return result

print(selection_sort([1, 4, 7, -9, 7, 4, -100, -3]))
