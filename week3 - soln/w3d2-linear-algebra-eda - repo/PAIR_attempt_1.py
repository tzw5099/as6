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
import scipy.stats as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

# 03atplotlib inline
# %load_ext heat
import datetime
plt.ion()
# plt.ioff()

# %heat

import os
# dir_path = os.path.dirname(os.path.realpath(__file__))
# cwd = os.getcwd()
# cwd


# df = pd.read_csv('data/201402_trip_data.csv', date_parser=['start_date', 'end_date'])
df = pd.read_csv('data/201402_trip_data.csv')
# 8/29/2013
# df['month'] = df[['start_date']]
df['month'] = pd.DatetimeIndex(df['start_date']).month
df['dayofweek'] = pd.DatetimeIndex(df['start_date']).dayofweek
df['day'] = pd.DatetimeIndex(df['start_date']).day
df['hour'] = pd.DatetimeIndex(df['start_date']).hour
df['date'] = pd.DatetimeIndex(df['start_date']).date
df['start_date'].hist()
# list(df)
['trip_id',
 'duration',
 'start_date',
 'start_station',
 'start_terminal',
 'end_date',
 'end_station',
 'end_terminal',
 'bike_#',
 'subscription_type',
 'zip_code',
 'month',
 'day',
 'hour',
 'dayofweek']

df.groupby(['month'])
df.groupby(['month']).agg(['count'])

df_grouped_month = df.groupby(['month']).agg(['count'])
df_grouped_month['trip_id']

# months = np.array(np.arange(1,13))

# array=np.array(df_grouped['trip_id']['count'])

x_plot  = month
y_plot = count

df_trips = df[['trip_id', 'start_date', 'end_date','date']]

df_grouped_date = df_trips.groupby(['date']).agg(['count'])
df_grouped_date.plot()


df_trips_9to12 = df_trips.where(df['month'] > 7)
df_grouped_9to12 = df_trips_9to12.groupby(['date']).agg(['count'])
df_grouped_9to12.plot()


mean_9to12 = df_grouped_9to12['trip_id'].mean()

std_9to12 = df_grouped_9to12['trip_id'].std()

conf_95_left = mean_9to12 + 1.5 * std_9to12
# 1231.290315

conf_95_right = mean_9to12 - 1.5 * std_9to12
# count    377.717685


df_grouped_date['trip_id'].hist()



# Part 2
