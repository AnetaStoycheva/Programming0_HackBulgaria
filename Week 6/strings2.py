def string_to_char_list(string):
    result = []

    for ch in string:
        result = result + [ch]

    return result

print(string_to_char_list("Python"))


def char_list_to_string(char_list):
    result = ""

    for ch in char_list:
        result += ch

    return result

print(char_list_to_string(['P', 'y', 't', 'h', 'o', 'n']))


# print(string_to_char_list(char_list_to_string("Python")))


def change_string(index, ch, string):

    char_list = string_to_char_list(string)

    char_list[index] = ch

    return char_list_to_string(char_list)


def reverse(items):
    result = []

    for item in items:
        result = [item] + result

    return result


def str_reverse(string):
    char_list = string_to_char_list(string)
    char_list = reverse(char_list)

    return char_list_to_string

print(str_reverse("Annie"))  # tuk ne6to ne raboti!!!
