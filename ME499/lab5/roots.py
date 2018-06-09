#!/usr/bin/env python3#
# -*- coding: utf-8 -*-

"""
****************************
    ME 499 Spring 2018
        Lab_5 Roots.py
        16 May 2018
    Samuel J. Stumbo
****************************
    """

"""
References used:
*****************************
https://docs.python.org/3/library/unittest.html
https://stackoverflow.com/questions/1623375/writing-your-own-square-root-function
https://en.wikipedia.org/wiki/Complex_number#Square_root
*****************************
"""

import decimal
import complex_test
import complex
import unittest
import numpy as np

def roots(array):
    """
    This function calculates the roots of a quadratic.
    It could be modified in the future to include higher order functions.
    :param array:
    :return:
    """
    poly = []
    for i in array:
        if isinstance(i, str):
            raise TypeError('Please enter float or int')
        if isinstance(i, int):
            poly.append(float(i))

    a = poly[0]
    b = poly[1]
    c = poly[2]
    d = b ** 2 - 4 * a * c

    if a == 0:
        roots = -c/b
        return roots

    if b == 0 and c == 0:
        roots = 0, 0
        return roots
    if d >= 0:
        roots = (-b  + complex.sqrt(d))/(2 * a), (-b - complex.sqrt(d))/(2 * a)
        return roots
    else:
        roots = (-b + complex.sqrt(d)) / (2 * a), (-b - complex.sqrt(d)) / (2 * a)
        c_root_1 = roots[0]
        c_root_2 = roots[1]
        re_1 = c_root_1.re
        im_1 = c_root_1.im
        re_2 = c_root_2.re
        im_2 = c_root_2.im


        if im_1 < 0 and im_2 < 0:
            return '{0} - {1}i'.format(re_1, abs(im_1)), '{0} - {1}i'.format(re_2, abs(im_2))

        if im_1 >= 0 and im_2 >= 0:
            return '{0} + {1}i'.format(re_1, im_1), '{0} + {1}i'.format(re_2, im_2)

        if im_1 >= 0 and im_2 < 0:
            return '{0} + {1}i'.format(re_1, im_1), '{0} - {1}i'.format(re_2, abs(im_2))

        if im_1 < 0 and im_2 >= 0:
            return '{0} - {1}i'.format(re_1, abs(im_1)), '{0} + {1}i'.format(re_2, im_2)


def evaluate(array, value):
    """
    This function evaluates a polynomial  for a given value.
    The value could be complex or normal.
    :param array:
    :param value:
    :return:
    """
    solution = 0
    for i in range(len(array)):
        solution += (array[-i-1]) * value ** i
    return solution


if __name__ == "__main__":
    unittest.main(complex_test.ComplexTestCase())
