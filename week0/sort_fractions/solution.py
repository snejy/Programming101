def sort_fractions(fractions):
    mylist = {}
    for i in range(0,len(fractions)):
        mylist[(fractions[i][0] / fractions[i][1])] = fractions[i]
    keys = sorted(mylist, key = mylist.get)
    array = []
    for i in sorted(keys):
        array.append(mylist[i])
    return array
