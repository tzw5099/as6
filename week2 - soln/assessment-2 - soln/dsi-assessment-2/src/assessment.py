## Fill each each function stub according to the docstring.
## To run the unit tests: Make sure you are in the root dir:assessment-2
## Then run the tests with this command: "make test"

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
import numpy as np
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
# ax.plot(x, y)


def max_lists(list1, list2):
    '''
    INPUT: list, list
    OUTPUT: list

    list1 and list2 have the same length. Return a list which contains the
    maximum element of each list for every index.
    '''
    list3 = []
    for x in range(len(list1)):
        if list1[x]>list2[x]:
            list3.append(list1[x])
        else:
            list3.append(list2[x])
    return list3


def get_diagonal(mat):
    index_start = mat[0][0]
    mat_diag = []
    len_mat = len(mat[0])
    for x in range(len(mat)):
        if len(mat[x]) == len_mat:
            mat_diag.append(mat[x][x])
        else:
            pass
    return mat_diag


def merge_dictionaries(d1, d2):
    '''
    INPUT: dictionary, dictionary
    OUTPUT: dictionary

    Return a new dictionary which contains all the keys from d1 and d2 with
    their associated values. If a key is in both dictionaries, the value should
    be the sum of the two values.
    '''
    d3 = {}
    both_d1_d2 = list((set(d1).intersection(d2)))

    for (key,val), (k2,v2) in zip(d1.items(), d2.items()):
        if any(key in s for s in both_d1_d2):
            d3[key] = (d1[key] + d2[key])
        else:
            d3[key] = val
            d3[k2] = v2
        print(key, "=>", val)

    return d3


def make_char_dict(filename):
    '''
    INPUT: string
    OUTPUT: dictionary (string => list)

    Given a file containing rows of text, create a dictionary whose keys
    are single characters. The value associated with each key is a list of all
    the line numbers which start with that letter. The first line should have
    line number 1.  Characters which never are the first letter of a line do
    not need to be included in your dictionary.
    '''
    pass


### Pandas
# For each of these, you will be dealing with a DataFrame which contains median
# rental prices in the US by neighborhood. The DataFrame will have these
# columns:
# Neighborhood, City, State, med_2011, med_2014

def pandas_add_increase_column(df):
    '''
    INPUT: DataFrame
    OUTPUT: None

    Add a column to the DataFrame called 'Increase' which contains the
    amount that the median rent increased by from 2011 to 2014.
    '''
    df['Increase']=((df['med_2014']-df['med_2011'])/df['med_2011'])
    return df


def pandas_only_given_state(df, state):
    '''
    INPUT: DataFrame, string
    OUTPUT: DataFrame

    Return a new pandas DataFrame which contains the entries for the given
    state. Only include these columns:
        Neighborhood, City, med_2011, med_2014
    '''
    df_state=df.where(df['State']==state)
    df_state=df_state.dropna()
    return df_state



def pandas_max_rent(df):
    '''
    INPUT: DataFrame
    OUTPUT: DataFrame

    Return a new pandas DataFrame which contains every city and the highest
    median rent from that city for 2011 and 2014.

    Note that city names are not unique and you need to use the state as well
    so that Portland, ME and Portland, OR are recognized as different.

    Your DataFrame should contain these columns:
        City, State, med_2011, med_2014
    '''
    df_max_rent = (df[['City', 'State', 'med_2011', 'med_2014']]).groupby(by=['City',"State"]).max()
    return df_max_rent

    return df[['City', 'State', 'med_2011', 'med_2014']].groupby(["City","State"]).max()
### SQL
# For each of these, your python function should return a string that is the
# SQL statement which answers the question.
# For example:
#    return '''SELECT * FROM rent;'''
# You may want to run "sqlite3 data/housing.sqlite" in the command line to test
# out your queries if the test is failing.
#
# There are two tables in the database with these columns:
# (this is the same data that you dealt with in the pandas questions)
#     rent: Neighborhood, City, State, med_2011, med_2014
#     buy:  Neighborhood, City, State, med_2011, med_2014
# The values in the date columns are integers corresponding to the price on
# that date.

def sql_count_neighborhoods():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the number of neighborhoods in each city
    according to the rent table. Keep in mind that city names are not always
    unique unless you include the state as well, so your result should have
    these columns (though you do not need to name them): city, state, cnt
    '''
    pass


def sql_highest_rent_increase():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the 5 San Francisco neighborhoods with the
    highest rent increase.
    '''
    pass


def sql_rent_and_buy():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the rent price and buying price for 2014 for
    all the neighborhoods in San Francisco.
    Your result should have these columns (though you do not need to name
    them): neighborhood, rent, buy
    '''
    pass
