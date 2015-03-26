def str_reverse(string):

    new_string = ''

    for element in string:
        new_string = element + new_string

    return new_string

# print(str_reverse("Python"))
# print(str_reverse(""))
# print(str_reverse('kapak'))


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

    for index in range(0, min(n, len(items))):  # zavisi koe stane pyrvo
        result += [items[index]]

    return result

# print(take(4, [1, 2, 3, 4, 5, 6, 7, 7]))
# print(take(0, [1]))


def tail(a_list):
    return a_list[1:]


def str_drop(n, string):

    result = ""

    for index in range(n, len(string)):
        result += string[index]

    return result

# print(str_drop(1, "Annieeto"))
# print(str_drop(-2, "bombi4ka"))  # rezultatyt e interesen (zaradi index -2)


def startswith(search, string):

    return search == string[0: len(search)]

# print(startswith("Py", "Python"))
# print(startswith("py", "Python"))
# print(startswith("baba", "asdbaba"))


def endswith(search, string):

    a = len(string)
    b = len(search)
    start = a - b

    return string[start:] == search

# print(endswith(".py", "hello.py"))
# print(endswith("kapak", "babakapak"))
# print(endswith(" ", "Python   "))
# print(endswith("py", "python"))
# print(endswith("asdfgh", "asd"))


def trim_left(string):

    while startswith(' ', string):
        string = str_drop(1, string)

    return string

# print(trim_left("     Rado  Rado"))


def trim_right(string):
    return str_reverse(trim_left(str_reverse(string)))

# print(len(trim_right("Rado Rado    ")))  # len za da sym sig, 4e nqma ' ' otzad


def trim(string):

    result = trim_left(string)

    result = trim_right(result)  # mnogo vajno -> da prilojim f-tq vyrhu ve4e otrqzaniq otlqvo str

    return result

print((trim("   asda   ")))
print(trim(" spacious    "))
print(trim("no here but yes at end   "))
print(len(trim("                      ")))
print(trim("python"))
