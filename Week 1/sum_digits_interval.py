first_number = int(input('First number: '))
last_number = int(input('Last number: '))

# trbqva da proverim intervalyt - dali e mejdu M i N ili e mejdu N i M
lower_bound = 0
upper_bound = 0

if first_number < last_number:
	lower_bound = first_number
	upper_bound = last_number
else:
	lower_bound = last_number
	upper_bound = first_number

start = lower_bound # obhojdame intervala

while start <= upper_bound:
	first_number = start
	total_sum = 0

	while first_number != 0:
	    digit = first_number % 10
	    total_sum += digit
	    first_number = first_number // 10

	print(total_sum)
	start += 1


