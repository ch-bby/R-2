#!\bin\usr\env python3

# Reading notes for week 3
# Dictionaries

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('parrot')
print(h.get('a', 0))
print(h.get('b', 0))

def print_hist(h):
    for c in h:
        print(c, h[c])
print('\n', '\n')

print_hist(h)
print('\n', '\n')

# This prints the dictionary in sorted order using the built-in 'sorted' function
for key in sorted(h):
    print(key, h[key])

# def reverse_lookup(d, v):
#     for k in d:
#         if d[k] == v:
#             return k
#     raise LookupError()
#
# key =  reverse_lookup(h, 3)
# print(key)

# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#     else:
#         inverse[val].append(key)
#     return inverse

#inverse = invert_dict(hist)

def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

known = {0:0, 1:1}

print(fibonacci(2))

# Class examples:
