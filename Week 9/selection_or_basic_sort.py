# vry6ta indexa na naj-malkiq element
def min_element_index(list_numbers):

    min_index = 0
    index = 0

    for number in list_numbers:
        if number < list_numbers[min_index]:
            min_index = index
        index += 1

    return min_index

print(min_element_index([2, 3, 6, 7, -2, -5]))  # 5 (poziciqta na -5)


# selection_sort_that_destroys!!!:
def basic_sort(numbers):

    result = []
    n = len(numbers)

    while len(result) != n:
        minimum = min_element_index(numbers)
        result.append(numbers[minimum])
        del numbers[minimum]

    return result

print(basic_sort([2, 3, 6, 7, 0]))
print(basic_sort([-9, 11, 2, -7, - 13]))
