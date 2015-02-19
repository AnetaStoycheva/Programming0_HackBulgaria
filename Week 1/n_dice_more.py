from random import randint

# pravim N da e int, za6toto input po default vry6ta string
N = int(input('Enter sides: '))

result_1 = randint(1, N)
print('Pyrvo hvyrlqne:', result_1)
result_2 = randint(1, N)
print('Vtoro hvyrlqne:', result_2)
result_3 = randint(1, N)
print('Treto hvyrlqne:', result_3)
print('Sbor ot hvyrlqniqta:', result_1 + result_2 + result_3)
