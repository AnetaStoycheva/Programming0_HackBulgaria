n = int(input('A number: '))

total_sum = 0
start = 1

while start <= n:
	if start % 2 == 1:
		total_sum += start
	start += 1
	
print(total_sum)

