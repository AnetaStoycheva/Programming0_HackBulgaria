a = int(input('Dolna granica:'))
b = int(input('Gorna granica:'))
x = int(input('Dr chislo:'))

if x == a:
	print('The number is equal to the lower bound of the interval')
elif x == b:
	print('The number is equal to the upper bound of the interval')
elif a < x and x < b:
	print("The number is in the interval")
elif x < a:
	print("The number is outside the interval, x < a")
elif x > b:
	print("The number is outside the interval, x > b")
else:
	pass

