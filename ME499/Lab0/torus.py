#!/usr/bin/env python3
""" ME 499 Computer Programming for Mechanical Systems
    Lab 0 Part 4: Volume of a torus calculator
    Samuel J. Stumbo
    5 April 2018


    This script calculates the volume of a torus given the inner radius and outer radius."""
from math import pi


r_1 = 3                             # Inner radius of torus
r_2 = 4                             # Outer radius of torus
r_mid = (r_1 + r_2) / 2             # Average radius of torus
r_circle = (r_2 - r_1) / 2          # Radius of donut cross-section

# This function calculates the volume of a torus
def volume_tor(ave_rad, rad_donut):
    volume = (pi * rad_donut ** 2)*(2 * pi * ave_rad)
    return volume

print(volume_tor(r_mid, r_circle))