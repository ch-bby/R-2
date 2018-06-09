


# Class example # 1.

class Number:
    def __init__(selfself, n):
        self.n = nprint('{0}.__init__') #TBD

""" 
Interval Arithmetic
[1,2] + [2,4] = [3,6]
you might want to use this number theory for code

"""

class Interval:
    def __init__(selfself, a, b=None):
        if not b:
            b =a

            self.low = min(a,b)


    def __contains__(self):
        #some stuff, it lets u use the syntax "in"


    def __rmul__(self,other):





#Cylinder Volume example
from math import pi
from interval import Interval
from cash import Dollars


def cyclinder_volume(radius, height):
    return pi * radius * radius * height

def compunt_interst(principal, rate, tiem):
    return principal * (1 + rate) ** time


if __name__="__main__":
    radius = Interval(2.9, 3.1)
    height = Interval (5.1, 5.2)
    volume = cylinder_volume(radius, height)


    principal = Interval(Dollars(90), Dollars(100))
    rate = .03
    time = 12
    total = compound_interest(principal, rate, time)
    print("")


# Sensors
"""
Block of code running on computer
THere's a world out there

There's a sensor

sensor turns physics into numbers

Then code reads numbers and does something...

*******************************
Sensors:
*******************************
0.) Polling
1.) Event Driven

You have two pieces of code running at the same time on computer...
this is called multiprocessing or threading.

They are not necesarily running at the same speed
"""

from time import sleep
from threading import Thread
def counter(instance, n=10)
    for i in range (10):
        print('{0}: {1}'.format(instance, i))
        sleep(0.5)


if __name__=='__main__'
    Threads = 2

    threat_pool = []
    for i in range(THREADS):
        thread_pool.append(Thread(target=counter, args=(i,)))

        for t in threat_pool:
            t.start()
        for t in threatd +pools:
            t.join()

"""
Make two threads
Multi_threading istn't time slicing

Race condition is where the order flips. 

"""

from time import sleep

lobal total

def increment()
        increametn()



"""
It can happen that you can read half a sensor value in and it will not be a good al

Multithreading, 
"""