#!\usr\bin\env python3
#-*- coding: UTF-8 -*-


"""
***********************************
* ME 499 LAB 7 Part 2
* Date: 06-03-18
* @author: Samuel J. Stumbo
* File: integrate.py
***********************************
"""

"""
************************************
sources: 
https://pascalbugnion.net/blog/monte-carlo-integration.html
************************************
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def integrate_mc(f, bounds, n):
    # Returns monte carlo approximation to definite integral
    xlower, xupper = bounds
    ylower = 0
    # Call with single value of n

    xvals = np.random.uniform(xlower, xupper, n)
    yval_max = 0
    for val in xvals:
        yval = func(val)
        if yval > yval_max:
            yval_max = yval
    b_box = ((yval_max - ylower) * (xupper - xlower))
    yvals = np.random.uniform(ylower, yval_max, n)
    count = 0
    for n in range(len(yvals)):
        if yvals[n] <= func(xvals[n]):
            count += 1

    proportion = count/len(yvals)
    integral_mc = b_box * proportion
    return integral_mc

def func(x):
    return x**2

def error_plots():
    n = [10, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]
    act_val = 9                                 # Actual value!!! NEEDS TO BE UPDATED FOR EACH FUNCTION
    integrals = []
    for i in n:
        integrals.append(integrate_mc(func, bounds, i))
    err_mc = []
    for integral in integrals:
        err_mc.append(abs(act_val - integral))
    fig = plt.figure()
    plt.loglog(n, err_mc)
    plt.xlabel('values of n (log)')
    plt.ylabel('Error (log)')
    plt.title('Plot of Accuracy versus number of steps for {}'.format('x**2'))
    plt.legend(['Monte Carlo Accuracy'], loc=0)

    # This section saves the figure...
    for i in range(20):
        fig_name = 'ME 499-L7-PL-{}.png'.format(i)
        fig_path = Path(fig_name)
        if fig_path.is_file():
            print('taken')
            continue
        else:
            fig_name = fig_name
            fig.savefig(fig_name)
            break
    return fig

if __name__ == "__main__":
    bounds = (0, 3)
    #n = [10, 10**2, 10**3, 10**4, 10**5, 10**6]
    n = 10**6
    i = integrate_mc(func, bounds, n)
    print(i)
    plot = error_plots()
    plt.show()
