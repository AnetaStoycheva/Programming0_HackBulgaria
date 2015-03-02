n = int(input('A number: '))
divisors = 0

for a in range(1, n):
	if n % a == 0:
		divisors = divisors + a

if divisors == n:
	print('The number is pefrect! :)')
else:
	print('The number is not perfect.')