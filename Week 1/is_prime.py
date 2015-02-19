n = input("Enter a number: ")
n = int(n)

start = 2 # za6toto e pyrvoto prosto
is_prime = True # priemame, 4e e taka

# Специален случай за 1. (i za 0-la)
if n == 1:
    is_prime = False

while start < n:
    if n % start == 0:
        is_prime = False
        break
    start = start + 1

if is_prime: # t.e. if is_prime == True (koeto bi sledvalo da e taka)
    print("It is prime")
else:
    print("It is not prime")
    