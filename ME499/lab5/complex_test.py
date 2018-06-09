#!/usr/bin/env python3#
# -*- coding: utf-8 -*-

"""
****************************
    ME 499 Spring 2018
        Lab_5 Test Suite
        16 May 2018
    Samuel J. Stumbo
****************************
    """
# Testing class
import unittest
from complex import Complex
import math
from complex import sqrt
import cmath
import roots
import numpy as np


class ComplexTestCase(unittest.TestCase):
    """
    This class tests the functionality of the Complex Class
    from lab 4 and 5. The test suite came from Python's unittest framework.
    """
    # Need to fix the string tests.
    # def test_1(self):
    #     a = Complex(1.0, 2.3)
    #
    #     self.assertEqual(print(a), '(1.0 + 2.3i)', 'String format is incorrect.')
    #
    # def test_2(self):
    #     b = Complex(2)
    #     self.assertEqual(print(b), '(2 + 0i', 'String format is incorrect.')
    #
    # def test_3(self):
    #     c = Complex()
    #     self.assertEqual(print(c), '(0 + 0i)', 'String format is incorrect.')
    #
    # def test_4(self):
    #     a = Complex(1, 2)
    #     self.assertEqual(print(a), '(1 + 2i)', 'String format is incorrect')
    #
    # def test_5(self):
    #     a = Complex(1, -2)
    #     self.assertEqual(a, complex(1, -2), 'String format is incorrect')

    def test_6(self):
        c = Complex(1.2, 3.4)
        self.assertEqual(c.re, 1.2, "Can't get real part") and self.assertEqual(
            c.im, 3.4, "Can't get at complex part."
        )

    def test_a_plus_b(self):
        a = Complex(1, 2)
        b = Complex(1, -2)
        c = a + b
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, complex(1, 2) + complex(1, -2),
                         'Complex add error')

    def test_b_plus_a(self):
        a = Complex(1, 2)
        b = Complex(1, -2)
        c = b + a
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, complex(1, -2) + complex(1, 2), 'Adding two complex numbers failed')

    def test_num_minus_b(self):
        a = 1.27
        b = Complex(1, -2)
        c = a - b
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, 1.27 - complex(1, -2), 'Subtracting a complex number from a complex number failed.')


    def test_b_minus_num(self):
        a = 1.27
        b = Complex(1, -2)
        c = b - a
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, complex(1, -2) - 1.27, 'Subtracting a number from a complex number failed.')

    def test_num_plus_b(self):
        a = 1.27
        b = Complex(1, -2)
        c = a + b
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, 1.27 + complex(1, -2), 'Adding a number to a complex number failed.')

    def test_b_plus_num(self):
        a = 1.27
        b = Complex(1, -2)
        c = b + a
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, complex(1, -2) + 1.27, 'Adding a complex number to a number failed.')

    def test_a_times_b(self):
        a = Complex(1, 2)
        b = Complex(1, -2)
        c = a * b
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, complex(1, 2) * complex(1, -2), 'Multiplying two complex numbers failed.')

    def test_a_times_num(self):
        a = Complex(1, 2)
        b = 10
        c = a * b
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, complex(1, 2) * 10, 'Multiplying a complex number by an integer failed.')

    def test_num_times_a(self):
        a = 10
        b = Complex(1, 2)
        c = a * b
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, 10 * complex(1, 2), 'Multiplying an integer by a complex'
                                                'number failed.')

    def test_a_div_b(self):
        a = Complex(-1, 2)
        b = Complex(1, 2)
        c = a / b
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, complex(-1, 2) / complex(1, 2), 'Dividing a complex number by a complex'
                                                            'number failed.')

    def test_b_div_a(self):
        a = Complex(-1, 2)
        b = Complex(1, 2)
        c = b / a
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, complex(1, 2) / complex(-1, 2), 'Dividing a complex number by a complex'
                                                            'number failed.')

    def test_a_div_num(self):
        a = Complex(-1, 2)
        b = 10
        c = a / b
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, complex(-1, 2) / 10, 'Dividing a complex number by a'
                                                            ' number failed.')

    def test_num_div_a(self):
        a = Complex(-1, 2)
        b = 10
        c = b / a
        re_c = c.re
        im_c = c.im
        c = complex(re_c, im_c)
        self.assertEqual(c, 10 / complex(-1, 2), 'Dividing a number by a'
                                                ' complex number failed.')

    def test_complex_negation(self):
        a = Complex(1, 2)
        neg_a = -a
        re_neg_a = neg_a.re
        im_neg_a = neg_a.im
        c = complex(re_neg_a, im_neg_a)
        self.assertEqual(c, -complex(1, 2), "Negation didn't work properly")

    def test_complex_conjugate(self):
        a = Complex(-1, 2)
        a_conj = a.conj()
        conj_re = a_conj.re
        conj_im = a_conj.im
        c = complex(conj_re, conj_im)
        d = ~a
        d_im = d.im
        d_re = d.re
        d = complex(d_re, d_im)
        self.assertEqual(c, complex(-1, 2).conjugate())
        self.assertEqual(d, complex(-1, 2).conjugate())


    def test_sqrt(self):
        a = 1.23
        c = Complex(1.23, 3.45)
        d = sqrt(c)

        d_re = d.re
        d_im = d.im
        e = complex(d_re, d_im)
        self.assertEqual(sqrt(a), math.sqrt(a))
        self.assertEqual(e, cmath.sqrt(complex(1.23, 3.45)))


    def test_roots(self):
        a = roots.roots([1, 0, 0])
        a_np = np.roots([1, 0, 0])
        b = roots.roots([1, 2, 3])
        b_np = np.roots([1, 2, 3])
        c = roots.roots([1, 2, -3])
        c_np = np.roots([1,2, -3])
        d = roots.roots([1, 0, 3])
        d_np = np.roots([1, 0, 3])
        self.assertTupleEqual(a, tuple(a_np), 'Roots test 1 fail.')

        # The following code recognizes an error, however, they technically
        # evaluate the same...
        self.assertTupleEqual(b, tuple(b_np), 'Roots test 2 fail.')
        self.assertTupleEqual(c, tuple(c_np), 'Roots test 3 fail.')
        self.assertTupleEqual(d, tuple(d_np), 'Roots test 4 fail.')

    def test_evaluate(self):
        a = roots.evaluate([1, 2, 3], 2)
        b = roots.evaluate([1, 2, 3], Complex(1, 2))
        c = roots.evaluate([4, 3, 2, 1], 12)
        a_np = np.polyval([1, 2, 3], 2)
        b_np = np.polyval([1, 2, 3], complex(1, 2))
        b = complex(b.re, b.im)
        c_np = np.polyval([4, 3, 2, 1], 12)
        self.assertEqual(a, a_np, 'Evaluate test 1 fail.')
        self.assertEqual(b, b_np, 'Evaluate test 2 fail.')
        self.assertEqual(c, c_np, 'Evaluate test 3 fail.')
