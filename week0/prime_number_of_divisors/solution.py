def is_prime(n):
    return len([x for x in range(1, abs(n)) if abs(n) % x == 0]) == 1

def sum_of_divisors(n):
    return len(list(filter(lambda x: n % x == 0 , range ( 1, n + 1 ))))

def prime_number_of_divisors(n):
    return is_prime(sum_of_divisors(n))

