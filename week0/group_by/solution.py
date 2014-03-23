import collections

def count_words(sentence):
    return collections.Counter(sentence)

def groupby(func, seq):
    s = list(map(func,seq))
    dictionary = count_words(list(map(func,seq)))
    for key in dictionary:
        result = []
        for i in range(0, len(seq)):
            if key == s[i]:
                result.append(seq[i])
        dictionary[key] = result
    return dictionary
