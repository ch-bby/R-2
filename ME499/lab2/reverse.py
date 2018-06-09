#!/usr/bin/env python3
"""
ME 499: Lab 2
Samuel J. Stumbo
19 April 2018

Reverse Function

Two functions: one iterative, one recursive, that takes a list and reverses its order
    """

from math import pi, sin, cos

# A function that reverses the order of a list: iterably (if that's a word)
# I got the idea from Lutz's, "Learning Python." 5th edition pg. 420 (seriously)

def reverse_i(l1):
    ffuts = []                      # This is stuff backwards... if you were wondering
    for i in range(len(l1)):
        ffuts.append(l1[-i-1])
    return ffuts

# A function that reverses the order of a list: recursively
# Credit to google --> stack overflow solution: This provided syntax corrections to what I already had.
def reverse_r(l1):
    ffuts = []
    if len(l1) == 1:
        return l1
    else:
        return l1[-1:] + reverse_r(l1[:-1])



if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(reverse_i(l1))
    print(reverse_r(l1))

    good_list = [[1, 1., 1, 10, 20.5, 82, 112313], [12, 1.5, 1.2], [pi, cos(pi), sin(2 * pi)], ['dog', 'cat', 'manual', 'sick bruh']]
    bad_list = [('six', 'two', 'four'), (1, '5', -1), (1, 2, 'j')]
    functions = [reverse_i, reverse_r]

    for f in functions:
        badness = 0
        for i in good_list:
            try:
                print(f(i))
            except ValueError:
                badness += 1
            except TypeError:
                badness += 1

        for i in bad_list:
            try:
                print(f(i))
            except ValueError:
                badness += 1
            except TypeError:
                badness += 1
            except SyntaxError:
                badness += 1
        print(badness)
