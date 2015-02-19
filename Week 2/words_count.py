word = input('A word: ')
n = int(input('A number: '))

counter = 0
broq4 = 0

while counter < n:
	duma = input('Chete po 1 duma na red: ')
	counter += 1

	if duma == word:
		broq4 += 1

print(broq4)
