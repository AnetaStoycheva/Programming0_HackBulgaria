p = int(input('A number: '))
# q = p - 2 ili q = p + 2!!! Rado, ako 4ete6 tova - moje da si go dopylni6 v uslovieto na zada4ata:)

def is_prime(n):
	if n == 0 or n == 1:
		return False

	for a in range(2, n):
		if n % a == 0:
			return False

	return True # znaem, 4e n e prosto, ako nikoga ne sme vlezli v if-a na for-a (ako bqhme vlezli - nqma6e da stignem do tozi red, zaradi return)

flagova_promenliva = False # v na4aloto nqmame nito 1 prosto 4islo bliznak, zatova e False, no ako namerim - 6te q napravim True

if is_prime(p) == True:

	if is_prime(p - 2) == True:
		flagova_promenliva = True # namerihme takova 4islo, => promenqme q :)
		print(p)
		print('Просто число близнак на ' + str(p) + ' e: ' + str(p - 2))

	if is_prime(p + 2) == True:
		flagova_promenliva = True
		print(p)
		print('Просто число близнак на ' + str(p) + ' e: ' + str(p + 2))

	if flagova_promenliva == False:
		print('Това просто число няма прости числа близнаци! Тъжно...')

else:
	print(str(p) + ' is not a prime.')
