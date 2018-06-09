#!\usr\bin\env python3

"""
ME 499: Lab 2
Samuel J. Stumbo
20 April 2018

Estimate Pi Function
This function estimates a value of pi using an infinite series. Srinivasa Ramanujan found this
infinite series. Atta boy.

"""
from math import pi, factorial as fac, sqrt
def estimate_pi():
    k = 0
    pie = 0
    newterm = 1
    while newterm > 1e-15:
        newterm_1 = (2*sqrt(2)/9801)
        newterm_2 = fac(4*k) * (1103 + 26390 * k)
        newterm_3 = ((fac(k)) ** 4 ) * 396 ** (4 * k)
        newterm = newterm_1 * newterm_2 / newterm_3
        pie += newterm
        k += 1
    return (pie ** (-1))

print(estimate_pi())
print(pi)