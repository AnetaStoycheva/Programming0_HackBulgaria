def str_reverse(string):
    new_string = ''

    for element in string:
        new_string = element + new_string

    return new_string


def is_string_palindrom(string):

    result = ''
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for ch in string:
        if ch in letters:
            result += ch

    result = result.lower()

    r = str_reverse(result)  # ot gornata funkciq

    return result == r


print(is_string_palindrom("Az obi4am ma4 i boza"))
print(is_string_palindrom("A Toyota!"))
print(is_string_palindrom("bozaaa"))
print(is_string_palindrom("  kapak!   "))
