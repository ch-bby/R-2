#!\usr\bin\env python3
#-*- coding: UTF-8 -*-

"""
*****************************
* ME 499 HW N: Probability 1st rand < 2nd rand
* @author: Samuel J. Stumbo
* date: 4 June 2018
* file: prob_1lt2.py
*****************************
"""

"""
This program calculates the probability that, given two numbers chosen randomly,
the first will be less than the second.
"""
from random import Random
def prob_1lt2():
    n = 10**4
    cnt = 0
    for i in range(n):
        lower, upper = 0, 1
        first = Random.uniform(Random(),lower, upper)
        second = Random.uniform(Random(), lower, upper)
        if first<second:
            cnt += 1
    return cnt/n

if __name__ == "__main__":
    print(prob_1lt2())