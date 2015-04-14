def dict_reverse(dictionary):

    new_dictionary = {}

    for key in dictionary:
        value = dictionary[key]
        new_dictionary[value] = key

    return new_dictionary


def decode_word(encrypted_word, cipher):

    result = ''

    dictionary = dict_reverse(cipher)

    for a in encrypted_word:

        if a in dictionary:
            result += dictionary[a]

        # if we had a problem instead -->
        # else:
        #     return False

    return result


def main():

    print(decode_word("mjriew", {'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'}))  # --> 'python'
    print(decode_word("rpf", {'m': 'p', 'o': 'r', 'g': 'f'}))
    print(decode_word("wfhsftzzuys", {'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'}))
    print(decode_word("bbbbbbbbbbbbbbbbbbbbbbbbbbb", {'a': 'b'}))  # len = 27
    # print(decode_word('aaa', {'s': '8'}))
    # print(decode_word('', {}))
    # print(decode_word('', {'a': ''}))
    # print(decode_word('', {' ': 'a'}))

if __name__ == '__main__':
    main()
