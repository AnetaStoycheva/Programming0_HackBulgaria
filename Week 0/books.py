book1_name = "Pragmatic Thinking and Learning"
book1_price = 30
book_count = 1
book2_name = "Learn You a Haskell"
book2_price = 0
book_count += 1
book3_name = 'The Healthy Programmer'
book3_price = 50
book_count += 1
book4_name = 'Code Complete'
book4_price = 60
book_count += 1
book5_name = 'The Pragmatic Programmer'
book5_price = 20
book_count += 1
book6_name = 'Pro Git'
book6_price = 0
book_count += 1
book7_name = 'Introduction to Algorithms'
book7_price = 80
book_count += 1
book8_name = 'Concrete Mathematics'
book8_price = 100
book_count += 1

print('Всяка книга, която е налична и нейната цена:')
print(book1_name, book1_price)
print(book2_name, book2_price)
print(book3_name, book3_price)
print(book4_name, book4_price)
print(book5_name, book5_price)
print(book6_name, book6_price)
print(book7_name, book7_price)
print(book8_name, book8_price)

print('Цената на всички книги е:')
print((book1_price + book2_price + book3_price + book4_price + book5_price +
  book6_price + book7_price + book8_price))

print('Общият брой на всички книги е:')
print(book_count)

print('След намалението търсената сборна цена ще е:')
print (int((book7_price + book8_price) - (book7_price + book8_price) * 25 / 100))

print('За 150 можем да вземем най-много 5 от всички книги. Те са:')
print(book1_name + ', ' + book2_name + ', ' + book3_name + ', ' + book5_name + ', ' + book6_name)
print('Те общо струват:')
print(book1_price + book2_price + book3_price + book5_price + book6_price)


