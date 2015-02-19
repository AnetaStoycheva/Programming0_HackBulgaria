from random import randint

N = int(input('Daj chislo: ')) # броя на страните на зарчето
dice = randint(1, N) # ако страните Ен са 6, то dice може да е между 1 и 6
print('Padna se:')
print(dice)

