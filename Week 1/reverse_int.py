# Ако n = 123 - резултатът е 321
# Ако n = 1230 - резултатът пак е 321 - крайните 0-ли не ги броим.

n = int(input('A number: '))

# Получаваме обърнатото число, спазвайки принципа, че ако имаме цифрите а и b
# получаваме числото от тези цифри така: a * 10 + b !!!
# 'a' ще бъде досега обърнатото число, а 'b' е текущата последна цифра на това, което обръщаме

reversed_n = 0

while n != 0:
	last_digit = n % 10
	reversed_n = reversed_n * 10 + last_digit # MNOGO VAJNO!!!

	n = n // 10 # novoto ni 4islo = 4isloto, koeto imame // 10 (pr.: 123 // 10 --> 12)

print("The reversed number is: " + str(reversed_n))



