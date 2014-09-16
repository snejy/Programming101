def sum_of_digits(number):
    return sum(list(map(int, list(str(abs(number))))))
