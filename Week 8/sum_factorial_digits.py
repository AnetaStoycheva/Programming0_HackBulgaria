def factorial(n):

    result = 1

    if n < 0:
        return "Nqma!"

    for a in range(1, n + 1):
        result *= a

    return result


def to_digits(n):

    result = []

    while n > 0:
        last_digit = n % 10
        result.append(last_digit)
        n = n // 10

    return result


def sum_num_fact(n):

    result = 0

    for digit in to_digits(n):
        result += factorial(digit)

    return result


print(sum_num_fact(111))
print(sum_num_fact(145))
print(sum_num_fact(999))
