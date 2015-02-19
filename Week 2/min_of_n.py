n  = int(input(' A number: '))

counter = 0
min_number = None

while counter < n:
	drugo_n = int(input('Sledva6tite ' + str(n) + ' reda: '))
	
	if min_number is None or drugo_n <= min_number: 
		min_number = drugo_n

	counter += 1

print(min_number)

