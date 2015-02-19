a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
oper = input("Choose from: '+', '-', '*' or '/' ")

if oper == '+':
	print('Result is:', a + b)
elif oper == '-':
	print(a - b)
elif oper == '*':
	print(a * b)
elif oper == '/':
	print(a / b)
else:
	print("I don't know this oper.")

