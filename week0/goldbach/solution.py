def goldbach(n):
    result = []
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            result.append(tuple((i,n - i)))
    return result

def is_prime(n):
    return len([x for x in range(1, abs(n)) if abs(n) % x == 0]) == 1