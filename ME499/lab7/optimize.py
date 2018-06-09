#!\usr\bin\env python3
# *-* coding: UTF-8 *-*


from scipy.optimize import minimize_scalar
import numpy as np
from decimal import Decimal
import random
import matplotlib.pyplot as plt
from pathlib import Path
from math import sin, exp, tan

def optimize_step(f, bounds, n):
    # This function finds the largest value of a function between a set of bounds.
    lower, upper = bounds
    y_max = 0
    cnt = 0
    x_val = 0
    x = np.linspace(lower, upper, n)
    for i in range(len(x)):
        y = f(x[i])
        if y > y_max:
            y_max = y
            x_val = cnt

        cnt += 1

    x_at_y_max = x[x_val]

    return  x_at_y_max




def optimize_random(f, bounds, n):
    # This function does the same thing as 'optimize_step' but takes n random samples
    # in the given interval
    cnt = 0
    lower, upper = bounds
    x = np.random.uniform(lower, upper, n)

    y_max = lower
    x_val = 0
    for i in range(len(x)):
        y = f(x[i])
        if y > y_max:
            y_max = y
            x_val = cnt
        cnt += 1
    x_at_y_max = x[x_val]
    return x_at_y_max

def func(x):
    return x**2

def err_d_f1(f, bounds):
    lower, upper = bounds
    n = [10, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]
    act_x = 10                                           # The actual x value that maximizes the function: UPDATE!!!!
    d_f1 = []
    err = []
    for i in n:
        d_f1.append(optimize_random(func, bounds, i))
    for i in d_f1:
        x = abs(act_x - i)
        err.append(x)

    return err

def err_d_f2(f, bounds):
    lower, upper = bounds
    n = [10, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]
    act_x = 10               # Actual x value that maximizes the function: UPDATE!!!!
    d_f2 = []
    err = []
    for i in n:
        d_f2.append(optimize_random(func, bounds, i))
    for i in d_f2:
        x = abs(act_x - i)
        err.append(x)

    return err

def compare_optimize(f, bounds):
    n = [10, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]
    act_x = 10                                           # Actual x value that maximizes the function: UPDATE!!!!
    err_step = err_d_f1(f, bounds)
    err_rand = err_d_f2(f, bounds)
    pyval = minimize_scalar(lambda x: -x**2, bounds=(0, 10), method='bounded')        # UPDATE FUNCTION
    fig = plt.figure()
    plt.axhline(abs(act_x - pyval.x), 0, 10**6, color='r')
    plt.loglog(n, err_step, n, err_rand)
    plt.grid
    plt.xlabel('values of n (log)')
    plt.ylabel('Error (log)')
    plt.title('Plot of Accuracy versus number of steps for {}'.format('x**2'))          #UPDATE FUNCTION
    plt.legend(['minimize_scalar accuracy', 'Optimize step accuracy', 'Optimize random accuracy'], loc=0)
    plt.text(10**.75, 10**-5, '***minimize_scalar used {0} iterations to converge to this value'.format(pyval.nfev))
    # plt.show()
    # for i in range(20):
    #     fig_name = 'ME 499-L7-PL-{}.png'.format(i)
    #     fig_path = Path(fig_name)
    #     if fig_path.is_file():
    #         print('taken')
    #         continue
    #     else:
    #         fig_name = fig_name
    #         fig.savefig(fig_name)
    return fig

if __name__ == "__main__":
    bounds = (0, 10)
    n = 100
    f = lambda x: x**2
    print(optimize_step(f, bounds, n))
    print(optimize_random(f, bounds, n))

    fig = compare_optimize(func, bounds)
    plt.show()
    #opt_rand = optimize_random(func, bounds, n)
    # pyval = minimize_scalar(lambda x: -sin(x), bounds=(0, 6), method='bounded')
    # print(pyval.nfev)
    #