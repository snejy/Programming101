def prime_factorization(n):
    if is_prime(n):
        return [(n,1)]
    else:
        result=[]
        for i in divisors(n):
            k = 0
            while n % i == 0:
                k=k+1
                if is_prime(n):
                    result.append((n,k))
                    return result
                n=n//i
            result.append((i,k))
    return result

def is_prime(n):
    return len([x for x in range(1, abs(n)) if abs(n) % x == 0]) == 1

def divisors(n):
    return [x for x in range (1, n + 1) if n % x == 0 and is_prime(x)]
