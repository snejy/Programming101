def member_of_nth_fib_lists(listA, listB, needle):
    for i in range(1,len(needle)):
        if nth_fib_lists(listA, listB, i) == needle:
            return True        
    else:
        return False

def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n ==  2:
        return listB
    else:
        return  nth_fib_lists(listA, listB, n - 2) + nth_fib_lists(listA, listB, n - 1)
