'''
Fill each each function stub (i.e., replace the "pass") according to
the docstring. To run the unit tests make sure you are in the root
dir:assessment-day1. Then run the tests with the command "make test"
Updated for Python 3
'''

import numpy as np
import pandas as pd


# PYTHON SECTION


import numpy as np
import pandas as pd

def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (with counts of each character in input string)

    Return a dictionary which contains
    a count of the number of times each character appears in the string.
    Characters which with a count of 0 should not be included in the
    output dictionary.
    '''
    d = {}
    for char in string:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d


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
    result = {}
    for key, value in d.items():
        if value not in result:
            # We use a set since original keys had no duplicates
            result[value] = set()
        # We can now safely call the .add method
        result[value].add(key)
    return result


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
    with open(filename) as f:
        l, w, c = 0, 0, 0
        for line in f:
            l += 1
            w += len(line.split())
            c += len(line)
    return l, w, c


def matrix_multiplication(A, B):
    '''
    INPUT: LIST (of length n) OF LIST (of length n) OF INTEGERS,
            LIST (of length n) OF LIST (of length n) OF INTEGERS
    OUTPUT: LIST OF LIST OF INTEGERS
            (storing the product of a matrix multiplication operation)

    Return the matrix which is the product of matrix A and matrix B
    where A and B will be (a) integer valued (b) square matrices
    (c) of size n-by-n (d) encoded as lists of lists,  e.g.
    A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]] corresponds to the matrix
    | 2  3  4 |
    | 6  4  2 |
    |-1  2  0 |
    '''

    n = len(A)
    result = []
    # iterate over the rows of A
    for i in range(n):
        row = []
        # iterate over the columns of B
        for j in range(n):
            total = 0
            # iterate ith row of A with jth column of B dot product
            for k in range(n):
                # k implements [ith row][jth column] element-wise dot product
                total += A[i][k] * B[k][j]
            # column j of row i
            row.append(total)
        # all columns j of row i completed
        result.append(row)
    # all rows done
    return result


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

    return a / (a + b)


# NumPy AND Pandas SECTION


def array_work(rows, cols, scalar, matrixA):
    '''
    INPUT: INT, INT, INT, NUMPY ARRAY
    OUTPUT: NUMPY ARRAY
    (of matrix product of r-by-c matrix of "scalar"'s time matrixA)

    Create matrix of size (rows, cols) with elements initialized to
    the scalar value. Right multiply that matrix with the passed
    matrixA (i.e. AB, not BA).  Return the result of the multiplication.
    You needn't check for matrix compatibililty, but you accomplish this
    in a single line.


    E.g., array_work(2, 3, 5, np.array([[3, 4], [5, 6], [7, 8]]))
           [[3, 4],      [[5, 5, 5],
            [5, 6],   *   [5, 5, 5]]
            [7, 8]]
    '''
    return matrixA.dot(np.ones((rows, cols)) * scalar)


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
    return pd.Series(np.arange(length) + start, index=index)


def data_frame_work(df, colA, colB, colC):
    '''
    INPUT: DATAFRAME, STR, STR, STR
    OUTPUT: None

    Insert a column (colC) into the dataframe that is the sum of colA and colB.
    Assume that df contains columns colA and colB and that these are numeric.
    '''
    df[colC] = df[colA] + df[colB]


def boolean_indexing(arr, minimum):
    '''
    INPUT: NUMPY ARRAY, INT
    OUTPUT: NUMPY ARRAY
    (of just elements in "arr" greater or equal to "minimum")

    Return an array of only the elements of "arr"
    that are greater than or equal to "minimum"

    Ex:
    In [1]: boolean_indexing(np.array([[3, 4, 5], [6, 7, 8]]), 7)
    Out[1]: array([7, 8])
    '''
    return arr[arr >= minimum]


def create_data_frame(filename):
    '''
    INPUT: STRING (filename of csv file
                   with no index column and no header row -- only data)
    OUTPUT: DATAFRAME
    (of data in above csv file with default values not from the data
                       for the index column and the header row)

    Return a pandas DataFrame constructed from the csv
    file data in filename. The header and index should
    be assigned default values not extracted from the data
    '''
    return pd.DataFrame.read_csv(filename, header=None, index_col=None)


def reverse_index(arr, finRow, finCol):
    '''
    INPUT: NUMPY ARRAY, INT, INT
    OUTPUT: NUMPY ARRAY (of an upside down subset of "arr")

    Reverse the row order of "arr" (i.e. so the top row is on the bottom)
    and return the sub-matrix from coordinate [0, 0] up to
    (but not including) [finRow, finCol].

    Ex:
    In [1]: arr = np.array([[ -4,  -3,  11],
                            [ 14,   2, -11],
                            [-17,  10,   3]])
    In [2]: reverse_index(arr, 2, 2)
    Out[2]:
    array([[-17, 10],
           [ 14,  2]])

    Hint: this can be using two steps of slicing
    that can be combined into a one-liner.
    '''
    return arr[::-1][:finRow, :finCol]


# SQL SECTION

# For each of these, your python function should return
# a string that is the SQL statement which answers the question.
# For example:
#    return "SELECT * FROM farmersmarkets;"
# You may want to run "sqlite3 markets.sql" in the command line
# to test out your queries.
#
# There are two tables in the database with these columns:
# statepopulations: state, pop2010, pop2000
# farmersmarkets: FMID, MarketName, Website, Street, City,
#    County, State, WIC, WICcash
#    (plus other columns we don't care about for this exercise)


def markets_per_state():
    '''
    INPUT: NONE
    OUTPUT: STRING (of SQL statement)

    Return a SQL statement which gives the states and the
    number of markets for each state which take WIC or WICcash.
    '''

    return '''SELECT State, COUNT(1)
              FROM farmersmarkets
              WHERE WIC='Y' OR WICcash='Y'
              GROUP BY State;'''


def state_population_gain():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL statement which gives the 10 states
    with the highest population gain from 2000 to 2010.
    '''

    return '''SELECT state FROM statepopulations
              ORDER BY (pop2010-pop2000) DESC LIMIT 10;'''


def market_density_per_state():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL statement which gives a table containing each state, number
    of people per farmers market (using the population number from 2010).
    If a state does not appear in the farmersmarket table, it should still
    appear in your result with a count of 0.
    '''

    return '''SELECT p.state, IFNULL(p.pop2010 / m.cnt, 0)
              FROM statepopulations p
              LEFT OUTER JOIN (
                  SELECT state, COUNT(1) AS cnt
                  FROM farmersmarkets 
                  GROUP BY state) m 
              ON p.state=m.state;'''


def markets_taking_wic():
    '''
    INPUT: NONE
    OUTPUT: STRING (of SQL statement)

    Return a SQL statement which gives the percent of markets
    which take WIC or WICcash.
    The WIC and WICcash columns contain either 'Y' or 'N'
    '''

    return '''SELECT (SELECT COUNT(1) FROM
                  farmersmarkets WHERE WIC='Y' OR WICcash='Y') /
                  (SELECT CAST(COUNT(1) AS REAL) FROM farmersmarkets);'''


def markets_populations():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL statement which gives a table containing
    each market name, the state it's in and the state
    population from 2010. Sort by MarketName
    '''

    return '''SELECT MarketName, farmersmarkets.State, pop2010
              FROM farmersmarkets JOIN statepopulations
              ON farmersmarkets.State=statepopulations.state
              ORDER BY MarketName;'''


