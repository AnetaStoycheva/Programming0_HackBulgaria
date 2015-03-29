def sublist(list1, list2):

    for pozition in range(0, len(list2)):  # obhojdame poziciite v list2

        # tyrsi v list2 mejdu poziciite 'pozition' i 'p-ion' + dylj na spisyka
        if list1 == list2[poztion: (pozition + len(list1))]:

            return True

    return False  # ako sme izlezli ot if-a i for-a i ne sme vyrnali True

print(sublist(['Python'], ['Python', 'Django']))
print(sublist([], ['Python', 'Django']))
print(sublist(['A'], ['bdshgkdjfhgjdfhgjdhf']))
