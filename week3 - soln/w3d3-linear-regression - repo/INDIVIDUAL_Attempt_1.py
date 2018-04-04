# COLLAPSE CELL
# PMsearch np.v*
#x = data['mass']
#x?

# from jupyterthemes import jtplot
# jtplot.style(theme='solarized')
# from jupyterlab_table import JSONTable
# JSONTable(df)

# fold1

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

# fold2

# 03atplotlib inline
# %load_ext heat

plt.ion()
# plt.ioff()

# %heat

import os
# dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()


prestige = sm.datasets.get_rdataset("Duncan", "car", cache=True).data
list(prestige)
# ['type', 'income', 'education', 'prestige']
credit_card = sm.datasets.ccard.load_pandas().data
pd.scatter_matrix(prestige, alpha=0.2)



prestige.boxplot()

pd.scatter_matrix(credit_card, alpha=0.2)
credit_card.boxplot()

# endog - y - dependent variable
# exog - x - independent variable
prestige_y = (prestige[['prestige']])
prestige_x = prestige[['income','education']]
prestige_x['const']=1
prestige_x
credit_card_y = (credit_card[['AVGEXP']])
credit_card_x = credit_card[['AGE', 'INCOME', 'INCOMESQ', 'OWNRENT']]
prestige_x
credit_card
# list(credit_card)

# prestige_exog = sm.add_constant(prestige_x, prepend=False)

# credit_model = sm.OLS(endog=np.log(credit_card_y), exog=credit_card_x).fit

prestige_mod = sm.OLS(prestige_y, prestige_x).fit()
# prestige_mod = sm.OLS(endog = np.log(prestige_y), exog = prestige_x).fit()
print(prestige_mod.summary())
prestige_student_resid = smr.linear_model.OLSResults.outlier_test(prestige_mod)['student_resid']

# plt.scatter(prestige_res.fittedvalues, prestige_student_resid)

prestige_student_resid = prestige_mod.outlier_test()['student_resid']
plt.scatter(prestige_mod.fittedvalues, prestige_student_resid, edgecolor='none', alpha=.3)

'''
credit_card_x = credit_card[['AGE', 'INCOME', 'INCOMESQ', 'OWNRENT']]
# credit_card_exog = sm.add_constant(credit_card_x, prepend=False)
credit_card_mod = sm.OLS(credit_card_y, credit_card_x)
credit_card_res = credit_card_mod.fit()

NOTE: INCORRECT ABOVE. Correct way:
# credit_card_mod = sm.OLS(np.log(credit_card_y), credit_card_exog)
# credit_card_res = credit_card_mod.fit()

Biggest factor = no constant for x
'''
print(credit_card_res.summary())



credit_model = sm.OLS(endog=np.log(credit_card_y), exog=credit_card_x).fit()
credit_model.summary()



# credit_card_student_resid = smr.linear_model.OLSResults.outlier_test(res)['student_resid']

credit_card_student_resid = credit_model.outlier_test()['student_resid']

# prestige_res.fittedvalues

#credit_card_res.fittedvalues



credit_card_y.hist()


np.log(credit_card_y).hist()


credit_card_y.hist()

np.log(credit_card_y)
credit_card_x




sms.diagnostic.HetGoldfeldQuandt().run((credit_card_y),credit_card_x)
# (0.4585839251839294, 0.9846652600038074, 'increasing')
sms.diagnostic.HetGoldfeldQuandt().run(np.log(credit_card_y),credit_card_x)
# (0.39453102907095255, 0.9948502526436053, 'increasing')


# plt.scatter(credit_card_res.fittedvalues,credit_card_student_resid)
# plt.xlabel('Fitted values of AVGEXP')
# plt.ylabel('Studentized Residuals')
plt.scatter(credit_model.fittedvalues,credit_card_student_resid)

plt.scatter(credit_model.fittedvalues, credit_card_student_resid, edgecolor='none', alpha=.3)

import statsmodels.graphics as smg
