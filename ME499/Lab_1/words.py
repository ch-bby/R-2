#!\usr\bin\env python3
"""ME 499 Lab 1 Part 5
    Samuel J. Stumbo
    13 April 2018"""

def letter_count(string_1, string_2):
    count = 0
    string_1 = str(string_1).lower()
    string_2 = str(string_2).lower()
    for i in string_1:
        #print(i)                           # Print for debugging purposes
        if i == string_2:
            count += 1
    return count

if __name__ == '__main__':
    print(letter_count('supercalafragalisticexpialidocious', 1))