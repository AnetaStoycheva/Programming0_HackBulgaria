def setify(a):

    result = []

    for element in a:
        if element not in result:
            result.append(element)

    return result


def second_largest(numbers):

    if len(setify(numbers)) < 2:
        return False

    result = setify(sorted(numbers))

    return result[-2]


def main():

    print(second_largest([]))
    print(second_largest([2, 1]))
    print(second_largest([5, 5]))
    print(second_largest([100, 100, 90]))
    print(second_largest([100, 100, 102, 102, 90, 85, 102]))
    print(second_largest([100]))


if __name__ == '__main__':
    main()
