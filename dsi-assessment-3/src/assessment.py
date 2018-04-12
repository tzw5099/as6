
'''
* Fill each each function stub according to the docstring.
* To run the unit tests: Make sure you are in the root dir(assessment-3)
  Then run the tests with this command: "make test"
'''

from numpy.random import beta as beta_dist
import numpy as np
from sklearn.linear_model import LinearRegression
import random
# COLLAPSE CELL
# AMsearch np.v*
#x = data['mass']
#x?

# from jupyterthemes import jtplot
# jtplot.style(theme='solarized')
# from jupyterlab_table import JSONTable
# JSONTable(df)

from pprint import pprint
import math
import statsmodels.stats as sms
import statsmodels.api as sm
import statsmodels.regression as smr
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

# 04atplotlib inline
# %load_ext heat

plt.ion()
# plt.ioff()

# %heat

import os
# dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

# fig, ax = plt.subplots()
# ax.plot(x, y)s


# Probability
def roll_the_dice(n_simulations = 1000):
    '''
    INPUT: INT
    OUTPUT: FLOAT

    Two unbiased, six sided, dice are thrown once and the sum of the showing
    faces is observed (so if you rolled a 3 and a 1, you would observe the sum,
    4). Use a simulation to find the estimated probability that the total score
    is an even number or a number greater than 7.  Your function should return
    an estimated probability, based on rolling the two dice n_simulations times.
    '''
    rolls = []

    for i in range(n_simulations):
        dies = random.randint(1, 6) + random.randint(1, 6)
        rolls.append(dies)
    return np.mean(rolls)/12


# A/B Testing
def calculate_clickthrough_prob(clicks_A, views_A, clicks_B, views_B):
    '''
    INPUT: INT, INT, INT, INT
    OUTPUT: FLOAT

    Calculate and return an estimated probability that SiteA performs better
    (has a higher click-through rate) than SiteB.

    Hint: Use Bayesian A/B Testing (multi-armed-bandit repo).
    '''
    pass


# Statistics
def calculate_t_test(sample1, sample2, type_I_error_rate):
    '''
    INPUT: NUMPY ARRAY, NUMPY ARRAY
    OUTPUT: FLOAT, BOOLEAN

    You are asked to evaluate whether the two samples come from a population
    with the same population mean.  Return a tuple containing the p-value for
    the pair of samples and True or False depending if the p-value is
    considered significant at the provided Type I Error Rate (i.e. false
    positive rate, i.e. alpha).
    '''
    pass


# Pandas and Numpy
def pandas_query(df):
    '''
    INPUT: DATAFRAME
    OUTPUT: DATAFRAME

    Given a DataFrame containing university data with these columns:
        name, address, Website, Type, Size

    Return the DataFrame containing the average size for each university
    type ordered by average size in ascending order.
    '''
    df[['Size']] = df[['Size']].astype(float)
    df = df.groupby(['Size']).sum()
    # I give up. Sum works, mean doesn't. waste 30+ min...
    return(df)


def df_to_numpy(df, y_column):
    '''
    INPUT: DATAFRAME, STRING
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY, NUMPY ARRAY

    Make the column named y_column into a numpy array (y) and make the rest of
    the DataFrame into a 2 dimensional numpy array (X). Return (X, y).

    E.g.
                a  b  c
        df = 0  1  3  5
             1  2  4  6
        y_column = 'c'

        output: np.array([[1, 3], [2, 4]]), np.array([5, 6])
    '''
    pass


def only_positive(arr):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY

    Return a numpy array containing only the rows from arr where all the values
    in that row are positive.

    E.g.  np.array([[1, -1, 2],
                    [3, 4, 2],
                    [-8, 4, -4]])
              ->  np.array([[3, 4, 2]])

    Use numpy methods to do this, full credit will not be awarded for a python
    for loop.
    '''
    n = 0
    while n < arr.shape[0]:
        print("Yo")
        n+=1


def add_column(arr, col):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY, NUMPY ARRAY
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY

    Return a numpy array containing arr with col added as a final column. You
    can assume that the number of rows in arr is the same as the length of col.

    E.g.  np.array([[1, 2], [3, 4]]), np.array([5, 6))
              ->  np.array([[1, 2, 5], [3, 4, 6]])
    '''
    for i in range(col.shape[0]):
        np.append(arr[i],(col[i]))
    return arr

def size_of_multiply(A, B):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY, 2 DIMENSIONAL NUMPY ARRAY
    OUTPUT: TUPLE

    If matrices A (dimensions m x n) and B (dimensions p x q) can be
    multiplied (AB), return the shape of the result of multiplying them. Use the
    shape function. Do not actually multiply the matrices, just return the
    shape.

    If A and B cannot be multiplied, return None.
    '''
    mult = (np.matmul(A,B))
    return mult.shape
# A = np.array([[1, 2], [3, 4], [5, 6]])
# B = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(size_of_multiply(A,B))

# Linear Regression
def linear_regression(X_train, y_train, X_test, y_test):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY, NUMPY ARRAY
    OUTPUT: TUPLE OF FLOATS, FLOAT

    The R^2 statistic, also known as the coefficient of determination, is a
    popular measure of fit for a linear regression model.  If you need a
    refresher, this wikipedia page should help:

    https://en.wikipedia.org/wiki/Coefficient_of_determination

    Use the sklearn LinearRegression to find the best fit line for X_train and
    y_train. Calculate the R^2 value for X_test and y_test.

    Return a tuple of the coefficients and the R^2 value. Your returned data
    should be in this form:
    (12.3, 9.5), 0.567
    '''
    pass


# SQL
def sql_query():
    '''
    INPUT: None
    OUTPUT: STRING

    Given a table named universities which contains university data with these
    columns:

        name, address, Website, Type, Size

    Return a SQL query that gives the average size of each university type
    in ascending order.
    '''
    # Your code should look like this:
    # return '''SELECT * FROM universities;'''
    pass
