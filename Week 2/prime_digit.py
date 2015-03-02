n = int(input('A number: '))

digits = []


while n > 0:
	last_digit = n % 10
	digits = [last_digit] + digits
	n = n // 10

has_prime_digit = False # slagame flagova promenliva!

for last_digit in digits:
	if last_digit in [1, 2, 3, 5, 7]:
		has_prime_digit = True
		break

if has_prime_digit:
	print('At least one prime digit found.')
else:
	print('There is not a prime digit.')
		






