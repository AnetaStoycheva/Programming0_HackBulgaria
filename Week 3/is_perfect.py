def is_perfect(n):
	spisyk_deliteli = []

	for a in range(1, n):
		if n % a == 0:
			spisyk_deliteli.append(a)

	suma_deliteli = sum_ints(spisyk_deliteli) # vikame f-qta sum_ints s parametyr gotoviqt ve4e spisyk i rezultatyt go prisvoqvame na promenliva

	if n == suma_deliteli:
		return True # ne pi6em 'print', za da moje posle da izpolzvame samata stojnost True, rezultatyt, kogato vikame f-qta
	else:
		return False


	# return n == suma_deliteli --> mojem da go napi6em samo taka na 1 red
	# za6toto n == suma_deliteli samo po sebe si e True ili False (i otpred mu slagame return)


def sum_ints(numbers): # tazi f-ciq 6te si raboti, ni6to 4e sme q napisali po-nadolu

	suma = 0
	for a in numbers:
		suma += a
	return suma

print(is_perfect(20))
print(is_perfect(6))
