a = int(input('Give me a number: ')) # lower bound
b = int(input('Give me second number: ')) # upper bound

while a <= b:

    n = a         # Това е поредното число от интервала
    if n % 2 == 0:
	    print(n)
	    print(str(n) + ' is even.')
    else:
	    print(n)
	    print(str(n) + ' is odd.')

    a += 1 # vseki pyt uveli4avame a s 1, za da ne zaciklim i da mojem da stignem do b