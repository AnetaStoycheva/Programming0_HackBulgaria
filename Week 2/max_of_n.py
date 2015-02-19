n = int(input('A number: '))

start = 0
numbers = []

while start < n:
    number = int(input('adhjgs: '))
    numbers = numbers + [number] # dobavq 4isloto v kraq na spisyka
    # ili numbers.append(number)
    start +=1

current_max = numbers[0]

for a in numbers:
    if a > current_max:
        current_max = a

print(current_max)