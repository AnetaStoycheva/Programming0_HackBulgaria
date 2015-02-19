n = input('Give me a number: ')
n = int(n)

# na vsqko zavyrtane na cikyla j pribavqme po 1,
# sled koeto q printim (v neq napravo pazim cqlata suma dosega)

total_sum = 0 

start = 1 # dyrjim porednoto 4islo ot 1 do n

while start <= n:
	total_sum = total_sum + start
	start += 1

print('The sum of numbers from 1 to ' + str(n) + ' is: ' + str(total_sum))
	