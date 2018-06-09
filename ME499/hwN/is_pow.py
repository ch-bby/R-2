#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

"""
********************************
* ME 499 HW - N
* Date: 4 June 2018
* Question 1 - is-power
* @author: Samuel J. Stumbo
* file: is_pow.py
********************************
"""

"""
Question 1: Identify if a is a power of b
"""

def is_power(a, b):
    if a % b == 0:
        if a == 0:
            return False
        if b == 0:
            raise ZeroDivisionError("b can't be zero")
        if a/b > 1:
            return is_power(a/b, b)
        elif a == b:
            return True
        else:
            return 'weirdness'
    else:
        return False

if __name__ == "__main__":
    a = 256
    b = 2
    print(is_power(a, b))
