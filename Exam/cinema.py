def count_0s_in_a_row(cinema, row):

    count_0s = 0

    for element in cinema[row]:
        if element == 0:
            count_0s += 1

    return count_0s

# print(count_0s_in_a_row([[1, 0, 0],
#                         [1, 0, 0],
#                         [1, 1, 0]], 2))  # 1


def find_fullest_row(cinema):

    index = 0
    row_with_min0 = -1
    count0 = len(cinema[0]) + 1

    for row in cinema:

        a = count_0s_in_a_row(cinema, index)

        if count0 > a and a > 0:

            count0 = a
            row_with_min0 = index

        index += 1

    return row_with_min0

# print(find_fullest_row([[1, 1, 1], [1, 0, 0], [0, 1, 1]]))


def order_of_seats(cinema):

    row_index = find_fullest_row(cinema)

    result = []

    while row_index != -1:

        for index in range(0, len(cinema[row_index])):

            if cinema[row_index][index] == 0:
                cinema[row_index][index] = 1
                result.append((row_index + 1, index + 1))

        row_index = find_fullest_row(cinema)

    return result


def main():

    print(order_of_seats([[0, 0, 1], [1, 0, 0], [0, 1, 0]]))
    print(order_of_seats([[1, 1, 1, 0], [1, 0, 1, 0], [0, 0, 0, 0]]))
    print(order_of_seats([[1, 1, 1], [1, 0, 0], [1, 0, 0], [1, 1, 0]]))
    print(order_of_seats([[0, 0], [0, 0], [0, 0]]))
    print(order_of_seats([[1, 1], [1, 1], [1, 1]]))


if __name__ == '__main__':
    main()
