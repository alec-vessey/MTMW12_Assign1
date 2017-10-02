# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

"""Question 1"""

def sum_of(N):
    """Function to calculate the sum of 0.01 multiple times
    :param: N: number of iterations to run the sum
    :return: the sum of  0.01 over a stated number of iterations
    """
    sum = 0
    for i in xrange(0, N):
        sum +=0.01
    return sum

print sum_of(int(1e4))
print sum_of(int(1e7))

"""Question 2"""

def integration(trig, m, c, lower_limit, upper_limit, number_intervals):
    """This function calculates to integrl of a fnction between known limits
    for y = mx + c functions 
    :param: function: numerical function to integrate between
    :param: lower_limit: the lower limit to calculate the integral
    :param: upper_limit: the upper limit to calculate the integral
    :return: the integral of the function betweent the known limits
    """
    #calculate interval length
    dx = (upper_limit - lower_limit)/number_intervals
    #initialise the integral value
    integral = 0.0

    
    #calculate integral 
    if trig == 'none':
        for i in xrange(0, number_intervals):
            integral += m*(lower_limit+(i+0.5)*dx) - c
        integral *= dx
    if trig == 'sin':
        for i in xrange(0, number_intervals):
            integral += np.sin(m*(lower_limit+(i+0.5)*dx)) - c
        integral *= dx
    if trig == 'cos':
        for i in xrange(0, number_intervals):
            integral += np.cos(m*(lower_limit+(i+0.5)*dx)) - c
        integral *= dx
    if trig == 'tan':
        for i in xrange(0, number_intervals):
            integral += np.tan(m*(lower_limit+(i+0.5)*dx)) - c
        integral *= dx
    
    return integral, dx, number_intervals 
    
#print integration(3, -2, 0, 10, 1)
#print integration(3, -2, 0, 10, 2)
#print integration(3, -2, 0, 10, 3)
#print integration(3, -2, 0, 10, 4)

print integration('sin', 3, 0, 0, np.pi, 20)   #20 intervals
print integration('sin', 1, 0, 0, np.pi, 20)      

#exact solutions for sin
exact = -np.cos(1*np.pi) + np.cos(1*0)
exact = -np.cos(3*np.pi) + np.cos(3*0)

"""Question 3"""

number_intervals = [4000, 40000, 400000, 4000000]
delta_x = []
errors = []
exact = -np.cos(1*np.pi) + np.cos(1*0)
for i in number_intervals:
    val, dx, number = integration('sin', 1, 0, 0, np.pi, i) 
    delta_x.append(dx)
    err = val - exact
    errors.append(err)
    
plt.figure(1)
plt.plot(delta_x, errors)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Delta x')
plt.ylabel('Errors')
plt.show()
