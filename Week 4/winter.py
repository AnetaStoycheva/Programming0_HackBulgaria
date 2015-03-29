def winter_is_coming(seasons):

	# if len(seasons) < 5:
	# 	return False

	past_seasons = 0

	for a in seasons:
		if a == 'winter':
			past_seasons = 0 # ako mina prez winter - zapo4vam otnovo da broq ot 0la

		else:
			past_seasons += 1

	# return past_seasons >= 5 --> tozi red pravi sledva6tite 4 izli6ni :D :D

	if past_seasons < 5:
		return False
	else:
		return True

print(winter_is_coming(["winter", "summer", "summer", "summer", "spring", "spring"]))
print(winter_is_coming(["winter", "summer", "summer", "summer", "spring"]))
print(winter_is_coming(["winter", "summer", "summer", "summer", "spring", "spring", "winter"]))
