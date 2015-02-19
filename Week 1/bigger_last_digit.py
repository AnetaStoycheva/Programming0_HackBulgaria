n = int(input('First number: '))
m = int(input('Second number: '))

if (n % 10) > (m % 10):
	print(n)
elif (n % 10) < (m % 10):
	print(m)
else:
	pass

if (n % 10) == (m % 10):
	if n > m:
		print(n)
	else:
		print(m)
