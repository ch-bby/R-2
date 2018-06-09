#!\bin\usr\env python3

"""
****************************************
*ME 499 Homework 1: Analyzing Grades   *
*       Samuel J. Stumbo               *
*           24 April 2018              *
****************************************
"""

"""
***************************************
*     1. Grab a copy of grades        *
***************************************
"""
import csv
import numpy as np
import string

# Pretty much a copy and past job straight out of Python's documentation on the csv module

# Found this 'sniffer' in Python's documentation,
# I found it when I googled "python csv".
# It basically looks for the format of the file and reads it in as it sees fit... MAGIC!
rows_2 = []
with open('grades.csv', newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    for row in reader:
        rows_2.append(list(row))
        # print(row)

headings = rows_2[0]

assignment_scores = []
print(len(rows_2))

# This iterates through the list and creates lists organized by assignemnt...
# note: This excludes the first row and column, so these will have to be reintroduced when looking at most difficult
# assignment questions.
for j in range(len(rows_2[0])-1):
    for i in range(len(rows_2)-1):
        try:
            assignment_scores[i].append(float(rows_2[i+1][j+1]))
            #print(rows_2[i+1][j+1])
        except:
            assignment_scores.append([0])

#assignment_scores = np.array(assignment_scores)
# transposed = []
# for i in range(len(assignment_scores[:][0])+1):
#     transposed.append([row[i] for row in assignment_scores])
# print(transposed)


""" 
********************************************
*       2. What's the average?             *
*    Percentage of students above average  *
*           Median Score?                  *
*           Above Median?                  *
********************************************
"""

# Looks for a column that holds the words "final score" in the first row .
final_score_index = 0
for word in rows_2[0]:
    if word.replace(' ', '').lower() == 'finalscore':
        final_score_column = final_score_index
    final_score_index += 1


# Creates an array of final grades
final_grades = []
for i in range(len(rows_2)):
    final_grades.append(rows_2[i][final_score_column])
print(final_grades)
final_grades_float = []
i = 0


# Floats this final grades (besides the first element
for grade in final_grades[1:]:
    final_grades_float.append(float(grade))


# This section uses numpy's mean and median tools to
#   find the mean and median of the final grades
fnl_grd_av = np.mean(final_grades_float)
fnl_grd_median = np.median(final_grades_float)
above_average = []
above_median = []


# Calculates the percentage of folks who were above average
for grade in final_grades_float:
    if grade > fnl_grd_av:
        above_average.append(grade)

percent_above_average = ((len(above_average))/len(final_grades_float)) * 100


# Calculates the number of folks who achieved greater than a median score
for grade in final_grades_float:
    if grade > fnl_grd_median:
        above_median.append(grade)

percent_above_median = ((len(above_median))/len(final_grades_float)) * 100


# Prints out all the data for question 2.
print('Average Score:  {0}% \n'
      'Median Score:   {1}% \n'
      'Above Average:  {2}% \n'
      'Above Median:   {3}%'.format(fnl_grd_av, fnl_grd_median, percent_above_average, percent_above_median))



"""
************************************************
*  3. What was the most difficult assignment?  *
************************************************
"""
assignment_average = []
assignment_max = []
zero_column_count = 0
#for score in assignment_scores:
 #   print(score)

for k in range(len(headings) - 2):
    # for i in range(len(assignment_scores)):
#for assignment in assignment_scores:
    if sum(assignment_scores[k][:]) > 0:
        assignment_max.append(max(assignment_scores[k][:]))
        assignment_average.append(np.mean(assignment_scores[k][:]))

    else:
        #zero_column_count += 1
        continue

print(assignment_max)
wrst_ave_ass_score = min(assignment_average[1:])
hardest_ass_index = np.argmin(wrst_ave_ass_score)
max_worst_ave = assignment_max[hardest_ass_index]
hardest_ass_name = rows_2[0][hardest_ass_index]
print(hardest_ass_index)
print(max(assignment_scores[hardest_ass_index][:]))
print('The hardest assignment was: {0}\n '
      'The average score was: {1}'.format(hardest_ass_name, (wrst_ave_ass_score/max_worst_ave) * 100))




"""
************************************************
*        4. What was the hardest lab?          *
************************************************
"""
labs_index = []
k = 0
count = 0
for i in rows_2[0]:
    try:
        if  'lab' + str(k) + 'exercise' in str(i).lower() :
            labs_index.append(i)

        else:
            continue
            count += 1
    except:
        print('Raised an exception')
    k += 1

print(count)
"""
**************************************************************************
*  5. Assuming standard distribution, how many students get each grade?  *
************************************************************************** 
"""




"""
********************************************************************************
*             6. How many students will complain about their grade?            *
*       Note: They complain if they are within 0.5% of getting a higher grade  *
********************************************************************************
"""


"""
7. What are the grade cutoffs if we want 10% to get As
20% to get Bs
30% to get a C
30% to get a D
and Fs for the rest
"""
