n = int(input('A number: '))

while n != 0:

	last_digit = n % 10 
	print(last_digit)
	n = n // 10 # na 4isloto prisvoqvame samo celo4islenata 4ast,
	# za da mojem otnovo da go delim i da vzemem ostatyka, kojto da printirame
	