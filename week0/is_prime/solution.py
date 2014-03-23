def is_prime(n):
    return len([x for x in range(1, abs(n)) if abs(n) % x == 0]) == 1
