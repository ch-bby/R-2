#!/usr/bin/env python3#
# -*- coding: utf-8 -*-

"""
****************************
    ME 499 Spring 2018
        Lab_5 complex.py
        17 May 2018
    Samuel J. Stumbo
****************************
    """

"""
References used:
*****************************
https://docs.python.org/3/library/unittest.html
*****************************
"""
from math import pi
import complex_test
import unittest

class Complex:
    """
    This class is for complex numbers.
    """
    def __init__(self, re=0, im=0):
        # add check for string
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

        if type(self) != Complex:
            self = Complex(self)

        r1 = self.re
        i1 = self.im
        r2 = other.re
        i2 = other.im

        real_sub = r1 - r2
        im_sub = i1 - i2

        return Complex(real_sub, im_sub)

    def __rsub__(self, other):
        return Complex(other - self.re, -self.im)

    def __mul__(self, other):
        if type(other) != Complex:
            other = Complex(other)
        re_1 = self.re
        re_2 = other.re
        im_1 = self.im
        im_2 = other.im
        re_mul = re_1 * re_2 - im_1 * im_2
        im_mul = re_1 * im_2 + re_2 * im_1
        return Complex(re_mul, im_mul)

    def __neg__(self):
        neg_real = -self.re
        neg_im = -self.im
        return Complex(neg_real, neg_im)

    def __rmul__(self, other):
        if type(other) != Complex:
            other = Complex(other)
        return other * self

    def __pow__(self, power):
        if power == 4:
            return self*self*self*self
        if power == 3:
            return self*self*self

        if power == 2:
            return self*self

        if power == 1:
            return self

        if power == 0:
            return 1

    def __invert__(self):
        return self.conj()

    def conj(self):
        real = self.re
        imag = -self.im
        return Complex(real, imag)


    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Complex(other)

        num = self
        den = other
        conju = other.conj()
        num_new = num * conju
        den_new = den * conju
        re_num = num_new.re
        re_den = den_new.re
        re_prt = re_num / re_den
        im_num = num_new.im
        im_den = den_new.im
        im_prt = im_num / re_den
        return Complex(re_prt, im_prt)

    def __rtruediv__(self, other):
        if type(other) != Complex:
            other = Complex(other)

        return other*~self / (self * ~self)




# My sqrt function
def sqrt(n):
    if isinstance(n, float) or isinstance(n, int):
        if n > 0:
            return n ** .5

    if isinstance(n, float) or isinstance(n, int) and n < 0:
        n = Complex(n)

    # Used wikipedia reference for this
    if isinstance(n, Complex):
        a = n.re
        b = n.im
        gamma = ((a + ((a ** 2 + b ** 2) ** .5)) / (2)) ** .5
        if b < 0:
            delta = -((-a + ((a ** 2 + b ** 2) ** .5)) / (2)) ** .5

        else:
            delta = ((-a + ((a ** 2 + b ** 2) ** .5)) / (2)) ** .5

        return Complex(gamma, delta)


if __name__ == '__main__':
    unittest.main(complex_test.ComplexTestCase())

    a = Complex(1, -2)
    b = Complex(1, 4)
    c = Complex(1)
    d = Complex()
    print(a)
    print(b)
    print('1. ' + str(1.27 - b))
    print('2. ' + str(2-a))
    print('3. ' + str(1.5 + c))
    print('4. ' + str(1.5 + d))
    print('5. ' + str(a + b))
    print('6. ' + str(b + a))
    print('7. ' + str(b + c))
    print('8. ' + str(b * a))
    print('9. ' + str(b * 10))
    print('10. ' + str(a / 2) + '   |pythons answer is: ' + str((complex(1, -2))/2))
    print('10. ' + str(a / Complex(2, 0)) + '   |pythons answer is: ' + str((complex(1, -2))/complex(2, 0)))
    print('11. ' + str(-a))
    print('12. ' + str(a.conj()))
    print('13. ' + str(10 * a))

