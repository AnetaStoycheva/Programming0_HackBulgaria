n = int(input('Give me a number: '))

start = 0
even_count = 0
while start < n:
	number = int(input())

	if number % 2 == 0:
		even_count += 1

	start += 1

print(str(even_count))







