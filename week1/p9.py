import string

def pangrams(text):
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for c in text:
        if c in d:
            d[c] += 1
    for value in d.values():
        if value == 0:
            return 'not pangram'
    return 'pangram'


print(pangrams('We promptly judged antique ivory buckles for the prize'))