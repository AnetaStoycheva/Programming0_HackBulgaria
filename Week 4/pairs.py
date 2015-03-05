def count_zero_neighbours(numbers):

	counter = 0
	index = 0

	for a in range(0, len(numbers) - 1): # ako iska da vidi 5to i 6to, a nqma 6to - zatova proverqva do predposlednoto

		if numbers[index] + numbers[index + 1] == 0:
			counter += 1
		
		index += 1

	return counter

print(count_zero_neighbours([1, 2, -2, 0, 0, 5, -5]))
