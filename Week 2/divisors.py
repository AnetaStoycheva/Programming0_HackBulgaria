n = int(input('A number: '))
divisors = []

for a in range(1, n):
	if n % a == 0:
		divisors = divisors + [a]

print(divisors)


# divisors_sum = 0
# start = 1
# end = n - 1

# while start <= end:
# 	if n % start == 0:
# 		divisors_sum += start

# 	start += 1
# if divisors_sum == n:
# 	print('Number is perfekt')
# else:
# 	print('Not')

