# dali x se sre6ta v xs, re6eno s rekursiq s dopylnit f-ii


def head(xs):
    return xs[0]


def tail(xs):
    return xs[1:]


def member(x, xs):

    if xs == []:
        return False

    if x == head(xs):
        return True

    return member(x, tail(xs))


def member_recursion(x, xs):

    if xs == []:
        return False

    # dava True or False - t.e. True

    return x == head(xs) or member(x, tail(xs))


print(member_recursion(3, [3, 4, 5, 6]))  # True
print(member_recursion(0, [1, 1, 1, 4]))  # False
print(member_recursion(3, [4, 5, 3, -10, -100]))  # True
