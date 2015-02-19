n = int(input('A number: '))

counter = 0
imena = []

while counter < n:
	name = input('A name: ')
	imena.append(name)
	counter += 1

print(sorted(imena))

# ili:

# imena.sort()
# print(imena)
