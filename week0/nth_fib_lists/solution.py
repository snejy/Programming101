def nth_fib_lists(listA, listB, n):
    if len(listA) == 0 and len(listB) == 0:
        return []
    if n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        return  nth_fib_lists(listA, listB, n - 2) + nth_fib_lists(listA, listB, n - 1)