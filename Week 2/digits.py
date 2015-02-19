n_first = int(input('A number: '))
digits = []
n = n_first # pazim n na o6te edno mqsto, za da ne go zagubim pri n = 0 i da mojem da go printirame posle (na 10ti red! - ina4e stava 0)

while n != 0:
	last_digit = n % 10
	digits = [last_digit] + digits # pribavqme poslednata cifra na 4isloto v na4aloto na spisyka, za da ne go reversvame posle
	n = n // 10

print('Списъкът от цифрите на числото ' + str(n_first) + ' e: ' + str(digits))


n = 0
for a in digits:
	n = n * 10 + a

print(n)
