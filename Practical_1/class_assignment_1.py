# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
This script contains code for MTMW12 Introduction to Numerical Modelling
Assignment 1.
"""

#import modules for code
import numpy as np
import matplotlib.pyplot as plt

"""Question 1"""

def sum_of(N):
    """
    Function to calculate the sum of 0.01 multiple times
    :param: N: number of iterations to run the sum
    :return: the sum of  0.01 over a stated number of iterations
    """
    #initialise variable sum
    sum = 0
    for i in xrange(0, N):
        sum +=0.01
    return sum

"""Question 2"""

def integration(trig, m, c, lower_limit, upper_limit, number_intervals):
    """
    This function calculates to integrl of a fnction between known limits
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


"""Question 3"""

def sin_integral_errors(num_ints):
    #initialise variable array names
    delta_x = []
    errors = []
    #calculate the exact values from integrating sin
    exact = -np.cos(1*np.pi) + np.cos(1*0)
    #iterate over N intervals and calculate delta x, and the error and 
    #append to array
    for i in num_ints:
        val, dx, number = integration('sin', 1, 0, 0, np.pi, i) 
        delta_x.append(dx)
        err = val - exact
        errors.append(err)

    ##plot the errors against delta x
    #plt.figure(1)
    #plt.plot(delta_x, errors)
    #plt.yscale('log')
    #plt.xscale('log')
    #plt.xlabel('Delta x')
    #plt.ylabel('Errors')
    #plt.show()

    return errors, dx


def order_of_convergence(error_array, delta_x_array):
    """
    This function calculates the order of convergence of a numerical method,
    which is the change in error relative to the change in resolution between 
    two resolutions
    :param: error_array: an array containing a list of errors of different resoltuions
    :param: error_array: an array containing a list of delta x of different resoltuions
    :return: a list of the order of conveergence
    """
    n_all = []
    for i in range(0,3,1):
        numerator = np.log(error_array[i]) - np.log(error_array[i+1])
        denominator = np.log(delta_x_array[i]) - np.log(delta_x_array[i+1])
        n = numerator / denominator
        n_all.append(n)
    return n_all



def main():
    """
    This function contains commands to execute for the answers for assignment 1
    """
    
    ##Question 1
    #print sum_of(int(1e4))
    #print sum_of(int(1e7))
    
    ##Question 2a
    #print integration('none', 3, -2, 0, 10, 1)
    #print integration('none', 3, -2, 0, 10, 2)
    #print integration('sin', 3, 0, 0, np.pi, 20)   #20 intervals
    #print integration('sin', 1, 0, 0, np.pi, 20)  
    
    ##calculate the exact solutions for sin
    #exact = -np.cos(1*np.pi) + np.cos(1*0)
    #exact = -np.cos(3*np.pi) + np.cos(3*0)
    
    ##Question 2b
    number_intervals = [4000, 40000, 400000, 4000000]
    sin_integral_errors(number_intervals)
    
    ##Question 3
    errors, delta_x = sin_integral_errors(number_intervals)
    print order_of_convergence(errors, delta_x)

if __name__ == '__main__':
    main()
    
#error should decrease as the number of iterations increases as you get closer
#to the true line with more iterations