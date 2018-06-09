#!\usr\bin\env python3
#-*- coding: UTF-8 -*-

"""
***************************
* ME 499 HW N: Monte Carlo Pi Estimation
* @author: Samuel J. Stumbo
* date: 4 June 2018
* file: pi_mc.py
***************************
"""

"""
This program estimates pi using a Monte Python approximation. 
"""
import numpy as np
from math import pi

def pi_mc(bounds=(0,1), n=[10**5]):
    lower, upper = bounds
    xvals = np.random.uniform(lower, upper, size=n)
    yvals = np.random.uniform(lower, upper, size=n)
    cnt = 0
    for i in range(len(xvals)):
        if xvals[i]**2 + yvals[i]**2 < 1:
            cnt += 1
    pi_mc = 4*cnt/n[0]
    return pi_mc

if __name__ == "__main__":
    print(pi_mc())
    print(pi)