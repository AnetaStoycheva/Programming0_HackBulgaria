niz = input('Input as a string: ')
counter = 0
vowels = 'aeiouyAEIOUY' # vsi4ki glasni v anglijskiq

for a in niz:
	if a in vowels:
		counter += 1

print('В стринга ' + niz + ' броят на гласните е: ' + str(counter))