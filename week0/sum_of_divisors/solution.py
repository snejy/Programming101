def sum_of_divisors(n):
    return sum(list(filter(lambda x: n % x == 0 , range ( 1, n+1 ))))
