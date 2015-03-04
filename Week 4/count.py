def count_vowels_consonants(word):

	dictionary = {}

	vow = "aeiouyAEIOUY"
	cons = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

	dictionary["vowels"] = 0
	dictionary["consonants"] = 0

	for letter in word:

		if letter in vow:
			dictionary["vowels"] += 1
		elif letter in cons:
			dictionary["consonants"] += 1

	return dictionary

print(count_vowels_consonants("aaaAcccD"))
