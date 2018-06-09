#!usr\bin\env python3
"""
*****************************
*     ME 499 Lab 3          *
*
*     27 April 2018         *
*     Samuel J. Stumbo      *
*****************************
"""

"""
***************************************************
*    Part 4: Mass spring damper function          *
*                                                 *
***************************************************
"""
# Import necessary libraries
import matplotlib.pyplot as plt
import msd

# The msd function is from our dear professor - straight up copy and paste for that part...
# This function returns the plot of the position response of the  mass, spring damper
def smd_plot():
    smd = msd.MassSpringDamper(1.0, 1.0, 1.0)
    state, t = smd.simulate(0.0, 1.0)
    x = []
    for s in state:
        x.append(s[0])

    fig = plt.figure(3)
    plt.plot(t, x)
    plt.xlabel('time [s]')
    plt.ylabel('position [units]')
    plt.title('Mass Spring Damper Position vs. Time')
    return fig
