def board_to_string(board):

    result = ''

    for element in board:
        for item in element:
            result += '| ' + item + ' '

        result += '|' + '\n'

    return result[0:-1]  # za da ne izkarva posledniq simvol/kojto e za nov red

# print(board_to_string([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]))
print(board_to_string([["X", "O", "#"], ["X", "X", "X"], ["#", "#", "#"]]))
