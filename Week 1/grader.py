ocenka = int(input("Kolko to4ki ima tozi u4enik? "))

if 0 <= ocenka <= 50:
	print('Slab 2')
elif 51 <= ocenka and ocenka <= 60:
	print('Sreden 3')
elif 61 <= ocenka and ocenka <= 70:
	print('Dobyr 4')
elif 71 <= ocenka and ocenka <= 80:
	print("mn dobyr 5")
elif 81 <= ocenka and ocenka < 100:
	print('Otli4en 6')
elif ocenka == 100:
	print('Mnogo Otli4en 7')
else:
	pass