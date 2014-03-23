def is_increasing(arr):
    return arr == sorted(arr) and len(set(arr)) == len(arr)
