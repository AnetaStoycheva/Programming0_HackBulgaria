person = {} # pravim si prazen re4nik, v kojto 6te zapisvame info za Individa

person["first_name"] = input('First name: ')
person["second_name"] = input('Secon name: ')
person["third_name"] = input('Third name: ')
person["birth_year"] = int(input('When were you born, the year: ')) # za da mojem da vadim
person["current_age"] = 2015 - person["birth_year"] # ne e to4no, ako RDto ne e minalo tazi godina! ima li import za tova?!

print(person)
