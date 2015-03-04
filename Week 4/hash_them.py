def hash_them(keys, values):

	dictionary = {}

	for index in range(0, len(keys)): # ot 0-la e zaradi 0-viq indeks

		if index >= len(values):
			dictionary[keys[index]] = None

		else:
			dictionary[keys[index]] = values[index]

	return dictionary

print(hash_them(["Ivan", "Maria"], [1, 2]))
