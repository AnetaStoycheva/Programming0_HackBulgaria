n = int(input('Edno cqlo chislo: '))


def is_prime(n):

	if n <= 1:
		return False

	for a in range(2, n):
		if n % a == 0:
			return False
	
	return True


def to_digits(n):

	spisyk = []

	while n > 0:

		spisyk.append(n % 10)
		n = n // 10

	return spisyk


cirfite_na_chisloto = to_digits(n)

flag = False
for a in cirfite_na_chisloto:
	if is_prime(a) == True:
		print('Chosloto sydyrja pone 1 prosta cifra.')
		flag = True
		break # za da spre da proverqva o6te sled 1ta prosta cifra

if flag == False:
	print('Izmejdu cifrite na chisloto nqma ni e edna prosta.')
