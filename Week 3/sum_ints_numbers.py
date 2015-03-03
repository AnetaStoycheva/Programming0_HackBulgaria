def divisors(n):
	deliteli = []
	for a in range(1, n):
		if n % a == 0:
			deliteli.append(a)
	return deliteli

def sum_ints(numbers):
	suma = 0
	for a in numbers:
		suma += a
	return suma

print(sum_ints(divisors(6)))


# vtoro re6enie  - bez 2ta funkciq:
# def divisors_sum(n):
# 	deliteli = 0
# 	for a in range(1, n):
# 		if n % a == 0:
# 			deliteli += a
# 	return deliteli

# print(divisors_sum(6))
