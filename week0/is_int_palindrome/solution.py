def is_int_palindrome(n):
    return str(n) == "".join(reversed(list(str(n))))
