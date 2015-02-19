from random import randint

total_Ivan = 1001
total_Maria = 1001

turn = 0 # 4etnite 'turn' 6te sa za Mariq, a ne4etnite - za Ivan


while True:

	result = 0 # trqbva da e v while-a, za6toto ina4e resultatite na ivan i Mariq ot vseki 5 posledovat hvyrlqniq se natrupvat

	for a in range(1, 6): # hvyrlqniqta na vseki sa po 5
		result = result + randint(1, 6)

	if turn % 2 == 0:
		if total_Maria < 0:
			total_Maria += result
		elif total_Maria > 0:
			total_Maria = total_Maria - result

		print("Sbora ot 5te hvyrlqniq na zar4eto na Mariq e: " + str(result))
		print("Maria now has: " + str(total_Maria))

		if total_Maria == 0:
			print('Maria wins!')
			break

	else:
		if total_Ivan < 0:
			total_Ivan += result
		elif total_Ivan > 0:
			total_Ivan = total_Ivan - result

		print('Ivan ot 5 pyti ob6to e hvyrlil: ' + str(result))
		print('Ivan sega ima: ' + str(total_Ivan) + ' to4ki.')

		if total_Ivan == 0:
			print('Ivan wins!')
			break

	turn += 1 # ako dosega e hvyrlqla Mariq, sega e red na Ivan
	



	

