import time

today = time.strftime("%A")

if today == 'Friday':
	print('it is friday!')
else:
	print('It is not friday ;( Today is', today)