from collections import Counter

def Char_count(s):
    return dict(Counter(s))

print(Char_count("kolkata is very good city"))