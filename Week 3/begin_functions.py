def square(x):
	return x ** 2

#print(square(5)) - primer, za proverka samo


def factorial(x):
	proizvedenie = 1
	for a in range(1, x + 1):
		proizvedenie = proizvedenie * a

	return proizvedenie

# print(factorial(5)) - primer


def count_elements(items):
	counter = 0
	for a in items:
		counter += 1

	return counter

# print(count_elements([3, 5, 7, 6, 90])) - za proverka


def member(x, xs):
	for a in xs:
		if a == x:
			return True # ako vyrne ne6to spira da raboti i ne izpylnqva reda s 'return False'
	
	return False # tova 6te se izpylni ako for-a ne e vyrnal True

# print(member('ani', ['fhdf', 'ani', 'hmm', 'dsgdf']))


def grades_that_pass(students, grades, limit):
	minava6ti = []
	index = 0
	for a in grades:
		if a >= limit:
			minava6ti.append(students[index])

		index += 1
		
	return minava6ti

print(grades_that_pass(['S', 'Ac', 'Mk'], [4.7, 5.4, 5.1], 5))
