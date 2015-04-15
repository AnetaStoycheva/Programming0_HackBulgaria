# n_trips = int(input('Брой пътувания: '))
# n_buses = int(input('Брой използвани превозни средства: '))

def city_transport(n_trips, n_buses):

	ticket = 1
	card = 23
	card_all = 50

	if n_buses > 1:

		if n_trips >= card and n_trips < card_all:
			print('За теб е по-добре да си купyваш билетче всеки път!')
		elif n_trips >= card_all:
			print('За теб е по-добре да си купиш карта за цяла градска мрежа!')
		else:
			print('За теб е по-добре да си купуваш билетче всеки път! Но не забравяй! ;)')

	elif n_buses == 1:
		if n_trips < card:
			print('За теб е по-добре да си купуваш билетче!')
		else:
			print('Купи си карта за 1 линия!')

city_transport(30, 2)
	




