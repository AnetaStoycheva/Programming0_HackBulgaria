def taken_name(surname_husband, surname_wife):

    return surname_wife[-(len(surname_husband) + 1): -2] in surname_husband:

print(taken_name("Petrov", "Petrova"))
print(taken_name("Ivanov", "Tsvetanova"))
print(taken_name("Petrov", "Ivanova-Petrova"))
