def sum_of_min_and_max(arr):
    if len(arr) == 0:
        return 0
    arr.sort()
    return arr[0]+arr[-1]
