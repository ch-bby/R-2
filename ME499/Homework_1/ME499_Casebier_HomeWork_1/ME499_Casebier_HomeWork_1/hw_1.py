# -*- coding: utf-8 -*-
"""****************************************************************************
Author: Justin Casebier 
Created on Sat Apr 21 2018
Description: This program takes the spread sheet 'Grades.csv' and calculates 
relevant statistics about this data, includeing number of students per letter
grade and most difficult assignment

****************************************************************************"""

#Import Necessary libraries 

from file_organizer import list_organize
from hard import Hard_HW, Hard_Lab
from grades import B_C, F_S, G_S, Complain

#This function call the necessary function for the lab
def grade_qs(f_name):
    C_Stats={}
    data, index=list_organize(f_name)
    C_Stats['FS_stats']=F_S(data['F_S'])
    C_Stats['Hardest HW']=Hard_HW(data)
    C_Stats['Hardest Lab']=Hard_Lab(data)
    C_Stats['Grading Scheme']=G_S(data['F_S'])
    C_Stats['Number Complain']=Complain(data['F_S'])
    C_Stats['Bell Curve']=B_C(data['F_S'])
    print_Data(C_Stats)
    
    return C_Stats

#This function is used to print the necessary data
def print_Data(C):

    print('\nAverage Score: %.2f \n' %C['FS_stats']['Avg Final Score'])
    print('Above Average: %.2f' %C['FS_stats']['Stdt above avg'] +'% \n')
    print('Median Score: %.2f \n' %C['FS_stats']['Median Final Score'])
    print('Above Median: %.2f' %C['FS_stats']['Stdt above median'] + '% \n')
     
    print('Hardest Assignment: {} \n'.format(C['Hardest HW']))
    
    print('Hardest Lab: {} \n'.format(C['Hardest Lab']))
    
    print('A {}\n' .format(C['Grading Scheme'][0]))
    print('A- {}\n' .format(C['Grading Scheme'][1]))
    print('B+ {}\n' .format(C['Grading Scheme'][2]))
    print('B {}\n' .format(C['Grading Scheme'][3]))
    print('B- {}\n' .format(C['Grading Scheme'][4]))
    print('C+ {}\n' .format(C['Grading Scheme'][5]))
    print('C {}\n' .format(C['Grading Scheme'][6]))
    print('C- {}\n' .format(C['Grading Scheme'][7]))
    print('D+ {}\n' .format(C['Grading Scheme'][8]))
    print('D {}\n' .format(C['Grading Scheme'][9]))
    print('D- {}\n' .format(C['Grading Scheme'][10]))
    print('F {}\n' .format(C['Grading Scheme'][11]))
    
    print('{} students will complain about ther grade\n'.format(C['Number Complain']))
    
    print('A {}\n'.format(C['Bell Curve'][0]))
    print('B {}\n'.format(C['Bell Curve'][1]))
    print('C {}\n'.format(C['Bell Curve'][2]))
    print('D {}\n'.format(C['Bell Curve'][3]))
    
    





           
    
if __name__== '__main__':
    data=grade_qs('grades.csv')     



#  s=grade_qs('grades.csv')
#    print(s)  
    
