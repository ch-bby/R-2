#!usr\bin\env python3
"""
*****************************
*     ME 499 Lab 3          *

*     27 April 2018         *
*     Samuel J. Stumbo      *
*****************************
"""

"""
***************************************************
*    Part 3: Plotting a normal distribution       *
*  Used documentation for numpy random.uniform    *
***************************************************
"""
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

def sum_norm():
    i = 0
    ssum = []

    while i < 10000:
        s = np.random.uniform(0,1,10)
        ssum.append(np.sum(s))
        i += 1
    return ssum

def print_norm_hist():
    ssum = sum_norm()
    fig = plt.figure()
    count, bins, ignored = plt.hist(ssum, 15, normed=True)
    plt.plot(bins, np.ones_like(bins), linewidth=2)
    plt.xlabel('Occurrences')
    plt.ylabel('Distribution')
    plt.title('Randomly generated list of summed lists histogram')
    return fig


