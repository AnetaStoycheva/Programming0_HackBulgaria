def max_score(beers, fries):

	beers = sorted(beers)
	fries = sorted(fries)

	counter = 0
	result = 0

	for a in beers:

		result += a * fries[counter]
		counter += 1

	return result

print(max_score([10, 11], [1, 5]))
print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))
