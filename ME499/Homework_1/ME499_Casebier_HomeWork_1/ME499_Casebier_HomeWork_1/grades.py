"""****************************************************************************
Author: Justin Casebier 
Created on Sat Apr 21 2018
Description: This program works congruently with hw_1 and is used to calculate
the number of students per grade and who will complain about there grade due to 
being .5% w/in the next letter grade  for the class in 'grades.csv 
THis program also calculates statistics about the final scores of students
****************************************************************************"""

import statistics

#Calculates a bell curve grading scheme
def B_C(f_s):
    cut=[]
    f_ssort=list(reversed(sorted(f_s)))
    f_slen=len(f_s)
    #Percentages as perscribed in the lab prompt
    Asize=int(f_slen*.1)
    Bsize=int(f_slen*.3)
    Csize=int(f_slen*.6)
    Dsize=int(f_slen*.9)
    
    cut.append(f_ssort[Asize-1])
    cut.append(f_ssort[Bsize-1])
    cut.append(f_ssort[Csize-1])
    cut.append(f_ssort[Dsize-1])
    
    return cut
   
    
    
#This function will compare each final score with a range for a letter 
#grade and give the student the appropriate grade 
def G_S(f_s):
    grades=[]
    

    grade_cut=[max(f_s)+1,94,90,87,84,80,77,74,70,67,64,61,0]
    for i in range(0,len(grade_cut)):
        temp=0
        for j in f_s:
            if (j<grade_cut[i]) and (j>=grade_cut[i+1]):
                temp+=1
        grades.append(temp)

    return grades

#This function will find the number of students that complain about their 
#grade. A student will complain if there grade is w/in .5% of the next later 
#grade. 
def Complain(f_s):
    grades=[]
    
    comp_hi=[93.99,89.99,86.99,83.99,79.99,76.99,73.99,69.99,66.99,63.99,60.99]
    comp_lo=[93.5,89.5,86.5,83.5,79.5,76.5,73.5,69.5,66.5,63.5,60.5]
    for i in range(0,len(comp_hi)):
        temp=0
        for j in f_s:
            if (j<=comp_hi[i]) and (j>=comp_lo[i]):
                temp+=1
        grades.append(temp)
        
    return sum(grades)
    
    

    
    
    
#This function gives relevant statistics about the class final score as a whole
    
def F_S(f_s):
    F_S_d={}
    F_S_d['Stdt above avg']=0
    F_S_d['Stdt above median']=0
    F_S_d['Avg Final Score']=statistics.mean(f_s)
    F_S_d['Median Final Score']=statistics.median(f_s)
    for i in range(0,len(f_s)) :
        if f_s[i]>=F_S_d['Avg Final Score']:
            F_S_d['Stdt above avg']+=1
        if f_s[i]>=F_S_d['Median Final Score']:
            F_S_d['Stdt above median']+=1
    F_S_d['Stdt above avg']=100*(F_S_d['Stdt above avg']/len(f_s))
    F_S_d['Stdt above median']=100*(F_S_d['Stdt above median']/len(f_s))
    return F_S_d
