# Генерира числата на Фибоначи


def fib(n):

    fib_numbers = [1, 1]  # tova sa pyrvite 2 4isla ot redicata
    current_index = 1
    counter = 2

    if n == 1:
        return [1]
        counter = 1

    elif n == 2:
        return fib_numbers

    elif n > 2:
        for a in range(2, n + 1):
            a = fib_numbers[n - 1] + fib_numbers[n - 2]
            fib_numbers.append(a)
            counter += 1

    return fib_numbers

    # while len(fib_numbers) < n:
    #   next_fib = fib_numbers[current_index] + fib_numbers[current_index - 1]

    #   fib_numbers = fib_numbers + [next_fib]
    #   current_index += 1

    # return fib_numbers
