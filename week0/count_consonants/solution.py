def count_consonants(string):
    return len(list(filter(lambda x: x in 'bcdfghjklmnpqrstvwxz' + 'bcdfghjklmnpqrstvwxz'.upper(),string)))