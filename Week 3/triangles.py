def is_triangle(a, b, c):
	return a + b > c and a + c > b and c + b > a # n-vo na triygylnika

print(is_triangle(10, 11, 11))
print(is_triangle(1, 11, 12))


from math import sqrt # naj-dobre e da e v na4aloto na fajla

def area(a, b, c):

	# tuk moje otnovo da se proveri za sy6testvuvaneto na triygylnik s taka zadadenite strani - red 15, 22, 23 i 24
	# no ako ne sy6testvuva, 6te vry6ta osven izre4enieto v print-a, i stojnost 0 (trqbva ni za f-qta max_area)

	if a + b > c and a + c > b and c + b > a:

		p = (a + b + c) / 2 # poluperimetyra - ot f-la na Heron
		liceto = sqrt(p * (p - a) * (p - b) * (p - c)) # pak ot f-lata

		return liceto

	else:
		print('Takyv triygylnik ne sy6testvuva! Ne e izpylneno ravenstvoto za tr.')
		return 0 # ako imame 0 shte znaem, 4e nqma takyv tr-k, no i 6te mojem da sravnim liceto mu, koeto 6te e 0 s licata na ostanalite

print(area(10, 11, 12))


def is_pythagorean(a, b, c):

	if a + b > c:
		return a ** 2 + b ** 2 == c ** 2 # imame '==' za6toto gi sravnqvame
	else:
		print('Zadajte drugi strani na triygylnika, tezi ne stavat.')
		return False

print(is_pythagorean(3, 4, 5))
print(is_pythagorean(10, 11, 12))
is_pythagorean(1, 11, 12) # -> napravo 6te izprinti izre4enieto. Ako slojim print(is_pitagoreen) - 6te vurne i None
	

def max_area(triangles):

	current_max = triangles[0] # primame, 4e pyrviqt spisyk sys strani na triygylnici otgovarq na uslovieto ni - da e max

	a = current_max[0] # vzimame si stranata a, poneje q nqmahme dosega (kato parametyr) i taka za b i c
	b = current_max[1]
	c = current_max[2]

	current_max_area = area(a, b, c) # smqtame liceto na 1iq triyg, vikajki f-ciqta area s gotovite ni ve4e a, b i c
	# kato daje ve4e znaem dali te sa naistina strani v edin triygylnik

	for triangle in triangles: # obhojdame vseki 1 ot spisycite sys strani na triyg-ci
		a = triangle[0]
		b = triangle[1]
		c = triangle[2]

		current_area = area(a, b, c)

		if current_area > current_max_area:
            
			current_max_area = current_area
			current_max = triangle

	return current_max

print(max_area([[3, 4, 5], [10, 11, 12]]))
