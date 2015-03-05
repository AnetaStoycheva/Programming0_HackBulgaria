def get_people_count(activity):

	spisyk = []

	for person in activity:

		if person not in spisyk:

			spisyk.append(person)

	counted_people = len(spisyk)

	return counted_people

print(get_people_count(["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria"]))
