#!/usr/bin/env python3#
# -*- coding: utf-8 -*-

"""
****************************
    ME 499 Spring 2018
        Lab_4 Test Program
        4 May 2018
    Samuel J. Stumbo
****************************
"""
"""
This program tests the functionality of 'shapes' and 'complex'. 
"""

from complex import Complex
from shapes import Rectangle, Circle
import random


# Test attributes of the circle class
c = Circle(1.2)
a = c.area()
p = c.perimeter()
d = c.diameter()

# Test attributes of rectangle class
r =Rectangle(3, 4)
a2 = r.area()
p2 = r.perimeter()

print(a, '    ', p, '     ', d, '     ', a2, '       ', p2)


# Test attributes of complex class
# count = 0
# complex_array = []
# for i in range (100):
#     real = 10 * random.random()
#     imag = -15 * random.random()
#     check_py = (complex(real, imag))
#     check_me = (Complex(real, imag))
#     complex_array[i][0].append(real)
#     complex_array[i][1].append(imag)
#     if check_py != check_me:
#         count += 1
#         #print(check_py, '     ',  check_me)

a = Complex()
b = Complex(1.,-2.13)

print(a + b)
print(a - b)
print(1 + a)
print(a + 1)
print(b.re, b.im)


