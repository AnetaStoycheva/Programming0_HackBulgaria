n = int(input('A number: ')) # zada4a za n!

start = 1
total = 1

# if n == 0:
#	 print('0! = 1')

while start <= n:
	total = total * start
	start += 1

print(total)


