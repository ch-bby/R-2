"""****************************************************************************
Author: Justin Casebier 
Created on Sat Apr 21 2018
Description: This program works congruently with hw_1 and is used to organize 
the data from the spreadsheet 'grades.csv' into a format that python can read.
This program can remove non numeric numbers and negatives. 

****************************************************************************"""
#Import Necessary libraries 
import csv

def list_organize(f_name):
    #Initialize counter and boolean used to remove number numeric values
    i=0
    bo0l=1
    #Create Dictionaries that will house data 
    index={}
    data={}
    #Read in the file
    with open(f_name,'r') as r_data:
        csv_reader=csv.reader(r_data)
        #For loop to cycle through each row of the spreadsheet
        for line in csv_reader:
            
            #Lines 25-50 are used to find the location of the necessary columns
            #and initialized the list within the dictionary to house this data
            #this chuck will only run once as it is only used to create 
            #dictionary keys and indexing
            for j in range(0,len(line)):
                if i==0:    
                    if line[j]=='Final Score':
                        index['F_S']=j
                        data['F_S']=[]
                       
                    for k in range(1,11):
                        if (line[j][9]==str(k)) and (line[j][0]=='L') and (line[j][10]==' '):
                            index['Lab Quiz '+str(k)]=j
                            data['Lab Quiz '+str(k)]=[]
                        elif (line[j][9]+line[j][10]==str(k)) and(line[j][0]=='L') and (line[j][10]=='0'):
                            index['Lab Quiz '+str(k)]=j
                            data['Lab Quiz '+str(k)]=[]
                            
                        elif (line[j][4]==str(k)) and (line[j][0]=='L') and (line[j][5]==' '):
                            index['Lab ' + str(k) + 'Exercise']=j
                            data['Lab ' + str(k) + 'Exercise']=[]
                            
                        elif (line[j][4]+line[j][5]==str(k)) and (line[j][0]=='L') and (line[j][5]=='0'):
                            index['Lab ' + str(k) + 'Exercise']=j
                            data['Lab ' + str(k) + 'Exercise']=[]
                        
                    for k in range(1,10):
                        if (line[j][9]==str(k)) and (line[j][0]=='H'):
                            index['Homework '+str(k)]=j
                            data['Homework '+str(k)]=[]
                   
                else:
                        #Lines 57-116 is used to Organized the data in to
                        #respective dictionary slots. If the index number of
                        #the index dictionary is equal to the current index  
                        #"j", then the number inside the spreadsheet cell will
                        #be added to the repesctive dictionary slot within data
                        bo0l=1
                        for k in range (1,11):
                            #Adds all lab quizzes to the data library
                            if (j==index['Lab Quiz '+str(k)]):
                                #This for loop is used to check if there any 
                                #non numeric vales by checking the ascii number
                                #The program will then report the column name
                                #and row number where the non numberic exist
                                for z in range(0,len(line[j])):  
                                    if (ord(line[j][z])==47) or (ord(line[j][z])>58) or (ord(line[j][z])<45):
                                        print('Non numeric value found in Lab Quiz ' + str(k) + ' row ' +str(i+1))
                                        bo0l=0
                                        #breaks once the it is realized that 
                                        #there is a non numeric value
                                        break
                                if bool(bo0l):
                                    #This if loop will check to see if there is
                                    #negative number in the cell. 
                                     #The program will then report the column name
                                #and row number where the negative exist
                                    if float(line[j])<0:
                                        print('Value less than Zero found in Lab Quiz ' + str(k) + ' row ' +str(i+1) )
                                    else:
                                        data['Lab Quiz '+str(k)].append(float(line[j]))
                        
                        for k in range (1,10):
                            #Adds all homeworks to the data library
                            #internals work the same as the block above 
                            if (j==index['Homework '+str(k)]):
                                 for z in range(0,len(line[j])):
                                     if (ord(line[j][z])==47) or (ord(line[j][z])>58) or (ord(line[j][z])<45):
                                         print('Non numeric value found in Homework ' + str(k) + ' row ' +str(i+1))
                                         bo0l=0
                                         break
                                 if bool(bo0l):
                                     if float(line[j])<0:
                                        print('Value less than Zero found in Homework ' + str(k) + ' row ' +str(i+1) )
                                     else:
                                        data['Homework '+str(k)].append(float(line[j]))
                                        
                        for k in range (1,11):
                            #Adds all lab excercises to the data library
                            #internals work the same as the block above 
                            if (j==index['Lab ' + str(k) + 'Exercise']):
                                for z in range(0,len(line[j])):    
                                    if (ord(line[j][z])==47) or (ord(line[j][z])>58) or (ord(line[j][z])<45):
                                        print('Non numeric value found in Lab ' + str(k) + ' Exercise, row ' +str(i+1))
                                        bo0l=0
                                        break
                                if bool(bo0l):
                                    
                                    if float(line[j])<0:
                                        print('Value less than Zero found in Lab ' + str(k) + 'Exercise, row ' +str(i+1) )
                                    else:
                                        data['Lab ' + str(k) + 'Exercise'].append(float(line[j]))                
                       
                                         
                                         
                        #Adds all Final Scores to the data library
                        #internals work the same as the block above                            
                        if (j==index['F_S']):
                             for z in range(0,len(line[j])):
                                 if (ord(line[j][z])==47) or (ord(line[j][z])>58) or (ord(line[j][z])<45):
                                     
                                     print('No numeric value found in Final Score row ' +str(i+1))
                                     bo0l=0
                                     break
                             if bool(bo0l):
                                 if float(line[j])<0:
                                        print('Value less than Zero found in Final Score row ' +str(i+1) )
                                 else:
                                        data['F_S'].append(float (line[j]))
                                
                                    
                                    
                            
            #Iterates through the rows     
            i+=1
            
    return data, index 