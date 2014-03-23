def is_number_balanced(n):
    n = list(str(n))
    if len(n) % 2 == 0 :
        return sum([int(x) for x in n[0:len(n)//2]]) == sum([int(x) for x in n[len(n)//2:len(n)]])
    else:
        return sum([int(x) for x in n[0:len(n)//2]]) == sum([int(x) for x in n[len(n)//2+1:len(n)]])
