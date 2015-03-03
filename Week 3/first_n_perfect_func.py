a_number = int(input('A number: '))


def is_perfect(n):
	spisyk_deliteli = []

	for a in range(1, n):
		if n % a == 0:
			spisyk_deliteli.append(a)

	suma_deliteli = sum_ints(spisyk_deliteli) # vikame f-qta sum_ints s parametyr gotoviqt ve4e spisyk i rezultatyt go prisvoqvame na promenliva

	return n == suma_deliteli


def sum_ints(numbers): # tazi f-ciq 6te si raboti, ni6to 4e sme q napisali po-nadolu

	suma = 0
	for a in numbers:
		suma += a
	return suma


def first_n_perfect(broj_chisla):
	broq4 = 0
	perf = 1 # moje da po4vame sys 6, za6toto znaem, 4e to e pyrvoto ;)
	while broq4 < broj_chisla:
		if is_perfect(perf) == False:
			pass

		else:
			print('The number ' + str(perf) + ' is perfect!')
			broq4 += 1 # uveli4avame broq4a tuk, za da pazi broq samo na namereniete perfektni 4isla

		perf += 1

first_n_perfect(a_number)
