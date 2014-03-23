def is_decreasing(arr):
    return arr == list(reversed(sorted(arr))) and len(set(arr)) == len(arr)
