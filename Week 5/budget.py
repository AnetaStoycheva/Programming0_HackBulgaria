def on_budget(books, budget):

	books_to_buy_and_loan = {
		'total_cost': 0,
		'books_on_budget': 0,
		'loan': 0
	}
	
	sorted_books = sorted(books)


	for book in sorted_books:

		# uveli4avame stojnostta, koqto e kym klu4a 'total_cost' na na6iq re4nik
		books_to_buy_and_loan['total_cost'] += book

		if books_to_buy_and_loan['total_cost'] > budget:
			books_to_buy_and_loan['loan'] = books_to_buy_and_loan['total_cost'] - budget

		else:
			books_to_buy_and_loan['books_on_budget'] += 1

	return books_to_buy_and_loan

print(on_budget([0, 10, 100, 5, 3, 8, 25], 35))
