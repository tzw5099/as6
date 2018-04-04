# COLLAPSE CELL
# PMsearch np.v*
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

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


from sklearn.datasets import load_boston

boston = load_boston()
X = boston.data # housing features
y = boston.target # housing prices
boston
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# rmse(true)
# sklearn.metrics.mean_squared_error()

linear = LinearRegression()
linear.fit(X_train, y_train)

train_predicted = linear.predict(X_train)
test_predicted = linear.predict(X_test)

y_train_predicted = linear.predict(X_train)
y_test_predicted = linear.predict(X_test)


import sklearn.metrics as metrics
metrics.mean_squared_error(y_train, y_train_predicted)
len(y_train)

def my_rmse(y_true, y_pred):
    mse = ((y_true - y_pred)**2).mean()
    return np.sqrt(mse)



print("my rmse is ", (my_rmse(y_train, y_train_predicted)))
print("my rmse is ", (np.sqrt(metrics.mean_squared_error(y_train, y_train_predicted))))
# 21.937540828291326

def my_cross_val_score(X_data, y_data, num_folds=3):
    ''' Returns error for k-fold cross validation. '''
    kf = KFold(n_splits=num_folds)
    error = np.empty(num_folds)
    index = 0
    linear = LinearRegression()
    for train, test in kf.split(X_data):
        linear.fit(X_data[train], y_data[train])
        pred = linear.predict(X_data[test])
        error[index] = my_rmse(pred, y_data[test])
        index += 1
    return np.mean(error)
print("my CV score is ", my_cross_val_score(X_train, y_train, num_folds=5))
