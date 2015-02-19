number = int(input('Cqlo 3 cifreno 4islo: '))

c = number % 10
a = number // 100 
b = (number - 100 * a - c) // 10 # s 2 4erti e, za da stane celo4isleno delenie

if a > b and a > c: # ako tova e taka - zna4i a e naj-golqmoto 4islo i izlizam ot if-a
	largest = a

elif a > b and a < c:
	largest = c

elif a < b and b > c:
	largest = b

elif a < b and b < c:
	largest = c

elif a < b and a > c:
	largest = b

elif a > b and b > c: # ako a e naj-golqmo (ot red 7) -> ne me interesuva koe ot b i c e po-golqmo
                      # i tozi red otpada
    largest = a

else:
    pass

print('The largest digit is: ' + str(largest))


# .... pravim podobno ne6to i za smallest_number, sled tova izbirame koj e sredniq i posle:
# max_number = largest * 100 + middle * 10 + smallest
# min_number = smallest * 100 + middle * 10 + largest


smallest = a # priemame, 4e...

if b <= smallest and b <= c:
    smallest = b

if c <= smallest and c <= b:
    smallest = c

print('The smallest digit is: ' + str(smallest))


middle = c

if (largest == c and smallest == b) or (smallest == c and largest == b):
    middle = a
elif (largest == c and smallest == a) or (smallest == c and largest == a):
    middle = b

print('The middle digit is: ' + str(middle))


max_number = largest * 100 + middle * 10 + smallest # MNOGO VAJNO!
min_number = smallest * 100 + middle * 10 + largest # MNOGO VAJNO!

print('Naj-golqmo 4islo sys zadadenite cifri e: ' + str(max_number))
print('A naj-malkoto e: ' + str(min_number))

