# https://github.com/HackBulgaria/Programming0-1/tree/master/week6/4-Print-Tic-Tac-Toe
# Tuk e re6enieto po stypkite ot uslovieto


def join(delimiter, items):

    result = ""
    last_index = len(items) - 1

    for index in range(0, last_index):
        item = items[index]
        result = result + item + delimiter

    result += items[last_index]

    return result


# Това е първата стъпка ->
def board_to_string(board):
    result = []

    for row in board:
        stringed_row = join("|", row)
        result += [stringed_row]

    return join("\n", result)

board = [["X", "O", "#"],
         ["X", "X", "X"],
         ["#", "#", "#"]]

result = board_to_string(board)

print("1st step result:")
print("======")
print(result)
print("======")

# ======
# X|O|#
# X|X|X
# #|#|#
# ======


# Това е втората стъпка ->
def board_to_string2(board):  # tuk e ve4e modificirano s praznoto mqsto
    result = []

    for row in board:
        stringed_row = join(" | ", row)
        result += [stringed_row]

    return join("\n", result)

result = board_to_string2(board)

print("2nd step result:")
print("======")
print(result)
print("======")

# ======
# X | O | #
# X | X | X
# # | # | #
# ======


# Това е третата стъпка ->
def board_to_string3(board):  # tuk e i s krejnite steni
    result = []

    for row in board:
        stringed_row = join(" | ", row)
        stringed_row = "| " + stringed_row + " |"
        result += [stringed_row]

    return join("\n", result)

board = [["X", "O", "#"],
         ["X", "X", "X"],
         ["#", "#", "#"]]

result = board_to_string3(board)

print("3rd step result:")
print("======")
print(result)
print("======")

# ======
# | X | O | # |
# | X | X | X |
# | # | # | # |
# ======
