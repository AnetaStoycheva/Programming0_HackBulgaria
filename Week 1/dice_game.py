from random import randint

strani_zar = int(input("Napi6i strani na zara:"))
player_1 = input("What's your name?:")
player_2 = input("What's your name?:")

pl1 = randint(1, strani_zar)
pl2 = randint(1, strani_zar)

if pl1 > pl2:
	print(pl1)
	print(player_1)
elif pl1 == pl2: # Da ne izpusna nqkoj slu4aj!
	print(pl1)
	print('Ravni ste!')
else:
	print(pl2)
	print(player_2)
