def loss_or_profit(income, outcome):

    counter = 0

    for element1 in income:
        counter += element1
        # print(counter)

    for element2 in outcome:
        counter -= element2
        # print(counter)

    if counter == 0:
        return '=0'
    elif counter < 0:
        return str(counter)
    else:
        return '+' + str(counter)


def main():

    print(loss_or_profit([1, 2, 3], [3]))
    print(loss_or_profit([10], [20, 30]))
    print(loss_or_profit([10], [10]))
    print(loss_or_profit([4, 4, 5], [10, 1]))
    print(loss_or_profit([], []))
    print(loss_or_profit([], [-6, 8]))
    print(loss_or_profit([-2], [1]))


if __name__ == '__main__':
    main()
