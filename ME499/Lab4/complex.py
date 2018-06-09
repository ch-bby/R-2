#!/usr/bin/env python3#
# -*- coding: utf-8 -*-

"""
****************************
    ME 499 Spring 2018
        Lab_4 Part 2
        4 May 2018
    Samuel J. Stumbo
****************************
    """

"""
References used:
*****************************
https://stackoverflow.com/questions/13060617/practicing-add-sub-mul-two-complex-number-by-python
http://hplgit.github.io/primer.html/doc/pub/class/._class-readable005.html
think python2
*****************************
"""
from math import pi

class Complex:
    """
    This class is for complex numbers.
    """
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im < 0:
            return '({0} - {1}i)'.format(self.re, abs(self.im))
        if self.im >= 0:
            return '({0} + {1}i)'.format(self.re, self.im)

    def __add__(self, other):
        if type(other) != Complex:
            other = Complex(other)
        r1 = self.re
        i1 = self.im
        r2 = other.re
        i2 = other.im
        real_sum = r1 + r2
        im_sum = i1 + i2

        return Complex(real_sum, im_sum)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if type(other) != Complex:
            other = Complex(other)

        r1 = self.re
        i1 = self.im
        r2 = other.re
        i2 = other.im

        real_sub = r1 - r2
        im_sub = i1 - i2

        return Complex(real_sub, im_sub)

    def __rsub__(self, other):
        return Complex(other - self.re, -self.im)

if __name__ == '__main__':
    a = Complex(1, 2)
    b = Complex(1, -2)
    c = Complex(1.2, 3.4)
    d = Complex(3,4)
    e = Complex()
    print(a)
    print(b)
    print(1.27 - b)
    print(2-a)
    print(1.5 + c)
    print(1.5 + d)
    print(a + b)
    print(b + a)
    print(b + c)


