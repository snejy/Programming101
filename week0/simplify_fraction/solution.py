def simplify_fraction(fraction):
    divs = []
    if fraction[0] == 1:
        return (fraction)
    for i in range(2, fraction[0] + 1):
        if fraction[1] % i == 0 and fraction[0] % i == 0:
            divs.append(i)
        else:
            divs.append(1)
    divs.sort()
    return tuple((fraction[0] // divs[-1], fraction[1] // divs[-1]))
