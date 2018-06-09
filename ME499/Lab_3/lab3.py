#!usr\bin\env python3
"""
*****************************
*     ME 499 Lab 3          *
*     27 April 2018         *
*     Samuel J. Stumbo      *
*****************************
"""
# Import necessary libraries

import matplotlib.pyplot as plt
import sine_wave_plot
import rnd_sum_hist
import smd
import time_sort

"""
********************************************************
*  Part 2: This script plots a sin wave from 0 to 4*pi *
********************************************************
"""
fig_1 = sine_wave_plot.plot_sine()


"""
***************************************************
*    Part 3: Plotting a normal distribution       *
*  Used documentation for numpy random.uniform    *
***************************************************
"""
fig_2 = rnd_sum_hist.print_norm_hist()

"""
***************************************************
*    Part 4: Mass spring damper function          *
*                                                 *
***************************************************
"""
fig_3 = smd.smd_plot()

"""
***************************************************
*         Part 5: Sorting Random Numbers          *
*                                                 *
***************************************************
"""
fig_4, fig_5 = time_sort.sort_plot()
plt.show()






