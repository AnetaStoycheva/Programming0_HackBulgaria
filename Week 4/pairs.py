def count_zero_neighbours(numbers):

	counter = 0
	index = 0

	for a in range(0, len(numbers) - 1): # ako iska da vidi 5to i 6to, a nqma 6to - zatova proverqva do predposlednoto

		if numbers[index] + numbers[index + 1] == 0:
			counter += 1
		
		index += 1

	return counter

print(count_zero_neighbours([1, 2, -2, 0, 0, 5, -5]))


def count_zero_pairs(numbers):

	counter = 0

	for index_1 in range(0, len(numbers)): # vzima poziciqta na vseki element na numbers

		for index_2 in range(index_1, len(numbers)): # vzima poziciqta na elem ot nastoq6tiq do kraq, za da ne se broqt po 2 pyti 3, -3 i -3, 3

			if numbers[index_1] + numbers[index_2] == 0:

				counter += 1

	return counter

print(count_zero_pairs([0, 5, 6, -6, -5])) # vry6ta 3!


def is_prime(n):

	if n < 2:
		return False

	for a in range(2, n):

		if n % a == 0:
			return False

	return True


def prime_pair(numbers):


	for index_1 in range(0, len(numbers)): 

		for index_2 in range(index_1, len(numbers)): 

			if is_prime(numbers[index_1] + numbers[index_2]): # == True

				return True

	# vry6tame False 4ak tuk, za da sme sigurni, 4e sme razgledali vsi4ki dvojki i nito 1 ne e s prosta suma,
	# a ne da sprem sled pyrvata (koqto moje i da ne otg na uslovieto, no nqkoq sledva6ta moje i da otgovarq)
	
	return False

print(prime_pair([1, 2, 3, 4, 5]))
print(prime_pair([2, 4, 6, 10]))
	