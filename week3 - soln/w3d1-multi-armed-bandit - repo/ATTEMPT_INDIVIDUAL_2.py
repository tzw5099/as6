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

x = np.arange(0, 1.01, 0.01)
y = stats.uniform().pdf(x)
%matplotlib inline
dfA = pd.read_csv('data/siteA.txt', sep=' ')
dfB = pd.read_csv('data/siteB.txt', sep=' ')
# views=[50,100,200,400,800]
views = 790

def beta_distribution(views, dfA, dfB):
    pA = dfA.mean() # 0.066333
    pB = dfB.mean() # 0.102628

    df_a_50 = dfA['0'].head(views)
    df_b_50 = dfB['0'].head(views)

    a_dfA = sum(df_a_50)
    b_dfA = 800-sum(df_b_50)
    y_prior = stats.beta(a_dfA, b_dfA).pdf(x)

    return(y_prior)

d_beta = beta_distribution(views, dfA, dfB)

views100 = 100
d_beta100 = beta_distribution(views100, dfA, dfB)

y_b = stats.beta(x, d_beta).pdf(x)

def plot_with_fill(x, y, label):
      lines = plt.plot(x, y, label=label, lw=2)
      plt.fill_between(x, 0, y, alpha=0.2, color=lines[0].get_c())

def plot_with_fill(x, y_prior, label):
      lines = plt.plot(x, y_prior, label=label, lw=2)
      plt.fill_between(x, 0, y_prior, alpha=0.2, color=lines[0].get_c())


beta_distribution(views,dfA,dfB)
plot_with_fill(x, y, "Posterior")
plt.legend("Prior")
plot_with_fill(x,d_beta, "Prior")
plot_with_fill(x,d_beta100, "Prior")

a_dfA
b = b_dfA
mean_A = pA

a_df_a_50 = dfA['0'].head(790)
a_df_b_50 = dfA['0'].head(790)

a_dfA_a = sum(df_a_50)
a_dfA_b = 790-sum(df_a_50)




gen_A = stats.beta(a_dfA_a, a_dfA_b, mean_A)
a_800rvs=(gen.rvs(size=10000))
# plt.show(x,a_800rvs)
a_800rvs
dataframe=pd.DataFrame(a_800rvs)
dataframe.hist()
plt.hist(a_800rvs, normed=True, histtype='stepfilled', alpha=0.2)


a_dfA
b = b_dfA
mean_A = pA
gen_A = stats.beta(a_dfA, b_dfA, mean_A)
a_800rvs=(gen.rvs(size=10000))
# plt.show(x,a_800rvs)
a_800rvs
dataframe=pd.DataFrame(a_800rvs)
dataframe.hist()
plt.hist(a_800rvs, normed=True, histtype='stepfilled', alpha=0.2)
