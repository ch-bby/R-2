"""****************************************************************************
Author: Justin Casebier 
Created on Sat Apr 21 2018
Description: This program works congruently with hw_1 and is used to calculate
the hardest lab and homework for the class in 'grades.csv 
****************************************************************************"""
#Import Necessary libraries 
import numpy, statistics


#This function will caluculate the hardest Homework 
def Hard_HW(data):
    hw=[]
    hw_pc=[]
    hw_ph=[]
    hw_max=[]
    avg_gr=[]
    
    
    for i in range(0,9):
        hw.append(data['Homework '+str(i+1)])
        hw_max.append(max(hw[i])) 
        hw_ph.append(numpy.divide(hw[i],hw_max[i]))
        hw_pc.append(hw_ph[i].tolist())
        avg_gr.append(statistics.mean(hw_pc[i])) 
        hard_hw=min(avg_gr)
 
     
    for i in range(0,9):
        if hard_hw==avg_gr[i]:
            Hard_hw_i=i+1 
    return Hard_hw_i

#This function will caluculate the hardest lab 
#Since there are two lab assignments, the lab assignments and quizzes are 
#averaged seperately and the averages together. 
def Hard_Lab(data):
    labQ=[]
    labE=[]
    labE_pc=[]
    labQ_pc=[]
    labE_ph=[]
    labQ_ph=[]
    labE_max=[]
    labQ_max=[]
    avgE_gr=[]
    avgQ_gr=[]
    avg_gr=[]
    
    
    
    for i in range(0,9):
        labQ.append(data['Lab Quiz '+str(i+1)])
        labE.append(data['Lab ' + str(i+1) + 'Exercise'])
        
        labQ_max.append(max(labQ[i])) 
        labE_max.append(max(labQ[i])) 
        
        labQ_ph.append(numpy.divide(labQ[i],labQ_max[i]))
        labE_ph.append(numpy.divide(labE[i],labE_max[i]))
                
        labQ_pc.append(labQ_ph[i].tolist())
        labE_pc.append(labE_ph[i].tolist())
        
        avgQ_gr.append(numpy.array(statistics.mean(labQ_pc[i]))) 
        avgE_gr.append(numpy.array(statistics.mean(labE_pc[i]))) 
        
        avg_gr.append(((avgQ_gr[i]+avgE_gr[i])/2).tolist())
        
        hard_lab=min(avg_gr)
             
    for i in range(0,9):
        if hard_lab==avg_gr[i]:
            Lab_hw_i=i+1 
    return Lab_hw_i