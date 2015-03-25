def string_to_char_list(string):
    result = []

    for ch in string:
        result = result + [ch]

    return result

# print(string_to_char_list("Python"))


def char_list_to_string(char_list):
    result = ""

    for ch in char_list:
        result += ch

    return result

# print(char_list_to_string(['P', 'y', 't', 'h', 'o', 'n']))


# print(string_to_char_list(char_list_to_string("Python")))  # vry6ta sy6toto


def change_string(index, ch, string):

    char_list = string_to_char_list(string)

    char_list[index] = ch

    return char_list_to_string(char_list)

# print(change_string(0, "A", "ani"))
# print(change_string(7, '8', "book"))  # index out of range! trqbva da se proverqva len!
# print(change_string(3, '8', 'The_plaYbook'))


def reverse(items):
    result = []

    for item in items:
        result = [item] + result

    return result


def str_reverse(string):
    char_list = string_to_char_list(string)
    char_list = reverse(char_list)

    # return char_list -> vry6ta gi v spisyk ot stringove
    return char_list_to_string(char_list)

# print(str_reverse("Annie"))  # tuk ne6to ne raboti!!!
print(str_reverse("kamila"))
print(str_reverse("kapak"))
print(str_reverse(""))
