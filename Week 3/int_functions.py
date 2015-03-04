def reverse_int(n):
	
	result = 0
	
	while n != 0:
		last_digit = n % 10
		result = result * 10 + last_digit # trqbva da e tuk!!!

		n = n // 10

	return result

print(reverse_int(123))


def sum_digits(n):

	suma = 0

	while n != 0:
		last_digit = n % 10
		suma += last_digit

		n = n // 10

	return suma

print(sum_digits(123))


def product_digits(n):

	product = 1 # proizvedenie 

	while n != 0:
		last_digit = n % 10
		product = product * last_digit

		n = n // 10

	return product

print(product_digits(123))
