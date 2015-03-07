def sublist(list1, list2):

	for poziciq in range(0, len(list2)): # obhojdame poziciite v list2

		if list1 == list2[poziciq: (poziciq + len(list1))]: # tyrsi v list2 mejdu poziciite 'poziciq' i 'p-iq' + dylj na spisyka

			return True

	return False # ako sme izlezli ot if-a i for-a i ne sme vyrnali True

print(sublist(['Python'], ['Python', 'Django']))
print(sublist([], ['Python', 'Django']))
print(sublist(['A'], ['bdshgkdjfhgjdfhgjdhf']))
