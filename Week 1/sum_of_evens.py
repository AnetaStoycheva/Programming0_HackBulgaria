n = int(input('Write a number: '))
total_sum = 0
start = 1

while start <= n:
	if start % 2 == 0:
	    total_sum += start
	    
	start = start + 1

print(total_sum)
