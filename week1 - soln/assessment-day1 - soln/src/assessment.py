'''
Fill each each function stub (i.e., replace the "pass") according to the
docstring. To run the unit tests make sure you are in the root
dir:assessment-day1. Then run the tests with the command "make test"
'''
import numpy as np
import pandas as pd


# PYTHON SECTION

def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (with counts of each character in input string)

    Return a dictionary which contains
    a count of the number of times each character appears in the string.
    Characters which with a count of 0 should not be included in the
    output dictionary.
    '''
    pass


def invert_dictionary(d):
    '''
    INPUT: DICT
    OUTPUT: DICT (of sets of input keys indexing the same input values
                  indexed by the input values)

    Given a dictionary d, return a new dictionary with d's values
    as keys and the value for a given key being
    the set of d's keys which shared the same value.
    e.g. {'a': 2, 'b': 4, 'c': 2} => {2: {'a', 'c'}, 4: {'b'}}
    '''
    pass


def word_count(filename):
    '''
    INPUT: STRING
    OUTPUT: INT, INT, INT (a tuple with line, word,
                           and character count of named INPUT file)

    The INPUT filename is the name of a text file.
    The OUTPUT is a tuple containting (in order)
    the following stats for the text file:
      1. number of lines
      2. number of words (broken by whitespace)
      3. number of characters
    '''
    pass


def matrix_multiplication(A, B):
    '''
    INPUT: LIST (of length n) OF LIST (of length n) OF INTEGERS,
            LIST (of length n) OF LIST (of length n) OF INTEGERS
    OUTPUT: LIST OF LIST OF INTEGERS
            (storing the product of a matrix multiplication operation)

    Return the matrix which is the product of matrix A and matrix B
    where A and B will be (a) integer valued (b) square matrices
    (c) of size n-by-n (d) encoded as lists of lists.
    
    For example:
    A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]] corresponds to the matrix

        | 2  3  4 |
        | 6  4  2 |
        |-1  2  0 |
    
    Please do not use numpy. Write your solution in straight python.
    '''
    pass


# PROBABILITY SECTION

def cookie_jar(a, b):
    '''
    INPUT: FLOAT (probability of drawing a chocolate cooking from Jar A),
            FLOAT (probability of drawing a chocolate cooking from Jar B)
    OUTPUT: FLOAT (conditional probability that cookie was drawn from Jar A
                   given that a chocolate cookie was drawn)

    There are two jars of cookies.
    Each has chocolate and peanut butter cookies.
    INPUT 'a' is the fraction of cookies in Jar A which are chocolate
    INPUT 'b' is the fraction of cookies in Jar B which are chocolate
    A jar is chosen at random and a cookie is drawn.
    The cookie is chocolate.
    Return the probability that the cookie came from Jar A.
    '''
    pass


# NumPy SECTION


def array_work(rows, cols, scalar, matrixA):
    '''
    INPUT: INT, INT, INT, NUMPY ARRAY
    OUTPUT: NUMPY ARRAY
    (of matrix product of r-by-c matrix of "scalar"'s time matrixA)

    Create matrix of size (rows, cols) with elements initialized to the scalar
    value. Right multiply that matrix with the passed matrixA (i.e. AB, not
    BA).  Return the result of the multiplication.  You needn't check for
    matrix compatibililty, but you accomplish this in a single line.

    E.g., array_work(2, 3, 5, [[3, 4], [5, 6], [7, 8]])
           [[3, 4],      [[5, 5, 5],
            [5, 6],   *   [5, 5, 5]]
            [7, 8]]
    '''
    pass


def boolean_indexing(arr, minimum):
    '''
    INPUT: NUMPY ARRAY, INT
    OUTPUT: NUMPY ARRAY
    (of just elements in "arr" greater or equal to "minimum")

    Return an array of only the elements of "arr" that are greater than or
    equal to "minimum"

    Ex:
    In [1]: boolean_indexing([[3, 4, 5], [6, 7, 8]], 7)
    Out[1]: array([7, 8])
    '''
    pass


# Pandas SECTION

def make_series(start, length, index):
    '''
    INPUTS: INT, INT, LIST (of length "length")
    OUTPUT: PANDAS SERIES (of "length" sequential integers
             beginning with "start" and with index "index")

    Create a pandas Series of length "length" with index "index"
    and with elements that are sequential integers starting from "start".
    You may assume the length of index will be "length".

    E.g.,
    In [1]: make_series(5, 3, ['a', 'b', 'c'])
    Out[1]:
    a    5
    b    6
    c    7
    dtype: int64
    '''
    pass


def data_frame_work(df, colA, colB, colC):
    '''
    INPUT: DATAFRAME, STR, STR, STR
    OUTPUT: None

    Insert a column (colC) into the dataframe that is the sum of colA and colB.
    Assume that df contains columns colA and colB and that these are numeric.
    '''
    pass


# SQL SECTION

# For each of these, your python function should return a string that is the
# SQL statement which answers the question.  
#
# For example:
#    
#    return "SELECT * FROM farmersmarkets;"
#
# You may want to test your queries using sqlite3 or postgresql.  Both
# databases - markets.sqlite (sqlite3) and markets.sql (postgreSQL) are in the
# dsi-assessment-day1/data directory.  Testing your queries with sqlite3 or
# postgresql is optional.  See the SQL instructions in the README.md if you
# want to do this.
#
# There are two tables in the database with these columns:
#
# statepopulations: state, pop2010, pop2000
#
# farmersmarkets: FMID, MarketName, Website, Street, City,
#    County, State, WIC, WICcash
#    (plus other columns we don't care about for this exercise)
#
# Note: FMID is a unique id for the farmers market.  WIC is a boolean varaible
# that indicates if the market accepts payments from the WIC government
# program.   WICCash is another boolean for a slightly different program.

def markets_per_state():
    '''
    Return a SQL statement which gives the states and a count of the number of
    markets for each state which take WIC or WICcash.
    '''
    pass


def state_population_gain():
    '''
    Return a SQL statement which gives the 10 states with the highest
    population gain from 2000 to 2010.
    '''
    pass


def market_density_per_state():
    '''
    Return a SQL statement which gives a table containing each state, number of
    people per farmers market (using the population number from 2010).  If a
    state does not appear in the farmersmarket table, it should still appear in
    your result with a count of 0.
    '''
    pass
