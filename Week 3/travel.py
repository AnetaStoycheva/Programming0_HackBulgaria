# tova e 'greedy' algorithm za re6avane na zada4ata
def travel_cost(travels): # davame mu spisyk 
	total_sum = 0

	for travel in travels:
		if travel >= 23:
			total_sum += 23
		else:
			total_sum += travel

		if total_sum >= 50:
			return 50

	return total_sum


def travel_cost_shorter(travels): 

	total_sum = 0

	for travel in travels:
		total_sum += min(travel, 23)

	return min(total_sum, 50)
	