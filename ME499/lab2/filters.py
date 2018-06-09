#!/usr/bin/env python3
"""
ME 499: Lab 2
Samuel J. Stumbo
20 April 2018

Filters Function

This function reads in random data (or any data, really) and normalizes it
    """

from sensor import *
import numpy as np
import matplotlib.pyplot as plt



def mean_filter(l1, width = 3):
    unfiltered = []
    w = width // 2

    for n in l1:
        unfiltered.append(n)
    filtered = []

    for i in range(w, len(l1)-w):
        filtered.append(sum(unfiltered[i - w : i + w + 1]) / width)

    return unfiltered, filtered

def median_filter(l1, width=3):
    filtered = []
    w = width
    for i in range(len(l1) - w + 1):
        filtered.append(np.median(unfiltered[i: i + w]))
    return filtered

if __name__ == '__main__':
    data = generate_sensor_data()
    width = 5
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    unfiltered, mean = mean_filter(data, width)
    median = median_filter(data,width)
    print_sensor_data(unfiltered, 'unfiltered.txt')
    print_sensor_data(mean, 'mean.txt')
    print_sensor_data(median, 'median.txt')
    # red dashes, blue squares and green triangles
    plt.plot(range(len(mean)), mean, 'r--', range(len(median)), median, 'g', range(len(data)), data)
    plt.show()
    # print(filtered)
    # print(median_filter(l1, n))

    # fin = open('words.txt')
    # print(fin.readline())