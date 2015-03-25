def str_reverse(string):
    new_string = ''

    for element in string:
        new_string = element + new_string

    return new_string
# print(str_reverse("Python"))
# print(str_reverse(""))


def join(delimiter, a_list):
    new_list = ''

    for item in a_list:

        if item != a_list[-1]:
            new_list = new_list + str(item) + str(delimiter)

        else:
            new_list = new_list + str(item)

    return new_list
# print(join("|", [1, 2, 3]))
# print(join("2", ["Radoslav", "Yordanov", "Georgiev"]))
# print(join("\n", ["line1", "line2"]))


def take(n, items):
    result = []

    for index in range(0, min(n, len(items))):
        result += [items[index]]

    return result


def startswith(search, string):

    if search == string[0: len(search)]:
        return True
    else:
        return False
# print(startswith("Py", "Python"))
# print(startswith("py", "Python"))
# print(startswith("baba", "asdbaba"))


def endswith(search, string):

    a = len(string)
    b = len(search)
    start = a - b

    if string[start: ] == search:
        return True
    else:
        return False
# print(endswith(".py", "hello.py"))
# print(endswith("kapak", "babakapak"))
# print(endswith(" ", "Python   "))
# print(endswith("py", "python"))


def tail(a_list):
    return a_list[1:]


def str_drop(n, string):
    result = ''

    for index in range(n, len(string)):
        result += string[index]

    return result


def trim_left(string):

    while startswith(' ', string):
        string = str_drop(1, string)

    return string

print(trim_left("     Rado  Rado"))


def trim_right(string):
    return str_reverse(trim_left(str_reverse(string)))


def trim():

    result = trim_left(string)
    result = trim_right(string)

    return result
