def calculate_coins(sumata):

	dictionary = {}

	# sum e f-ciq i ne iskam da q slagam tuk, zatova go promenih na 'sumata'
	a = round(sumata * 100) # round zakryglq, za da imame ot 0.803 -> 80.3 stotinki -> 80 storinki

	stojnosti_pari4ki = [100, 50, 20, 10, 5, 2, 1] # 6te gi obhojdame

	for stojnost in stojnosti_pari4ki:

		dictionary[stojnost] = a // stojnost # vijdame kolko po 100(ili 50, ili 20...) ni trqbvat i gi zapisvame kym syotv im klu4
		a = a - stojnost * dictionary[stojnost]

	return dictionary

print(calculate_coins(6.57)) # malko neugledno, no vse pak - {1: 0, 50: 1, 20: 0, 5: 1, 100: 6, 10: 0, 2: 1}
