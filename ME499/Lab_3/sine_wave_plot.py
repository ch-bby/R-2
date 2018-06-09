#!/usr/bin/env python3
#  -*- coding: utf-8 -*

"""
*****************************
*     ME 499 Lab 3          *
*    -Sine Wave Plot-       *
*     27 April 2018         *
*     Samuel J. Stumbo      *
*****************************
"""

"""
********************************************************
*  Part 2: This script plots a sin wave from 0 to 4*pi *
********************************************************
"""

"""
***********************************************
                List of Borrowed Code
                ********************
https://stackoverflow.com/questions/24791709/save-a-plot-resulting-from-a-function-matplotlib-python
***********************************************

"""
# import necessary packages
from math import pi
import numpy as np
import matplotlib.pyplot as plt

def plot_sine():
    # Generate range of values to plot
    theta = np.arange(0., 4*pi, pi/100)

    # Plots
    sine_fig = plt.figure()
    plt.plot(theta, np.sin(theta))
    plt.xlabel(r'$\theta$ [rad]')
    plt.ylabel(r'sin($\theta$)')
    plt.title(r'Lab 3 Part 2: sin($\theta$) from 0 to 4$\pi$')
    plt.xlim([0, 4*pi])
    plt.ylim([-1, 1])
    plt.grid(True)
    #plt.show()

    return sine_fig

if __name__ == "__main__":
    sine_fig = plot_sine()
