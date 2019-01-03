# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 12:25:55 2019

@author: nigaddam
"""

import pandas as pd
def Error(b_current,m_current,data):
    '''
    error intially with hyper parameters b=0 and slope m=1
    '''
    error=0
    b=b_current
    m=m_current
    #size of samples
    N=data.shape[0]
    for i in range(N):
        predicted=m*data.iloc[i][0]+b
        actual=data.iloc[i][1]
        #squaring to get error magnitude positive
        error+=(actual-predicted)**2
    #returning average of error
    return error/N
    

#method accepts data,number of iterations
def gradientDescent(b_starting,m_starting,data,noOfIterations,learning_rate):     
    '''
    Adjusting hyper parameters(Weights) by gradient descent to reduce error with number of 
    iterations and learning rate
    '''
    b=b_starting
    m=m_starting
    
    for i in range(noOfIterations):
        [b,m]=step_gradient_descent(b,m,data,learning_rate)
    return [b,m]    
        
        
def step_gradient_descent(b_current,m_current,data,learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(data))
    for i in range(0, len(data)):
        x = data.iloc[i, 0]
        y = data.iloc[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += (2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current + (learningRate * b_gradient)
    new_m = m_current + (learningRate * m_gradient)
    return [new_b, new_m]


def run():    
    data = pd.read_csv('data.csv',sep=',')
    print("Inital hyper parameters b={0},m={1} error={2}".format(0,1,Error(0,1,data)))
    learning_rate=0.0001    
    [b,m]=gradientDescent(0,0,data,1000,learning_rate)
    print("final hyper parameters b={0},m={1} error={2}".format(b,m,Error(b,m,data)))

    
if __name__=='__main__':
    run()
    