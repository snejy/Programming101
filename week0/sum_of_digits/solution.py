def sum_of_digits(number):
    number=abs(number)
    return sum(list(map(int, list(str(number)))))
