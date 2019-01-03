# LinearRegressionByCode
Performing linear Regression by Code by tuning weights using gradient Descent


Gradient Descent Example for Linear Regression
This example project demonstrates how the gradient descent algorithm may be used to solve a linear regression problem. A more detailed description of this example can be found here.

Code Requirements
The example code is in Python (version 3 or higher will work). The only other requirement is Pandas.

Description
This code demonstrates how a gradient descent search may be used to solve the linear regression problem of fitting a line to a set of points. In this problem, we wish to model a set of points using a line. The line model is defined by two parameters - the line's slope m,
and y-intercept b. Gradient descent attemps to find the best values for these parameters, subject to an error function.

The code contains a main function called run. 
This function defines a set of parameters used in the gradient descent algorithm including an initial guess
of the line slope and y-intercept, the learning rate to use, and the number of iterations to run gradient descent for.

The code contains a main function called run. This function defines a set of parameters used in the gradient descent algorithm including an initial guess of the line slope and y-intercept, the learning rate to use, and the number of iterations to run gradient descent for.

initial_b = 0 # initial y-intercept guess
initial_m = 0 # initial slope guess
num_iterations = 1000
Using these parameters a gradient descent search is executed on a sample data set of 100 ponts. Here is a visualization of the search running for 200 iterations using an initial guess of m = 0, b = 0, and a learning rate of 0.00001

Execution
To run the example, simply run the linearRegression.py file using Python

python linearRegression.py
The output will look like this

inital hyper parameters b=0,m=1 error=692.2825498224661
final hyper parameters b=-0.10252297775897005,m=1.4836433839482832 error=111.15976495628857
