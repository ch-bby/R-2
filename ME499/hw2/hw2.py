#!/usr/bin/env python3
# -*-coding: utf-8 -*-


"""
****************************
    ME 499 Spring 2018
        HW 2 hw2.py
        24 May 2018
    Samuel J. Stumbo
****************************
"""

"""
References used:
*****************************
1. Dr. Smart's webcam.py 
*****************************
"""

"""
*****************************
Import necessary libraries
*****************************
"""

from webcam import Webcam
from PIL import Image, ImageMath, ImageStat
from math import *
import numpy as np
import csv
import time
import os
import matplotlib.pyplot as plt


class MUCamera():
    """
    The MUCamera class pulls images from the MU Camera on campus. This code takes the average intensity of
    some images in

    """

    def __init__(self):
        self.w = Webcam()
        self.start = self.w.start()
        self.stop = self.w.stop()
        self.callback = self.w.callback
        self.w.register_callback(self.callback, .5)
        # self.filtered_average_intensity = filtered_average_intensity(self)

    def __str__(self):
        return 'Average Intensity:                                  {0}\n'\
               'Filtered Average Intensity:                           \n'\
                "It's daytime right now!                            {1}\n" \
               "The filtered average is:                            {2}\n" \
               "Most common color:                                   {3}".format(self.average_intensity(),
                                                                                  self.daytime(),
                                                                                    self.filtered_average_intensity(),
                                                                                    self. most_common_color())

    def average_intensity(self):
        w = Webcam()
        im = w.grab_image()
        stat = ImageStat.Stat(im)
        ave = stat.mean
        ave = np.average(ave)

        return ave

    def filtered_average_intensity(self):
        # This code takes waaaay too long to run! I had this issue when I tried to take the average manually (sum(sum(row))
        # The solution was to use the .Stat module. I don't know if that applies a filter though...
        w = Webcam()
        im = w.grab_image()
        rgb = im.getdata()
        ave_rgb = []
        value = []
        for pixel in rgb:
            value.append(pixel)
            ave_rgb.append(np.average(pixel))

        # The filter used here is my own from a previous assignment. It works, but it's really slow!
        filtered_average_intensity = np.average(mean_filter(ave_rgb))
        return filtered_average_intensity

    def daytime(self):
        # This looks at the average intensity. If the value drops below 70 it's probably dark
        if self.average_intensity() < 70:
            return False
        else:
            return True

    def most_common_color(self):
        # So far, this hasn't returned a value. It's either working and taking forever or
        # it's stuck in an infinite loop.
        w = Webcam()
        im = w.grab_image()
        rgb = im.getdata()
        rgb = list(rgb)
        most_common_color = max(rgb, key=rgb.count)
        return most_common_color

def mean_filter(l1, width = 3):
    unfiltered = []
    w = width // 2

    for n in l1:
        unfiltered.append(n)
    filtered = []

    for i in range(w, len(l1)-w):
        filtered.append(sum(unfiltered[i - w: i + w + 1]) / width)

    return filtered

def get_pic_data(how_long=600, cnt=0, last_time=0):
    # Function calls class to plot average intensities...
    w = Webcam()
    t = time.time()
    averages = []
    time_arr = []
    while time.time() - t < how_long:
        interval = time.time() - last_time
        if interval >= 6:
            time_arr.append(floor(time.time() - t))
            averages.append(m.average_intensity())
            last_time = time.time()
    with open('averages_{}'.format(time.time()), 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([averages, time_arr])
    csvfile.close()
    return averages, time_arr

def plot_image_data():
    # tried to use this to access images that I collected overnight last night, but was unable to access the images
    # They are stored in an excel spreadsheet.
    with open('images_5_30.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        images = []
        for row in reader:
            for item in row:
                print(item)
                item = Image.Image.frombytes(item)
                print(type(item))
                images.append(item)
        t = range(len(images))
        averages = []
        for im in images:
            stat = ImageStat.Stat(im)
            ave = stat.mean
            ave = np.average(ave)
            averages.append(ave)

    return t, averages


if __name__ == '__main__':
    m = MUCamera()
    # average_intensity = m.average_intensity()
    # print(average_intensity)
    #
    # filtered = m.filtered_average_intensity()
    # print(filtered)
    #
    # daytime = m.daytime()
    # print(daytime)

    # most_comm = m.most_common_color()
    # print(most_comm)

    intensities, time_arr = get_pic_data()
    fig = plt.figure()
    plt.plot(time_arr, intensities)
    plt.xlabel('Time (s)')
    plt.ylabel('Intensity')
    plt.title('Intensity vs. Time')
    plt.show()





