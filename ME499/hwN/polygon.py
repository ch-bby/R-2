#!\usr\bin\env python3
#-*- coding: UTF-8 -*-

"""
*****************************
* ME 499 HW N: Polygon
* @author: Samuel J. Stumbo
* date: 4 June 2018
* file: polygon.py
* references: https://www.wikihow.com/Calculate-the-Area-of-a-Polygon
            https://en.wikipedia.org/wiki/Apothem
* description: Class that takes in a value for number of sides
            and returns the area and the name if fewer than 6-sides.
"""
from math import pi, tan

class Polygon():
    """
    Polygon class calculates the area of a polygon and returns the name
    given a number of sides. We assume a side length of 1 in all cases.
    """

    def __init__(self, n):
        self.n = n
        self.area = self.area(n)

    def __str__(self):
        if self.n < 4:
            return "This shape isn't polygonny enough!"
        if self.n == 4:
            return "Square"
        if self.n == 5:
            return "Pentagon"
        if self.n == 6:
            return "Hexagon"
        if self.n > 6:
            return "{0}-sided Polygon".format(n)

    def area(self, n):
        length = 1                          # Side length
        perimeter = n * length
        apothem = length/(2*tan(pi/n))
        return .5 * perimeter * apothem

if __name__=="__main__":
    n = 6
    s = Polygon(n)
    print(s.area)
    print(s)
