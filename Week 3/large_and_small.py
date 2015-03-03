n = int(input('A number: '))


def to_digits(n):

	spisyk = []

	while n > 0:
		spisyk.append(n % 10)
		n = n // 10

	return spisyk

a = to_digits(n)

smallest = sorted(a)
largest = reversed(smallest)

def to_number(spisyk):

	chislo = 0
	for a in spisyk:
		chislo = 10 * chislo + a

	return chislo

print(to_number(smallest))
print(to_number(largest))
