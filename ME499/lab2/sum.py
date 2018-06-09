#!\usr\bin\env python3

"""
ME 499: Lab 2
Samuel J. Stumbo
19 April 2018

SUM Function
This function takes the elements in a list and returns the sum of the numbers.
The exceptions were borrowed from Dr. Smarts example code 'exceptions2'
    """
from math import pi, sin, cos, fsum
def sum_i(l):
    summed = 0
    for i in l:
        try:
            summed += i

        except TypeError:
            return None
        except NameError:
            return None

    return summed

def sum_r(l):
    if len(l) == 1:
        try:
            summed = l[0]
        except TypeError:
            return None
        except NameError:
            return None
    else:
        try:
            summed = l[0] + l[-1] + sum_r(l[1:-1])
        except TypeError:
            return None
        except NameError:
            return None
    return summed

if __name__ == "__main__":
    """Ideas from this test section were borrowed liberally from Dr. Smart's Example code. 
        It was not directly copied, of course."""

    numbers_list = [[1, 1., 1, 10, 20.5, 82, 112313], [12, 1.5, 1.2], [pi, cos(pi), sin(2*pi)]]
    not_numbers_list = [['six', 'two', 'four'], [1, '5', '-1'], [1, 2, 'j']]
    functions = [sum_i, sum_r]

    for f in functions:
        badness = 0
        for i in numbers_list:
            try:
                print(f(i))
            except ValueError:
                badness += 1
            except TypeError:
                badness += 1

        for i in not_numbers_list:
            try:
                print(f(i))
            except ValueError:
                badness += 1

        # else:
        #     print('Must not be a list.')
        print(badness)
    # print(sum_i([1, 2, 3, 4, 5]))
    # print(sum_r([1, 2, 3, 4, 5]))

