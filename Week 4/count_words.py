def count_words(words):

	dictionary = {}

	for word in words:
		if word in dictionary:
			dictionary[word] += 1

		else:
			dictionary[word] = 1

	return dictionary

print(count_words(["words", "are", "meaningful", "words", "words", "are"]))
