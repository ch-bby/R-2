#!/usr/bin/env python3

"""
ME 499: Lab 2
Samuel J. Stumbo
20 April 2018

GCD Function

A function that takes in two variables and returns their greatest common divisor.
    """

def gcd(a, b):
    # Googled how to do this problem. Ripped off ideas from Stack Overflow.
        if a > b:
            if b == 0:
                return a
            else:
                if a % b == 0:
                    return b
                else:
                    r = a % b
                    return gcd(b, r)
        if a < b:
            if a == 0:
                return b
            else:
                if b % a == 0:
                    return a
                else:
                    r = b % a
                    return gcd(a, r)

if __name__ == '__main__':
    print(gcd(50, 12))

