# tova vaji samo za spisyci
def swap(i, j, items):  # (first_index, second_index, a_list_ofitems)

    temp = items[i]
    items[i] = items[j]
    items[j] = temp

# nqmame return za6toto promenqme items i promenqme i a-to

a = [1, 2, 3, 4, 5]
swap(0, 1, a)
print(a)
