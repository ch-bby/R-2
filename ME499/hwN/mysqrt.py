#!\usr\bin\env python3
#-*- coding: UTF-8 -*-

"""
*************************************
* ME 499 HW N sqrt problem
* @author: Samuel J. Stumbo
* date: 4 June 2018
* file: mysqrt.py
*************************************
"""

import math
def mysqrt(a=4):
    x = 3
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return y

def test_sqrt():
    a = range(1, 100)
    header1 = 'a' + '     ' + 'mysqrt(a)' + '       ' + "math.sqrt(a)" + '    ' + "diff"
    header2 = '-' + '     ' + '---------' + '       ' + "------------" + '    ' + "----"
    headers = [header1, header2]
    myval = []
    mathval = []
    diff = []
    for i in a:
        my_y = mysqrt(i)
        myval.append(my_y)
        math_y = math.sqrt(i)
        mathval.append(math_y)
        diff.append(abs(my_y - math_y))

    for header in headers:
        print(header)
    for i in range(len(a)):
        print('%.1f   %.10f    %.10f    %s' %(a[i], myval[i], mathval[i], diff[i]))

if __name__ == "__main__":
    test = test_sqrt()
