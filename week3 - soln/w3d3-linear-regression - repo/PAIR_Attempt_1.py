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

# plt.ion()
# plt.ioff()

# %heat

import os
# dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

df = pd.read_csv('data/balance.csv')
df




pd.scatter_matrix(df)
