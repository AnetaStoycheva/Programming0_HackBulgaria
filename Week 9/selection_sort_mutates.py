# razmenq nastoq6tiq element sys sledva6tiq
def swap(i, j, items):  # (first_index, second_index, a_list_ofitems)

    temp = items[i]
    items[i] = items[j]
    items[j] = temp


# vry6ta poziciqta na naj-malkiq el v [] ot nqkakva poziciq natam
def min_element_index_from_somewhere(from_index, list_numbers):

    min_index = from_index

    for index in range(from_index, len(list_numbers)):

        if list_numbers[index] < list_numbers[min_index]:
            min_index = index

        index += 1  # ?

    return min_index


# t.e. ako smenim poziciqta - smenqma i rezultata
print(min_element_index_from_somewhere(1, [0, -5000, -100, -8, -900]))  # 1 p-q


def selection_sort_that_mutates(numbers):

    for i in range(0, len(numbers)):

        min_index_from_i = min_element_index_from_somewhere(i, numbers)
        swap(i, min_index_from_i, numbers)

a = [2, 0, -10, 9, -5, 11, 100, -100]
selection_sort_that_mutates(a)
print(a)
