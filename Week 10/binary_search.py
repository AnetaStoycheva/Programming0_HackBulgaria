def bsearch(x, xs):  # Списъкът трябва да е сортиран, ако не е - не работи!

    left = 0
    right = len(xs) - 1

    while left <= right:

        mid = (left + right) // 2

        if xs[mid] == x:
            return True
        elif x < xs[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False

print(bsearch(5, [4, 5, 7, 8, 9, 10, 12, 999]))  # True
print(bsearch(3, [4, 5, 7, 8, 9, 10, 12, 999]))  # False
print(bsearch(5, [4, 5, 5, 5, 7, 8, 9, 10, 12, 999]))  # True
print(bsearch(0, []))  # False
