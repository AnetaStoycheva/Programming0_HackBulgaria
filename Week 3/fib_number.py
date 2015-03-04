def last_item(list_of_items):
	return list_of_items[len(list_of_items) - 1] # vry6ta posledniq element ot spisyk s elementi


def predi_last(list_of_items):
	return list_of_items[len(list_of_items) - 2] # vry6ta predposledniq /// ili list_of_items[-2] :)


def fib(n):

	if n == 1:
		return [1]

	if n == 2:
		return [1, 1]

	current_fib_numbers = [1, 1]

	while len(current_fib_numbers) < n:

		next_fib = last_item(current_fib_numbers) + predi_last(current_fib_numbers)
		current_fib_numbers.append(next_fib)

	return current_fib_numbers


def count_digits(n):

	result = 0

	while n > 0:
		result += 1
		n = n // 10

	return result # vry6ta broq na cifrite na zadadenoto 4islo (trqbva ni ako 4isloto ne e ednocifreno)


def to_number(numbers): # sybira vsi4ki cisla v 1 4islo, kato konkatenirane

	result = 0

	for a in numbers:
		multiplier = 10 ** count_digits(a) # tova 6te e 10 na stepenta na broq cifri, za da imame pr. 150 +7
		result = result * multiplier + a

	return result


def fib_number(n):
	return to_number(fib(n))


print(fib_number(8))
