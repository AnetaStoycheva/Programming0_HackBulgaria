n = int(input('A number: '))
reversed_n = 0

# Тъй като свеждаме 'n' до нула, ще си запазим числото в още 1 променлива, за да го сравним накрая с обърнатото число (ina4e gubim stojnostta mu)
non_reversed = n

while n != 0:
    last_digit = n % 10
    reversed_n = reversed_n * 10 + last_digit

    n = n // 10

# print(reversed_n)

if non_reversed == reversed_n:
    print('The number ' + str(non_reversed) + ' is palindrom.')
else:
    print('The number ' + str(non_reversed) + " isn't palindrom.")