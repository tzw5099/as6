import sys
import numpy as np
import pandas as pd
from performotron import Comparer

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

class RMLSEComparer(Comparer):
    def score(self, predictions):
        log_diff = np.log(predictions+1) - np.log(self.target+1)
        return np.sqrt(np.mean(log_diff**2))

if __name__=='__main__':
    infile = sys.argv[1]
    predictions = pd.read_csv(infile)
    predictions.set_index('SalesID')
    test_solution = pd.read_csv('data/do_not_open/test_soln.csv')
    test_solution.set_index('SalesID')
    c = RMLSEComparer(test_solution.SalePrice)
    c.report_to_slack(predictions.SalePrice)
df_mb = pd.read_csv('data/median_benchmark.csv')
# list(df_mb)
# ['SalesID', 'SalePrice']
df_mb.describe()





df_test= pd.read_csv('data/test.csv', nrows=100)
df_train=pd.read_csv('data/Train.csv', low_memory=False)  # nrows=100,
# list(df_test)

X = df_train.copy()
y = X.pop('SalePrice')




df_mb['SalesID']
list(X)



# https://www.dataquest.io/blog/pandas-big-data/
df_test.dtypes

df_train.memory_usage(deep=True)

df_train.head()

df_train.T.apply(lambda x: x.nunique(), axis=1)
# https://docs.google.com/spreadsheets/d/1ZSBijXBbqQsFaPsHY6cu-QwX-CboiwWuzYOLbqz1wRY/edit#gid=0

df_train[['fiBaseModel']].head()

potential_dummies = df_train[["Steering_Controls","Differential_Type","Travel_Controls","Blade_Type","Backhoe_Mounting","Grouser_Type","Pattern_Changer","Thumb","Track_Type","Hydraulics_Flow","Grouser_Tracks","Coupler_System","Coupler","Tire_Size","Tip_Control","Scarifier","Ripper","Pushblock","Hydraulics","Engine_Horsepower","Enclosure_Type","Blade_Width","Blade_Extension","Turbocharged","Transmission","Stick","Ride_Control","Pad_Type","Forks","Enclosure","Drive_System","ProductGroupDesc","ProductGroup","ProductSize","UsageBand","datasource"]]


for col in df_train:
    print df_train[col].unique()

df_train["Steering_Controls"].unique()

# pd.to_string(df_train)


# df_train[df_train.columns[2]]

for col in range(len(list(potential_dummies))):
    print(potential_dummies[col])
    # print (df_train[col].unique())
len(list(potential_dummies))

df_test_vars=['SalesID',
 'MachineID',
 'ModelID',
 'datasource',
 'auctioneerID',
 'YearMade',
 'MachineHoursCurrentMeter',
 'UsageBand',
 'saledate',
 'fiModelDesc',
 'fiBaseModel',
 'fiSecondaryDesc',
 'fiModelSeries',
 'fiModelDescriptor',
 'ProductSize',
 'fiProductClassDesc',
 'state',
 'ProductGroup',
 'ProductGroupDesc',
 'Drive_System',
 'Enclosure',
 'Forks',
 'Pad_Type',
 'Ride_Control',
 'Stick',
 'Transmission',
 'Turbocharged',
 'Blade_Extension',
 'Blade_Width',
 'Enclosure_Type',
 'Engine_Horsepower',
 'Hydraulics',
 'Pushblock',
 'Ripper',
 'Scarifier',
 'Tip_Control',
 'Tire_Size',
 'Coupler',
 'Coupler_System',
 'Grouser_Tracks',
 'Hydraulics_Flow',
 'Track_Type',
 'Undercarriage_Pad_Width',
 'Stick_Length',
 'Thumb',
 'Pattern_Changer',
 'Grouser_Type',
 'Backhoe_Mounting',
 'Blade_Type',
 'Travel_Controls',
 'Differential_Type',
 'Steering_Controls']
