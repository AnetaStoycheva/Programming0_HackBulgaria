# {key:value} --> {value: key}
# {'A': 'abc'} --> {'abc':'A'}


def dict_reverse(dictionary):

    new_dictionary = {}

    for key in dictionary:
        value = dictionary[key]
        new_dictionary[value] = key

    return new_dictionary

print(dict_reverse({'A': 'abc', 'B': 'def'}))
