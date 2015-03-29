def board_to_string(board):

    result = ''

    for element in board:
        for item in element:
            result += '| ' + item + ' '

        result += '|' + '\n'

    return result[0:-1]


def string_matrix(width, list_of_strings):

    result = []  # tova 6te mi e matricata(spisyka ot spisyci)
    current_row = []

    for a_list in list_of_strings:

        current_row = a_list[0: width]  # taka reja po-dylgite dumi

        if len(current_row) < width:
            current_row = current_row + ('X' * (width - len(current_row)))

        result.append(current_row)

    return result

print(board_to_string(string_matrix(6, ["python", "gogo", "aloha", "java", "haskell", "rubyOnRails"])))
