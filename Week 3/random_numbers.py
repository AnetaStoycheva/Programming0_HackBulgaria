from random import randint

def generate_random_list(n, start, end):

	spisyk = []

	while n != 0:

		chislo = randint(start, end)
		spisyk.append(chislo)
		n = n - 1
	
	return spisyk

print(generate_random_list(5, 1, 10))

# dyljina_spisyk = n
