import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.graphics import regressionplots as smg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from sklearn.preprocessing import scale
from statsmodels.stats.outliers_influence import variance_inflation_factor

#Datasets 
prestige = sm.datasets.get_rdataset("Duncan", "car", cache=True).data
credit_card = sm.datasets.ccard.load_pandas().data

#1.
pd.scatter_matrix(prestige, diagonal = 'kde')
pd.scatter_matrix(credit_card, diagonal = 'kde')

credit_card.boxplot('AGE', by = 'OWNRENT')
credit_card.boxplot('AVGEXP', by = 'OWNRENT')
credit_card.boxplot('INCOME', by = 'OWNRENT')
credit_card.boxplot('INCOMESQ', by = 'OWNRENT')
credit_card.boxplot('AVGEXP') #If just want a single variable

prestige.boxplot('income')
prestige.boxplot('income', by = 'type')

#Model 1
y = prestige['prestige']
x = prestige[['income', 'education']].astype(float)
x['const'] = 1 #Add intercept
prestige_model = sm.OLS(y, x).fit()

prestige_model.summary()

#Model 2
y2 = credit_card['AVGEXP']
x2 = credit_card[['INCOME', 'INCOMESQ', 'OWNRENT', 'AGE']].astype(float)
x2['const'] = 1 #Add intercept
ccard_model = sm.OLS(y2, x2).fit()

ccard_model.summary()

#2.
resids = prestige_model.outlier_test()['student_resid']
resids2 = ccard_model.outlier_test()['student_resid']

#residual plot 1
plt.plot(prestige_model.fittedvalues, resids, 'o') #These look pretty good...
plt.xlabel('studentized residuals')
plt.ylabel('predicted response')
plt.axhline(0, c='r', linestyle = '--')

#residual plot 2
plt.plot(ccard_model.fittedvalues, resids2, 'o') #These do not look that great...
plt.xlabel('studentized residuals')
plt.ylabel('predicted response')
plt.axhline(0, c='r', linestyle = '--')

'''
We use the studentized residuals as opposed to the outright residuals, because this
looks at how extreme a residual is after accounting for the standard error of the 
residuals.  Where simply comparing does not account for this.
'''

#3
'''
It appears that the residuals from the prestige model seem to have 
a better representation of equal variance (homoscedasticity).  The 
residuals from the ccard model definitely appear to fan out.  We do
not want to see heteroscedastic residuals, as this means we do not 
have equal variances.  If we are doing inferential statistics, the
assumption of equal variance is used to assure the accuracy of 
statements regarding 95% confidence intervals (similar with 
hypothesis testing).
'''

hetero_test = sm.stats.diagnostic.het_goldfeldquandt
hetero_test(y, x) 
hetero_test(np.log(y), x) 

hetero_test(y2, x2)
hetero_test(np.log(y2), x2) 
#For all results shows increasing... However, some pvalues are small and others are large.
#Not sure this test's third result is accurate...

#4
#Refit models with log of the response
#Model 1
y_log = np.log(prestige['prestige'])
prestige_model2 = sm.OLS(y_log, x).fit()

#Model 2
y2_log = credit_card['AVGEXP']
ccard_model2 = sm.OLS(y2_log, x2).fit()

#Obtain the residuals
resids_log = prestige_model2.outlier_test()['student_resid']
resids2_log = ccard_model2.outlier_test()['student_resid']

#residual plot 1 with log response
plt.plot(prestige_model2.fittedvalues, resids_log, 'o') #This looks worse than before to me...
plt.xlabel('studentized residuals with log response')
plt.ylabel('predicted log response')
plt.axhline(0, c='r', linestyle = '--')

#residual plot 2 with log response
plt.plot(ccard_model2.fittedvalues, resids2_log, 'o') #These still do not look that great...
plt.xlabel('studentized residuals with log response')
plt.ylabel('predicted log response')
plt.axhline(0, c='r', linestyle = '--')
'''
The hypothesis test was provided above using the log of the response.
'''

#5
sm.graphics.qqplot(resids, line='45', fit=True) #This looks pretty good
sm.graphics.qqplot(resids2, line='45', fit=True) #This looks awful
sm.graphics.qqplot(resids_log, line='45', fit=True) #Still good
sm.graphics.qqplot(resids2_log, line='45', fit=True) #Still awful - a log transfrom doesn't usually assist us with the normality assumption


#6 
'''
Multicollinearity is when we have x-variables that are correlated with one another.
Commonly, if multicollinearity is present, then we might have cases where two x-variables
have a positive relationship with a response, but because they are related to one another, 
when both are placed in the same linear model, we might see a negative coefficient on 
one of the x-variables, when it truly should have a positive relationship with the response.
'''

#Checking our vifs

def vifs(x):
	'''
	Input x as a DataFrame, calculates the vifs for each variable in the DataFrame.
	DataFrame should not have response variable. 
	Returns dictionary where key is column name and value is the vif for that column.
	Requires scipy.stats be imported as scs
	'''
	vifs = []
	for index in range(x.shape[1]):
		vifs.append(round(variance_inflation_factor(x.values, index),2))
	return vifs

vifs(x)

#Since all of our v.i.f.s are under 10, this suggests we do not have any multicollinearity issues with our x-variables


##Part 2
#1
trace = go.Scatter(
    x = prestige_model.fittedvalues,
    y = resids,
    mode = 'markers'
)

data = [trace]

py.iplot(data, filename='basic-scatter')

#2
trace = go.Scatter(
    x = x['income'],
    y = resids,
    mode = 'markers'
)

data = [trace]

py.iplot(data, filename='basic-scatter')

trace = go.Scatter(
    x = x['education'],
    y = resids,
    mode = 'markers'
)

data = [trace]

py.iplot(data, filename='basic-scatter')

#3
smg.influence_plot(prestige_model)
smg.influence_plot(ccard_model)

#4
'''
By removing the outliers, the beta coefficients will more accurately represent the trend.
If there were low outliers, then the coefficients will become larger.  For high outliers,
the coefficients will become smaller.
'''
