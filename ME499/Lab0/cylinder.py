#!/usr/bin/env python3
""" ME 499 Computer Programming for Mechanical Systems
    Lab 0 Part 3: Volume of a cylinder
    Samuel J. Stumbo
    5 April 2018

    This script calculates the volume of a cylinder given the radius and height of a cylinder."""


from math import pi                         # Imports the pi function from the math package

radius = 3.0                                # Radius of cylinder (unitless)
height = 5.0                                # Height of cylinder (unitless)
Volume = pi * radius ** 2 * height          # Calculate volume of cylinder
print(Volume)                               # Prints the volume


