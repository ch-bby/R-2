#!usr\bin\env python3
"""
*****************************
*     ME 499 Lab 3          *
*
*     27 April 2018         *
*     Samuel J. Stumbo      *
*****************************
"""
"""
***************************************************
*         Part 5: Sorting Random Numbers          *
*     This program generates a list of random     *
* numbers and sets it in order and then plots the *
*    time it takes versus the length of the list  *
***************************************************
"""
# Include necessary libraries
import numpy as np
import time
import matplotlib.pyplot as plt
def list_sort_time():
    i = 1
    time_sort = []
    i_array = []
    time_sum = []

    while i <= 1000000:
        l = np.random.random_sample((i,))
        start_time = time.clock()
        l.sort()
        end_time = time.clock()
        time_diff = end_time - start_time
        time_sort.append(time_diff)

        # This part adds the list and counts how long it takes...
        start_time = time.clock()
        (sum(l))
        end_time = time.clock()
        time_diff = end_time - start_time
        time_sum.append(time_diff)
        i_array.append(i)
        i = i * 10
    return (time_sort, time_sum, i_array)

def sort_plot():
    time_sort, time_sum, i_array = list_sort_time()
    fig_1 = plt.figure()
    plt.semilogx()
    plt.plot(i_array, time_sort)
    plt.xlabel('Length of list')
    plt.ylabel('Time it takes [s]')
    plt.title("Length of list versus time it takes to SORT it")

    fig_2 = plt.figure()
    plt.semilogx()
    plt.plot(i_array, time_sum)
    plt.xlabel('Length of list')
    plt.ylabel('Time [s]')
    plt.title("Length of list versus time it takes to ADD it")
    return fig_1, fig_2



