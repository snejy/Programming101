def count_vowels(string):
    return len(list(filter(lambda x: x in 'aeoiuyAEOIUY', string)))