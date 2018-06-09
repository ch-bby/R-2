#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 16:52:54 2018

@author: johneichmann
"""
"""

Find the hardest assignment

"""
import glob
import csv
from statistics import *
 
f = csv.reader(open('grades.csv'))
matrix = list(f)   
headers = matrix[0][:]

first_hw_assignmentindex = headers.index('Homework 1 (7083684)')

hw_print_titles = headers[47:56]

hw = []
max_hw = []
mean_hw = []

for i in range(len(headers)):
    
    if i >= (first_hw_assignmentindex) and i<=(first_hw_assignmentindex+8):
        hwi = [row[i] for row in matrix]
        hwi = hwi[1:]
        
        hw.append(hwi)
        
hw1 = hw[:][0]

hw1.remove('EX')
hw1 = [float(i) for i in hw1]  

for i in range(9):
    if i == 0:
        max_score = max(hw1)
        max_hw.append(max_score)
        mean_score = mean(hw1)
        mean_hw.append(mean_score)
    
    else:
        hw_temp = hw[i]
        hw_temp = [float(i) for i in hw_temp]
        
        max_score = max(hw_temp)
        max_hw.append(max_score)
        mean_score = mean(hw_temp)
        mean_hw.append(mean_score)        
        
hw_percent = []

for i in range(9):
    hw_percent.append((mean_hw[i]/max_hw[i])*100)
    
    
hw_hard_index = int(hw_percent.index(min(hw_percent)))
hw_hard_title = hw_print_titles[0+ hw_hard_index]


print('Hardest assignment:'+ ' ' + str(hw_hard_title))

"""

Find the hardest Lab assignment


"""
first_lab_assignmentindex = headers.index('Lab 1 Exercise (7083695)')

lab_print_titles = headers[36:46]

lab = []
max_lab = []
mean_lab = []

for i in range(len(headers)):
    
    if i >= first_lab_assignmentindex and i<=(first_lab_assignmentindex+9):
        labi = [row[i] for row in matrix]
        labi = labi[1:]
        
        lab.append(labi)
        
lab1 = lab[:][0]

lab1.remove('EX')

lab1 = [float(i) for i in lab1]  

for i in range(10):
    if i == 0:
        max_lab_score = max(lab1)
        max_lab.append(max_lab_score)
        mean_lab_score = mean(lab1)
        mean_lab.append(mean_lab_score)

    else:
        lab_temp = lab[i]
        
        lab_temp = [float(i) for i in lab_temp]
        
        max_lab_score = max(lab_temp)
        max_lab.append(max_lab_score)
        mean_lab_score = mean(lab_temp)
        mean_lab.append(mean_lab_score)        
        
lab_percent = []
for i in range(10):
    lab_percent.append((mean_lab[i]/max_lab[i])*100)
    
lab_hard_index = int(lab_percent.index(min(lab_percent)))
lab_hard_title = lab_print_titles[0+ lab_hard_index]

print('Hardest lab:'+ ' ' + str(lab_hard_title))
