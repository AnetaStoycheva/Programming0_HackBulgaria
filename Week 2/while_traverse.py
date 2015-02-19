books = ["Learn You a Haskell", 
         "The Healthy Programmer",
         "Code Complete",
         "The Pragmatic Programmer",
         "Pro Git",
         "Introduction to Algorithms",
         "Concrete Mathematics"]

start_index = 0 # indeks, ot kojto 6te se dvijim
end_index = len(books) # dyljinata na knigite, t.e. broqt im

while start_index < end_index:
	a = books[start_index]
	print(a)
	start_index += 1