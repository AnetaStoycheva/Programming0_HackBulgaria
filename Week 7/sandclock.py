# priemame, 4e n vinagi e ne4etno 4islo
# priemam, 4e trqbva da e ograden s '.' otstrani


def sands_of_time(n):

    star = "*"
    dot = "."
    number_dots = 1
    number_stars = n

    mirror_reverse = False

    for a in range(0, n):

        print((number_dots * dot) + (star * number_stars) + (number_dots * dot))

        if mirror_reverse:
            number_stars += 2
            number_dots -= 1

        else:
            number_dots += 1
            number_stars -= 2

        if number_stars == 1:
            mirror_reverse = True  # ob6ty6tame 4asovnika

sands_of_time(5)  # samo vikame f-qta, ne q printim, za6toto vry6ta None
sands_of_time(7)
sands_of_time(11)

# n = 5 ->
# .*****.
# ..***..
# ...*...
# ..***..
# .*****.

# n = 7 ->
# .*******.
# ..*****..
# ...***...
# ....*....
# ...***...
# ..*****..
# .*******.
