def divisors(n):
	deliteli = []
	for a in range(1, n):
		if n % a == 0:
			deliteli.append(a)
	return deliteli

print(divisors(6))