#!\usr\bin\env python3
"""ME 499 Lab 1 Part 4
    Samuel J. Stumbo
    13 April 2018"""

def close(a, b, c):
    if abs(a - b) < c:
        return True
    else:
        return False

if __name__ == '__main__':
    print(close(2,1,.5))