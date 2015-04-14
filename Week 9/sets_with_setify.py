# da gi re6im bez da promenqme pyrvona4alnite spisyci, t.e. BEZ mutaciq


def setify(a):  # vzima spisyk i vry6ta nov spisyk, v k' Vs el se sre6ta po 1py
    result = []

    for element in a:
        if element not in result:
            result.append(element)

    return result

# print(setify([2, 2, 3, 5, 5, 7, 0, -10, 9, -100, 2, 3]))


def diff(a, b):

    result = []

    for element in setify(a):
        if element not in setify(b):
            result.append(element)

    return setify(result)

print(diff([0, 1, 2, 3, 4, 5], [0, 0, 1, 1, 2, 2, 3, 3]))  # [4, 5]


def union(a, b):  # pravi obedinie na 2ta spisyka, no bez povtarq6ti se

    return setify(a + b)

print(union([0, 0, 0, 0, 0], [1, 2]))  # [0, 1, 2])


def intersection(a, b):  # se4enieto na 2ta spisyka, no bez povtarq6ti se

    result = []

    for element in setify(a):
        if element in setify(b):
            result.append(element)

    return setify(result)

print(setify([0, 1, 1, 5, 5, 6]) == [0, 1, 5, 6])  # True


# vzima 2 spisyka, dekartovo proizvedenie, nov sp
# ot naredenite dvojki (tuple), no setifajnata
def cartesian_product(a, b):

    result = []

    for element in setify(a):
        for elementa in setify(b):
            result.append((element, elementa))

    return setify(result)

print(cartesian_product([0, 1], [1, 0]))  # [(0, 1), (1, 1)])


def diff2(a, b):
    return setify([x for x in a if x not in b])


def union2(a, b):
    return setify(a + b)


def intersection2(a, b):
    return setify([x for x in a if x in b])


def cartesian_product2(a, b):
    return [(i, j) for i in a for j in b]
