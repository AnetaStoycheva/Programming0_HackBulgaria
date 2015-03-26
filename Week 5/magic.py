# sq1 = [[23, 28, 21],
#        [22, 24, 26],
#        [27, 20, 25]]

# sq2 = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]


def sum_row(matrix, index):

    # pri index = 0 shte vyrne sum na el ot 1viq spisyk v matricata - 72 // i 6
    return sum(matrix[index])

# print(sum_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0))  # vry6ta 6 za sq2
# print(sum_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))  # vry6ta 15 za sq2
# print(sum_row([[23, 28, 21], [22, 24, 26], [27, 20, 25]], 0))  #vry6ta 72 za sq1 - za 23 + 28 + 21


def sum_col(matrix, index):

    result = 0

    for row in matrix:  # tova 6te sybere 23, 22 // i 27 i 1, 4 i 7
        result += row[index]

    return result

# print(sum_col([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0))  # vry6ta 12 ako indeksyt e 0
# print(sum_col([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))  # vry6ta 15 ako indeksyt e 1


def sum_main_diag(matrix):

    result = 0
    index = 0

    for row in matrix:
        result += matrix[index][index]  # vzima 4isloto na poziciq index (0:0),
        index += 1  # i syotvetno (1:1) i (2:2)

    return result

# print(sum_main_diag([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  #  1 + 5 + 9
# print(sum_main_diag([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))  # 23 + 24 + 25


def sum_second_diag(matrix):

    result = 0
    row_index = 0
    col_index = len(matrix[0]) - 1  # v na4aloto e 2

    for row in matrix:
        result += matrix[row_index][col_index]  # v na4aloto e 4isloto na poziciq (0:2) - t.e. 21 ili 3

        row_index += 1  # taka se pridvijvame ot dqsno na lqvo
        col_index -= 1  # poziciqta ni ve4e e (1:1) - t.e. 24 ili 5

    return result  # vry6ta direktno celiq sbor na 2riq diagonal

# print(sum_second_diag([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))  # 21 + 24 + 27
# print(sum_second_diag([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 3 + 5 + 7


def magic_square(matrix):

    target_sum = sum_main_diag(matrix)  # priemame, 4e tyrsenata suma za sravnenie e na glavniq diag

    if sum_second_diag(matrix) != target_sum:
        return False

    for index in range(0, len(matrix)):  # taka obhojdame po index 0, 1 i 2
        if sum_row(matrix, index) != target_sum:
            return False

    for index in range(0, len(matrix[0])):
        if sum_col(matrix, index) != target_sum:
            return False

    # ako ne sme vlezli v nito edna proverka, koqto da dade gre6ka, zna4i-magic
    return True


sq1 = [[23, 28, 21], [22, 24, 26], [27, 20, 25]]
sq2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print(magic_square(sq1))
print(magic_square(sq2))
