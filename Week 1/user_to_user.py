a = int(input('Give me a number: '))
b = int(input('Give me a number again: '))

while a <= b:
    print(a)
    a += 1

if a > b:
	a = b
	b = a
	while a <= b:
        print(a)
        a += 1


