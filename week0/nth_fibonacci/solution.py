def nth_fibonacci(n):
    if n <= 0 : 
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
