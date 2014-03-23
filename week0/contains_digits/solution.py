def contains_digits(num, digits):
    return len([x for x in list(digits) if str(x) in str(num)]) == len(digits)
