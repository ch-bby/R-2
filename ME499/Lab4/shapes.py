#!/usr/bin/env python3#
# -*- coding: utf-8 -*-

"""
****************************
    ME 499 Spring 2018
        Lab_4 Part 1
        3 May 2018
    Samuel J. Stumbo
****************************
    """
from math import pi

class Circle:
    """
    The circle class defines perimeter, diameter and area of a circle
    given the radius, r.
    """

    def __init__(self, r):
        if r <= 0:
            raise 'The radius must be greater than 0!'
        self.r = r

    def __str__(self):
        return 'Circle, radius {0}'.format(self.r)

    def area(self):
        return pi * self.r ** 2

    def diameter(self):
        return 2 * self.r

    def perimeter(self):
        return 2 * pi * self.r

class Rectangle:
    """
    The rectangle class has attributes of a rectangle, perimeter and area
    """
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise 'The length and width must both be positive values.'
        self.length = length
        self.width = width

    def __str__(self):
        return 'Rectangle, length {0} and width {1}'.format(self.length, self.width)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * 2 + self.width * 2

if __name__ == '__main__':
    c = Circle(1)
    r = Rectangle(2, 4)
    shapes = [c, r]

    for s in shapes:
        print('{0}: {1}, {2}'.format(s, s.area(), s.perimeter()))
