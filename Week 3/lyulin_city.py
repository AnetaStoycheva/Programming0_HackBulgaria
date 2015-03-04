def how_many_blocks(blocks): # kato vikame funkciqta napravo vkarvame spisyka s viso4inata na blokovete
	if len(blocks) == 0: # proverqvame da ne bi da sme mu vyveli prazen spisyk
		return 0

	seen = 1 # vinagi vijdame pone pyrviq blok, zatova e 1
	current_max = blocks[0] # priemame, 4e pyrviqt blok, kojto vijdame e naj-visokiqt

	for a in blocks:
		if a > current_max:
			seen += 1
			current_max = a

	return seen

result = how_many_blocks([5, 6, 1, 2, 8]) # 6te vyrne 3 bloka, koito vijdame - 5, 6 i 8
print(result)
